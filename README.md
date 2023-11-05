
# SimCentral

SimCentral is a collection of tools to help you with your everyday Sim Racing and consists of scripts and smaller tools I've created over the months.

It is written in Python and uses tkinter for the UI. Please note that I'm not a programmer and this is my first tkinter project :sweat_smile: Let me know if you find anything that needs fixing or can be improved.







## Features
Currently there are 3 features planned:
* Tool Quickstart
* Setup Sync
* Briefing

Setup Sync is not yet implemented. This feature will help you sync all setups from services you are subscribed to like VRS or GNG.

### Tool Quickstart
Here you can define up to 5 tools which can be opened all at once (also automatically on startup). I use this for all the tools I need to start racing... like iOverlay, iRacing, Trading Paints, etc...
![quickstart](https://github.com/KaiRenz/SimCentral/assets/52081463/67ecd20b-33f9-4ae5-83df-cea6d6afb05f)  



### Briefing

Since I'm not racing everyday (more like once or twice a week), I wanted to have some insights on how competitive I am on the current track. Briefing will analyze the current week for drivers in your iRating range and give you an average lap you need to run in order to be competitive. This currently works for GT3 Fanatec Challenge Fixed and IMSA Fixed (GTP). More will follow.
![briefing](https://github.com/KaiRenz/SimCentral/assets/52081463/6024b997-a26c-4e0e-bbaf-8ac5840e09bf)


## FAQ

#### When I do the briefing the program freezes

Analyzing all the sessions can take some time. Chances are that the tool is still running in the background. Give it some time and you should see the output in the briefing area. 

#### When I enter my iRacing password, is it stored somewhere?

No, the password is not stored. Thats also the reason you have to enter it everytime you do a briefing run. The only thing stored in the config file (which is on your computer only) is your email address used for iRacing.

#### Where can I find the config file?

The config.ini file is store in your appdata. 

Example: *C:\Users\YOURUSER\AppData\Local\SimCentral\config.ini*


#### Where is the Windows installer?

There is no installer at the moment. There will be when the project is a bit further developed. 


#### Is there a roadmap for development?

No but if you have questions or ideas let me know! 


## Feedback

If you have any feedback or ideas, please reach out to me at [Twitter](https://twitter.com/kairenz1990).

