# ISS LOCATOR 🛰️

Python program to locate the International Space Station. Can be scripted to run at regular intervals.

![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Version](https://img.shields.io/badge/Version-1.0-blue)

--- 

## FEATURES 🌟
- Locates the International Space Station using coordinates converted to a physical address
- File is scriptable to run at customizable intervals on both Mac and Windows
- Sends desktop notifications of the ISS current location to the user whenever the script is run

## INSTALLATION ⚙️
Clone the repository while in your desired directory:
```bash
git clone https://github.com/CrypticT1tan/iss-locator.git
```
Navigate to the repository directory to begin using it.

Create and activate a virtual environment:
MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:
```bash
python -m venv venv
venv\Scripts\activate.bat
```

Use package manager pip to install the following:
```bash
pip install requests
pip install geopy
pip install desktop-notifier
```

When you are done with the installations, you can deactivate the virtual environment with this command:
```bash
deactivate
```

## USAGE 🔧

Create a script with these commands:

MacOS (script.sh):
```bash
cd <path_to_iss-locator>
source venv/bin/activate
python3 locator.py
deactivate
```

Windows (script.bat):
```bash
cd <path_to_iss-locator>
venv\Scripts\activate.bat
python locator.py
deactivate
```
  
Setting up the automation:

MacOS (crontabs):
```bash
crontab -e
```
Once inside, use the crontab.guru website to determine the command and enter it into the Vim for the task to be automated.  
Link: https://crontab.guru 

## CONTACT 📞
For any questions, contact me here on Github, at gavinkiosco@gmail.com via email, or cryptict1tan on Discord.

## ATTRIBUTION ©️
- ISS Locator API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
- Geopy API: https://github.com/geopy/geopy
- Desktop Notifier: https://github.com/samschott/desktop-notifier
- Crontab.Guru: https://crontab.guru 
