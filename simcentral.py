import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
import os
from pathlib import Path
import configparser
import subprocess
from briefing import *

# Initialization
config = configparser.RawConfigParser()

def browseFiles(entry):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")
    entry.delete(0,'end')
    entry.insert(0,filename)
    # Autosave
    if chkbtn_autosave_changes.getvar('chkbtn_autosave_changes_state') == 1:
        save_config()

def openTool(entry):
    if entry['state'] == 'normal':
        subprocess.Popen(entry.get())


def checkCheckbuttonState(index):
    if index=="1":
        if checkbutton_1.getvar('checkbutton_1_state') == "0":
            entry_1.config(state='disabled')
            browse_button_1.config(state='disabled')
            open_button_1.config(state='disabled')
        else:
            entry_1.config(state='enabled')
            browse_button_1.config(state='enabled')
            open_button_1.config(state='enabled')
    if index=="2":
        if checkbutton_2.getvar('checkbutton_2_state') == "0":
            entry_2.config(state='disabled')
            browse_button_2.config(state='disabled')
            open_button_2.config(state='disabled')
        else:
            entry_2.config(state='enabled')
            browse_button_2.config(state='enabled')
            open_button_2.config(state='enabled')
    if index=="3":
        if checkbutton_3.getvar('checkbutton_3_state') == "0":
            entry_3.config(state='disabled')
            browse_button_3.config(state='disabled')
            open_button_3.config(state='disabled')
        else:
            entry_3.config(state='enabled')
            browse_button_3.config(state='enabled')
            open_button_3.config(state='enabled')
    if index=="4":
        if checkbutton_4.getvar('checkbutton_4_state') == "0":
            entry_4.config(state='disabled')
            browse_button_4.config(state='disabled')
            open_button_4.config(state='disabled')
        else:
            entry_4.config(state='enabled')
            browse_button_4.config(state='enabled')
            open_button_4.config(state='enabled')
    if index=="5":
        if checkbutton_5.getvar('checkbutton_5_state') == "0":
            entry_5.config(state='disabled')
            browse_button_5.config(state='disabled')
            open_button_5.config(state='disabled')
        else:
            entry_5.config(state='enabled')
            browse_button_5.config(state='enabled')
            open_button_5.config(state='enabled')
    if index=="7":
        save_config()
        load_config()
    # Autosave
    if chkbtn_autosave_changes.getvar('chkbtn_autosave_changes_state') == 1:
        save_config()

def start_all():
    if (entry_1['state'] == 'normal') or (entry_1['state'] == 'enabled'):
        subprocess.Popen(entry_1.get())
    if (entry_2['state'] == 'normal') or (entry_2['state'] == 'enabled'):
        subprocess.Popen(entry_2.get())
    if (entry_3['state'] == 'normal') or (entry_3['state'] == 'enabled'):
        subprocess.Popen(entry_3.get())
    if (entry_4['state'] == 'normal') or (entry_4['state'] == 'enabled'):
        subprocess.Popen(entry_4.get())
    if (entry_5['state'] == 'normal') or (entry_5['state'] == 'enabled'):
        subprocess.Popen(entry_5.get())

def on_focus_out(event):
    # Autosave
    if chkbtn_autosave_changes.getvar('chkbtn_autosave_changes_state') == 1:
        save_config()

