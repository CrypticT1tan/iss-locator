# ISS LOCATOR 🛰️

Python program to locate the International Space Station with an interactive map.  
Inspired by Angela Yu's ISS Overhead Project.

![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Version](https://img.shields.io/badge/Version-2.0-blue)

--- 

## FEATURES 🌟
- Locates the International Space Station using coordinates converted to a physical address
- Interactivate map of the world with zoom features and markers for the ISS and a given position
- Sends desktop notifications of the ISS current location to the user whenever ISS is near/overhead the given position

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
pip install countryflag
```

When you are done with the installations, you can deactivate the virtual environment with this command:
```bash
deactivate
```
  
For MacOS, you will need to use Crontabs to set up the automation.  
For Windows, you will need to use the Task Scheduler instead.  

## CONTACT 📞
For any questions, contact me here on Github, at gavinkiosco@gmail.com via email, or cryptict1tan on Discord.

## ATTRIBUTION ©️
- ISS Current Location API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
- Geopy API: https://github.com/geopy/geopy
- Desktop Notifier: https://github.com/samschott/desktop-notifier
- Tkinter Map Viewer: https://github.com/TomSchimansky/TkinterMapView
