# HebrewScheduler   
HebrewScheduler is a python module for creating 
Google Calendar's recurrent events by Hebrew (Jewish) date.  

# Setup
For run the program, you must first enable the Google API in your account [here](https://developers.google.com/calendar/quickstart/js)  

In the link, you'll see these buttons:  
![Google Calendar' API](https://github.com/gilbd/HebrewScheduler/blob/master/images/google%20calendar%20api%201.png)  

Click on **"Enable the Google Calendar API"** and the next window will open:  
![Enter new project name](https://github.com/gilbd/HebrewScheduler/blob/master/images/google%20calendar%20api%202.png)  

Insert *HebrewScheduler* (or any other name) and click **"NEXT"**.  
Hooray! Your'e all set!
![You're all set](https://github.com/gilbd/HebrewScheduler/blob/master/images/google%20calendar%20api%203.png)  

Click on **"Download Client configuration"**. The configuration file will download.  
Save the 'credentials.json' file in the project's folder (keep is name!) and you're ready to go!


# Run the program
After you got the 'credentials.json' file, `cd` to the project's folder.  
You can see the usage by `python initiator.py -h`:
```shell script
usage: initiator.py [-h] [--date DATE] [--number-years [1-50]]
                    [--event-name EVENT_NAME] [--event-desc EVENT_DESC]
                    [--event-loc EVENT_LOC] [--delete] [--gui-mode]
                    [--color [1-11]]

optional arguments:
  -h, --help            show this help message and exit
  --date DATE, -d DATE  Desired Gregorian date in the following format: YYYY-
                        MM-DD Default: today
  --number-years [1-50], -n [1-50]
                        Number of years for further calculation
  --event-name EVENT_NAME, -e EVENT_NAME
                        The created event's name
  --event-desc EVENT_DESC, -de EVENT_DESC
                        The created event's description
  --event-loc EVENT_LOC, -l EVENT_LOC
                        The created event's location
  --delete, -del        if you want to delete the event
  --gui-mode, -g        If this flag set up - use the GUI
  --color [1-11], -c [1-11]
                        The Event's color code from the following map: 1
                        Lavender 2 Sage 3 Grape 4 Flamingo 5 Banana 6
                        Tangerine 7 Peacock 8 Graphite 9 Blueberry 10 Basil 11
                        Tomato
```  

The GUI looks like this:  
![GUI](https://github.com/gilbd/HebrewScheduler/blob/master/images/HebrewSchedular%201.png)  
Yeah, I know, it look really lame, but its my first python-GUI app, so I just wanted to learn the tkinter usage.  

After insert the date to the textboxes and the color picking (color picking and Number of year insertions are mandatory)  
you may click on the Calendar button, and the calendar will open:
![GUI Calendar](https://github.com/gilbd/HebrewScheduler/blob/master/images/HebrewSchedular%202.png)  
pick the date corresponding the hebrew date you want to set:  
For example: If you want to set the date of *"Yom Kippur"* (י' תשרי), 
you may pick the Gregorian date `2020-09-28`, which is the corresponding date on 2020 (תשפ"א).  
Note: the "Number of years" will count from the 
picked date (i.e. if `Number of years = 1` and the picked date is `2020-09-28` so only *Yom Kippur* of תשפ"א will set).  

After run the program, you should see on the screen all the dates (Gregorian) which have set.  