def save_config():
    # Check if config folder exists. If not, create it
    directory = os.path.expanduser('~') + '\\AppData\\Local\\SimCentral\\'
    filename = directory + 'config.ini'
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Check if the file exists. If not, create it
    if not os.path.exists(filename):
        config_template = """
            [SETTINGS]
            autostart_tools = 1

            [CHECKBUTTONS]
            checkbutton_1 = 0
            checkbutton_2 = 0
            checkbutton_3 = 0
            checkbutton_4 = 0
            checkbutton_5 = 0

            [ENTRIES]
            entry_1 = none
            entry_2 = none
            entry_3 = none
            entry_4 = none
            entry_5 = none

            [IRACING]
            irating_difference = 300
            email = none
            series_gt3_fanatec_challenge_fixed = 0
            imsa_iracing_series_fixed = 0
            """
        with open(filename, "w") as f:
            f.write(config_template)
            f.close()
            
    # Set the config
    config.read(filename)
    if checkbutton_1.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_1', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_1', '0')
    if checkbutton_2.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_2', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_2', '0')
    if checkbutton_3.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_3', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_3', '0')
    if checkbutton_4.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_4', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_4', '0')
    if checkbutton_5.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_5', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_5', '0')
    config.set('ENTRIES', 'entry_1', entry_1.get())
    config.set('ENTRIES', 'entry_2', entry_2.get())
    config.set('ENTRIES', 'entry_3', entry_3.get())
    config.set('ENTRIES', 'entry_4', entry_4.get())
    config.set('ENTRIES', 'entry_5', entry_5.get())
    if chkbtn_autostart_tools.instate(['selected']):
        print("yes")
        config.set('SETTINGS', 'autostart_tools', '1')
    else:
        config.set('SETTINGS', 'autostart_tools', '0')
    if chkbtn_autosave_changes.instate(['selected']):
        config.set('SETTINGS', 'autosave_changes', '1')
    else:
        config.set('SETTINGS', 'autosave_changes', '0')
    config.set('IRACING', 'email', entry_iracing_email.get())
    config.set('IRACING', 'irating_difference', entry_irating_diff.get())
    if chkbtn_iracing_fanatec_challenge.instate(['selected']):
        config.set('IRACING', 'series_gt3_fanatec_challenge_fixed', '1')
    else:
        config.set('IRACING', 'series_gt3_fanatec_challenge_fixed', '0')
    if chkbtn_iracing_imsa_fixed_gtp.instate(['selected']):
        config.set('IRACING', 'imsa_iracing_series_fixed', '1')
    else:
        config.set('IRACING', 'imsa_iracing_series_fixed', '0')

    # Write the config
    with open(filename, "w") as f:
        config.write(f)
    
def load_config():
    # Check for the config
    # Check if config folder exists. If not, create it
    directory = os.path.expanduser('~') + '\\AppData\\Local\\SimCentral\\'
    filename = directory + 'config.ini'
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Check if the file exists. If not, create it
    if not os.path.exists(filename):
        config_template = """
[SETTINGS]
autostart_tools = 0
autosave_changes = 0

[CHECKBUTTONS]
checkbutton_1 = 0
checkbutton_2 = 0
checkbutton_3 = 0
checkbutton_4 = 0
checkbutton_5 = 0

[ENTRIES]
entry_1 = none
entry_2 = none
entry_3 = none
entry_4 = none
entry_5 = none

[IRACING]
irating_difference = 300
email = none
series_gt3_fanatec_challenge_fixed = 0
imsa_iracing_series_fixed = 0
            """
        with open(filename, "w") as f:
            f.write(config_template)
            f.close()


    directory = os.path.expanduser('~') + '\\AppData\\Local\\SimCentral\\'
    filename = directory + 'config.ini'
    if os.path.exists(filename):
        config.read(filename)
        entry_1.delete(0,'end')
        entry_1.insert(0,config['ENTRIES']['entry_1'])
        entry_2.delete(0,'end')
        entry_2.insert(0,config['ENTRIES']['entry_2'])
        entry_3.delete(0,'end')
        entry_3.insert(0,config['ENTRIES']['entry_3'])
        entry_4.delete(0,'end')
        entry_4.insert(0,config['ENTRIES']['entry_4'])
        entry_5.delete(0,'end')
        entry_5.insert(0,config['ENTRIES']['entry_5'])
        if config['CHECKBUTTONS']['Checkbutton_1'] == "1":
            checkbutton_1.setvar('checkbutton_1_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_1_state', 0)
            entry_1.config(state='disabled')
            browse_button_1.config(state='disabled')
            open_button_1.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_2'] == "1":
            checkbutton_1.setvar('checkbutton_2_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_2_state', 0)
            entry_2.config(state='disabled')
            browse_button_2.config(state='disabled')
            open_button_2.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_3'] == "1":
            checkbutton_1.setvar('checkbutton_3_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_3_state', 0)
            entry_3.config(state='disabled')
            browse_button_3.config(state='disabled')
            open_button_3.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_4'] == "1":
            checkbutton_1.setvar('checkbutton_4_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_4_state', 0)
            entry_4.config(state='disabled')
            browse_button_4.config(state='disabled')
            open_button_4.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_5'] == "1":
            checkbutton_1.setvar('checkbutton_5_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_5_state', 0)
            entry_5.config(state='disabled')
            browse_button_5.config(state='disabled')
            open_button_5.config(state='disabled')
        if config['SETTINGS']['autostart_tools'] == "1":
            chkbtn_autostart_tools.setvar('chkbtn_autostart_tools_state', 1)
        else:
            chkbtn_autostart_tools.setvar('chkbtn_autostart_tools_state', 0)
        if config['SETTINGS']['autosave_changes'] == "1":
            chkbtn_autostart_tools.setvar('chkbtn_autosave_changes_state', 1)
        else:
            chkbtn_autostart_tools.setvar('chkbtn_autosave_changes_state', 0)
        entry_iracing_email.insert(0,config['IRACING']['email'])
        entry_irating_diff.insert(0, config['IRACING']['irating_difference'])
        if config['IRACING']['series_gt3_fanatec_challenge_fixed'] == "1":
            chkbtn_iracing_fanatec_challenge.setvar('chkbtn_iracing_fanatec_challenge_state', 1)
        else: 
            chkbtn_iracing_fanatec_challenge.setvar('chkbtn_iracing_fanatec_challenge_state', 0)
        if config['IRACING']['imsa_iracing_series_fixed'] == "1":
            chkbtn_iracing_fanatec_challenge.setvar('chkbtn_iracing_imsa_fixed_gtp_state', 1)
        else: 
            chkbtn_iracing_fanatec_challenge.setvar('chkbtn_iracing_imsa_fixed_gtp_state', 0)

