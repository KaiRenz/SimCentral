import hashlib
import base64
import requests
import urllib.parse
import json
from datetime import datetime, timedelta
import numpy as np


def encode_pw(username, password):
    initialHash = hashlib.sha256((password + username.lower()).encode('utf-8')).digest()
    hashInBase64 = base64.b64encode(initialHash).decode('utf-8')
    return hashInBase64


def authenticate(username, password):
    pwValueToSubmit = encode_pw(username, password)
    s = requests.Session()

    # api-endpoint
    URL = "https://members-ng.iracing.com/auth"
    
    # defining a params dict for the parameters to be sent to the API
    payload = 'email='+urllib.parse.quote(username)+'&password='+urllib.parse.quote(pwValueToSubmit)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # sending get request and saving the response as response object
    r = s.request("POST", URL, headers=headers, data=payload)

    return(r.cookies)

def get_driver_details(cookies):
    s = requests.Session()
    payload={}
    s.cookies.update(cookies)
    URL = "https://members-ng.iracing.com/data/member/info"
    r = s.request("GET", URL, data=payload)
    json_response = json.loads(r.text)
    r = s.request("GET", json_response['link'])
    json_response = json.loads(r.text)
    return json_response

def get_road_irating(cookies):
    driver_details = get_driver_details(cookies)
    return driver_details['licenses']['road']['irating']

def get_full_series_list(cookies):
    # Get full series list 
    s = requests.Session()
    payload={}
    s.cookies.update(cookies)
    URL = "https://members-ng.iracing.com/data/series/get"
    r = s.request("GET", URL, data=payload)
    json_response = json.loads(r.text)
    series_list = json.loads(s.request("GET", json_response['link']).text)
    return series_list


def get_gt3_fanatec_challenge_fixed_id(full_series_list):
    for series in full_series_list:
        if series['series_name'] == "GT3 Fanatec Challenge - Fixed":
            return series['series_id']
    return False

def get_imsa_fixed_id(full_series_list):
    for series in full_series_list:
        if series['series_name'] == "IMSA iRacing Series - Fixed":
            return series['series_id']
    return False


def get_series_results(cookies, series_id, season_year, season_quarter, race_week_num):
    s = requests.Session()
    payload = {}
    s.cookies.update(cookies)
    d = datetime.now() - timedelta(days=7)
    timestamp = d.strftime('%Y-%m-%dT%H:%M:%SZ')
    URL = "https://members-ng.iracing.com/data/results/search_series?series_id="+str(series_id)+"&event_types=5&season_year="+str(season_year)+"&season_quarter="+str(season_quarter)+"&race_week_num="+str(race_week_num)
    r = s.request("GET", URL, data=payload)
    json_response = json.loads(r.text)
    base_download_url = json_response['data']['chunk_info']['base_download_url']
    chunk_file_names = json_response['data']['chunk_info']['chunk_file_names']
    series_results = []

    for chunk_file in chunk_file_names:
        r = s.request("GET", base_download_url + chunk_file, data=payload)
        series_results.append(json.loads(r.text))
    return series_results


def get_race_week(cookies):
    s = requests.Session()
    payload = {}
    s.cookies.update(cookies)
    URL = "https://members-ng.iracing.com/data/season/race_guide"
    r = s.request("GET", URL, data=payload)
    json_response = json.loads(r.text)
    r = s.request("GET", json_response['link'])
    json_response = json.loads(r.text)
    return json_response['sessions'][0]['race_week_num']


def filter_session_ids(series_results):
    subsession_ids = []
    for series_result in series_results[0]:
        subsession_ids.append(series_result['subsession_id'])
    return subsession_ids

def convert_laptime(laptime):
    minutes = 0
    laptime = laptime / 600000
    while laptime >= 1:
        minutes = minutes + 1
        laptime = (laptime- 1)
    seconds = laptime * 60
    return (str(minutes)+":"+str(round(seconds,3)))

def convert_laptime_to_seconds(laptime):
    minutes = 0
    laptime = laptime / 600000
    while laptime >= 1:
        minutes = minutes + 1
        laptime = (laptime- 1)
    seconds = laptime * 60
    return seconds

def get_average_lap_times(subsession_ids, irating, cookies, irating_difference, car_class_id):
    average_laps = []
    s = requests.Session()
    payload = {}
    s.cookies.update(cookies)
    for subsession_id in subsession_ids:
        # Get session details
        URL = "https://members-ng.iracing.com/data/results/get?subsession_id=" + str(subsession_id)
        r = s.request("GET", URL, data=payload)
        json_response = json.loads(r.text)
        r = s.request("GET", json_response['link'])
        json_response = json.loads(r.text)
        # Now filter for drivers with similar rating and save their average_lap
        for i in range(len(json_response['session_results'])):
            if json_response['session_results'][i]['simsession_type_name'] == "Race":
                race_results_overall = json_response['session_results'][i]['results']
                for race_result_pp in race_results_overall:
                    if (irating-irating_difference) <= race_result_pp['newi_rating'] <= (irating+irating_difference):
                        interval_in_seconds = convert_laptime_to_seconds(race_result_pp['class_interval'])
                        #average_laps.append([race_result_pp['display_name'],race_result_pp['average_lap'],race_result_pp['newi_rating'],convert_laptime(race_result_pp['average_lap'])])
                        if (race_result_pp['average_lap'] != 0) and (interval_in_seconds > 0) and (interval_in_seconds < 60) and (str(race_result_pp['car_class_id']) == str(car_class_id)):
                            average_laps.append(race_result_pp['average_lap'])
    return average_laps, (json_response['track']['track_name'] + " - " + json_response['track']['config_name'])

def calculate_required_laptime(average_lap_times):
    laptime_sum = 0
    for laptime in average_lap_times:
        laptime_sum = laptime_sum + laptime
    return laptime_sum / len(average_lap_times)

def find_outliers_in_laptimes(average_lap_times):
    # find q1 and q3 values
    q1, q3 = np.percentile(sorted(average_lap_times), [25, 75])
 
    # compute IRQ
    iqr = q3 - q1
 
    # find lower and upper bounds
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
 
    not_outliers = [x for x in average_lap_times if x > lower_bound or x < upper_bound]
    outliers = [x for x in average_lap_times if x <=  lower_bound or x >= upper_bound]
    for outlier in outliers:
        average_lap_times.remove(outlier)
    return(average_lap_times)



def series_results_worker(cookies, series_id, season_year, season_quarter, irating, irating_difference, car_class_id):
    # First, get race_week
    race_week_num = get_race_week(cookies)
    # Get all the results for this series and the current season year and quarter
    series_results = get_series_results(cookies, series_id, season_year, season_quarter, race_week_num)
    # Get the subsession_ids for those races
    subsession_ids = filter_session_ids(series_results)
    # Get the details of each subsession and extract the lap times for similar irating drivers
    average_lap_times, track = get_average_lap_times(subsession_ids, irating, cookies, irating_difference, car_class_id)
    # Find outliers in the average lap times
    filtered_average_lap_times = find_outliers_in_laptimes(average_lap_times)
    # Calculate required average lap time
    required_avg_laptime = convert_laptime(calculate_required_laptime(filtered_average_lap_times))
    return track, required_avg_laptime

def get_season_details(cookies):
    s = requests.Session()
    payload={}
    s.cookies.update(cookies)
    URL = "https://members-ng.iracing.com/data/series/seasons"
    r = s.request("GET", URL, data=payload)
    json_response = json.loads(r.text)
    seasons_info = json.loads(s.request("GET", json_response['link']).text)

    return seasons_info[-1]['season_year'],seasons_info[-1]['season_quarter'] 