def start_briefing():
    briefing_button.configure(text='Running...')

    # Ask user for his iracing password
    iracing_pw = tk.simpledialog.askstring("Password", "Enter iRacing password:", show='*', parent=window)
    # Login to the API and return cookies
    cookies = authenticate(config['IRACING']['email'], iracing_pw)
    # Get road irating
    road_irating = get_road_irating(cookies)
    briefing_log.insert(tk.INSERT, '[+] Current iRating: ' + str(road_irating))
    ## SEASON START
    # Get current season_year and season_quarter
    season_year, season_quarter = get_season_details(cookies)
    briefing_log.insert(tk.INSERT, '\n[+] Current season: ' + str(season_year) + '/' + str(season_quarter))
    ## SERIES START
    # Get the full series list
    full_series_list = get_full_series_list(cookies)
    # GT3 Fanatec Challenge - Fixed
    if config['IRACING']['series_gt3_fanatec_challenge_fixed'] == "1":
        briefing_log.insert(tk.INSERT, '\n[++] GT3 Fanatec Challenge - Fixed')
        car_class_id = "2708"
        GT3_Fanatec_Challenge_Fixed_ID = get_gt3_fanatec_challenge_fixed_id(full_series_list)
        if GT3_Fanatec_Challenge_Fixed_ID:
            briefing_log.insert(tk.INSERT, '\n[+++] ID is: ' + str(GT3_Fanatec_Challenge_Fixed_ID))
            briefing_log.insert(tk.INSERT, '\n[+++] Getting GT3 Fanatec Challenge - Fixed results...')
            track, required_avg_laptime = series_results_worker(cookies, GT3_Fanatec_Challenge_Fixed_ID, season_year, season_quarter, road_irating, int(config['IRACING']['irating_difference']), car_class_id)
            briefing_log.insert(tk.INSERT, '\n[+++] Current track is: ' + str(track))
            briefing_log.insert(tk.INSERT, '\n[+++] Required average lap time for your rating is: ' + str(required_avg_laptime) + '\n')
        else:
            briefing_log.insert(tk.INSERT, '\n[+++] Didn\'t find the series - exiting...\n')
            exit
    # IMSA iRacing Series - Fixed
    if config['IRACING']['imsa_iracing_series_fixed'] == "1":
        car_class_id = "4029"
        briefing_log.insert(tk.INSERT, '\n[++] IMSA iRacing Series - Fixed')
        IMSA_Fixed_ID = get_imsa_fixed_id(full_series_list)
        if IMSA_Fixed_ID:
            briefing_log.insert(tk.INSERT, '\n[+++] ID is: ' + str(IMSA_Fixed_ID))
            briefing_log.insert(tk.INSERT, '\n[+++] IMSA iRacing Series - Fixed results...')
            track, required_avg_laptime = series_results_worker(cookies, IMSA_Fixed_ID, season_year, season_quarter, road_irating, int(config['IRACING']['irating_difference']), car_class_id)
            briefing_log.insert(tk.INSERT, '\n[+++] Current track is: ' + str(track))
            briefing_log.insert(tk.INSERT, '\n[+++] Required average lap time for your rating is: ' + str(required_avg_laptime) + '\n')
        else:
            briefing_log.insert(tk.INSERT, '\n[+++] Didn\'t find the series - exiting...\n')
            exit

    briefing_button.configure(text='Refresh data')

# Window
window = ttk.Window(themename='superhero')
window.title('SimCentral')
window.iconbitmap("icons8-automation-48.ico")
window.bind("<FocusOut>", on_focus_out)
window.resizable(False,False)

# left frame
left_frame = ttk.Frame(master=window)
left_frame.pack(side='left', expand='True', fill='both', padx=5)

# menu frame
menu_frame = ttk.Frame(master=left_frame, width=15)
menu_label = ttk.Label(master=menu_frame, text="Menu", font=['Segoe UI', 15, 'bold'])
menu_label.pack(pady=5)

# load config button
load_cfg_button = ttk.Button(master=menu_frame, text='Load config', command=lambda:load_config())
load_cfg_button.configure(width='15')
load_cfg_button.pack(pady=10)

# save config button
save_cfg_button = ttk.Button(master=menu_frame, text="Save config", command=lambda:save_config())
save_cfg_button.configure(width='15')
save_cfg_button.pack()
menu_frame.pack(expand='True', fill='both')

# Exit frame
exit_frame = ttk.Frame(master=window)
exit_frame.pack()

# Exit button
exit_button = ttk.Button(master=left_frame, text="Exit", command=window.destroy)
exit_button.configure(width='15')
exit_button.pack(pady=10)


# notebook widget
notebook = ttk.Notebook(master=window)

# Tab quickstart
tab_quickstart = ttk.Frame(master=notebook)
frame_entries = ttk.Frame(master=tab_quickstart, borderwidth=10)
frame_entries.pack()

# entries
frame_entry1 = ttk.Frame(master=frame_entries, width=30)
frame_entry2 = ttk.Frame(master=frame_entries, width=30)
frame_entry3 = ttk.Frame(master=frame_entries, width=30)
frame_entry4 = ttk.Frame(master=frame_entries, width=30)
frame_entry5 = ttk.Frame(master=frame_entries, width=30)
frame_entry1.pack()
frame_entry2.pack()
frame_entry3.pack()
frame_entry4.pack()
frame_entry5.pack()
entry_1 = ttk.Entry(master=frame_entry1, width=100)
entry_2 = ttk.Entry(master=frame_entry2, width=100)
entry_3 = ttk.Entry(master=frame_entry3, width=100)
entry_4 = ttk.Entry(master=frame_entry4, width=100)
entry_5 = ttk.Entry(master=frame_entry5, width=100)
browse_button_1 = ttk.Button(master=frame_entry1, text="Browse", command=lambda:browseFiles(entry_1))
browse_button_2 = ttk.Button(master=frame_entry2, text="Browse", command=lambda:browseFiles(entry_2))
browse_button_3 = ttk.Button(master=frame_entry3, text="Browse", command=lambda:browseFiles(entry_3))
browse_button_4 = ttk.Button(master=frame_entry4, text="Browse", command=lambda:browseFiles(entry_4))
browse_button_5 = ttk.Button(master=frame_entry5, text="Browse", command=lambda:browseFiles(entry_5))
open_button_1 = ttk.Button(master=frame_entry1, text='Open', command=lambda:openTool(entry_1))
open_button_2 = ttk.Button(master=frame_entry2, text='Open', command=lambda:openTool(entry_2))
open_button_3 = ttk.Button(master=frame_entry3, text='Open', command=lambda:openTool(entry_3))
open_button_4 = ttk.Button(master=frame_entry4, text='Open', command=lambda:openTool(entry_4))
open_button_5 = ttk.Button(master=frame_entry5, text='Open', command=lambda:openTool(entry_5))
checkbutton_1 = ttk.Checkbutton(master=frame_entry1, style='Roundtoggle.Toolbutton', variable='checkbutton_1_state', command=lambda:checkCheckbuttonState("1"))
checkbutton_2 = ttk.Checkbutton(master=frame_entry2, style='Roundtoggle.Toolbutton', variable='checkbutton_2_state', command=lambda:checkCheckbuttonState("2"))
checkbutton_3 = ttk.Checkbutton(master=frame_entry3, style='Roundtoggle.Toolbutton', variable='checkbutton_3_state', command=lambda:checkCheckbuttonState("3"))
checkbutton_4 = ttk.Checkbutton(master=frame_entry4, style='Roundtoggle.Toolbutton', variable='checkbutton_4_state', command=lambda:checkCheckbuttonState("4"))
checkbutton_5 = ttk.Checkbutton(master=frame_entry5, style='Roundtoggle.Toolbutton', variable='checkbutton_5_state', command=lambda:checkCheckbuttonState("5"))
checkbutton_1.pack(pady=10, side='left')
checkbutton_2.pack(pady=10, side='left')
checkbutton_3.pack(pady=10, side='left')
checkbutton_4.pack(pady=10, side='left')
checkbutton_5.pack(pady=10, side='left')
entry_1.pack(pady=10, side='left')
entry_2.pack(pady=10, side='left')
entry_3.pack(pady=10, side='left')
entry_4.pack(pady=10, side='left')
entry_5.pack(pady=10, side='left')
browse_button_1.pack(side='left')
browse_button_2.pack(side='left')
browse_button_3.pack(side='left')
browse_button_4.pack(side='left')
browse_button_5.pack(side='left')
open_button_1.pack(padx=5, side='left')
open_button_2.pack(padx=5, side='left')
open_button_3.pack(padx=5, side='left')
open_button_4.pack(padx=5, side='left')
open_button_5.pack(padx=5, side='left')

# start_all button
start_all_button = ttk.Button(master=tab_quickstart, text='Open all', command=lambda:start_all(), width=16)
start_all_button.pack(side='right', padx=20)


# Setups Tab
tab_setuptool = ttk.Frame(master=notebook)
frame_setuptool = ttk.Frame(master=tab_setuptool, borderwidth=10)
frame_setuptool.pack()
setups_notebook = ttk.Notebook(master=tab_setuptool)
tab_setups_gng = ttk.Frame(master=setups_notebook)
setups_notebook.add(tab_setups_gng, text="GNG")
tab_setups_vrs = ttk.Frame(master=setups_notebook)
setups_notebook.add(tab_setups_vrs, text="VRS")
setups_notebook.pack(side='left', expand='True', fill='both', padx=5)

# Briefing Tab
tab_briefing = ttk.Frame(master=notebook)
frame_briefing_infos = ttk.Frame(master=tab_briefing)
frame_briefing_output = ttk.Frame(master=tab_briefing, width=50)
lbl_briefing_intro = ttk.Label(master=tab_briefing, text='Currently only supported for iRacing. This tool will analyze sessions for the current week and give you an estimated lap time based on your irating.')
labelframe_input=ttk.LabelFrame(master=frame_briefing_infos, text='Settings')
labelframe_output=ttk.LabelFrame(master=frame_briefing_output, text='Briefing area')
labelframe_series=ttk.LabelFrame(master=frame_briefing_infos, text='iRacing Series')
briefing_button = ttk.Button(master=labelframe_output, text='Start', command=lambda:start_briefing())
briefing_log = ttk.ScrolledText(master=labelframe_output, wrap = tk.WORD, width=70, height=10) 
label_iracing_email = ttk.Label(master=labelframe_input, text='iRacing eMail: ')
label_irating_diff = ttk.Label(master=labelframe_input, text='irating difference: ')
label_irating_diff_recommended = ttk.Label(master=labelframe_input, text='Recommended: 300 ')
entry_iracing_email = ttk.Entry(master=labelframe_input, width=30)
entry_irating_diff = ttk.Entry(master=labelframe_input, width=4, justify='center')
chkbtn_iracing_fanatec_challenge = ttk.Checkbutton(master=labelframe_series, style='Roundtoggle.Toolbutton', variable='chkbtn_iracing_fanatec_challenge_state', command=lambda:checkCheckbuttonState("8"))
chkbtn_iracing_imsa_fixed_gtp = ttk.Checkbutton(master=labelframe_series, style='Roundtoggle.Toolbutton', variable='chkbtn_iracing_imsa_fixed_gtp_state', command=lambda:checkCheckbuttonState("9"))
label_iracing_fanatec_challenge = ttk.Label(master=labelframe_series, text='GT3 Fanatec Challenge Fixed')
label_iracing_imsa_fixed_GTP = ttk.Label(master=labelframe_series, text='IMSA iRacing Series - Fixed (GTP)')
lbl_briefing_intro.grid(row=0,column=0, padx=5, pady=10, sticky='nw', columnspan=2)
frame_briefing_infos.grid(row=0, column=0, sticky='nw', pady=30)
frame_briefing_output.grid(row=0, column=1, sticky='nw', pady=30)
labelframe_input.grid(row=1,column=0, padx=5, pady=10, sticky='nw')
labelframe_output.grid(row=1,column=1, padx=5, pady=10, sticky='ne')
labelframe_series.grid(row=2, column=0, padx=5, sticky='nw')
label_iracing_email.grid(row=0, column=0, sticky='w', padx=5)
entry_iracing_email.grid(row=0, column=1, padx=5, sticky='w')
label_irating_diff.grid(row=1, column=0, sticky='w', padx=5)
entry_irating_diff.grid(row=1, column=1, padx=5, pady=5, sticky='w')
label_irating_diff_recommended.grid(row=1, column=1, padx=40, sticky='e')
chkbtn_iracing_fanatec_challenge.grid(row=0, column=0, padx=5, pady=5)
chkbtn_iracing_imsa_fixed_gtp.grid(row=1, column=0, padx=5, pady=5)
label_iracing_fanatec_challenge.grid(row=0, column=1, sticky='w', padx=5)
label_iracing_imsa_fixed_GTP.grid(row=1, column=1, sticky='w', padx=5)
briefing_button.grid(row=0, column=0, padx=5, pady=5)
briefing_log.grid(row=1, column=0, padx=5, pady=5, sticky='w')

# Tab settings
tab_settings = ttk.Frame(master=notebook)
frame_settings = ttk.Frame(master=tab_settings, borderwidth=10)
frame_settings.pack(side='left', expand='True', fill='both', padx=5)

chkbtn_autostart_tools = ttk.Checkbutton(master=frame_settings, style='Roundtoggle.Toolbutton', variable='chkbtn_autostart_tools_state', command=lambda:checkCheckbuttonState("6"))
chkbtn_autostart_tools.grid(row=0, column=0)
lbl_autostart_tools = ttk.Label(master=frame_settings, text='Autostart enabled tools')
lbl_autostart_tools.grid(row=0, column=1, sticky='w')

chkbtn_autosave_changes = ttk.Checkbutton(master=frame_settings, style='Roundtoggle.Toolbutton', variable='chkbtn_autosave_changes_state', command=lambda:checkCheckbuttonState("7"))
chkbtn_autosave_changes.grid(row=1, column=0)
lbl_autosave_changes = ttk.Label(master=frame_settings, text="AutoSave settings on change")
lbl_autosave_changes.grid(row=1, column=1, sticky='w')



notebook.add(tab_quickstart, text='Tool Quickstart')
notebook.add(tab_setuptool, text='Setup Sync')
notebook.add(tab_briefing, text="Briefing")
notebook.add(tab_settings, text='Settings')
notebook.pack(padx=5, pady=10)




# run
load_config()
if config['SETTINGS']['autostart_tools'] == "1":
        start_all()
window.mainloop()