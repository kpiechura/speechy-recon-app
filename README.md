# speechy-recon-app
Project targets into text-to-speech/voice recognition implementation for database of writers and their novels.
App is fetching data from JSON file, parsing them and then using `pyttsx3` voice engine to read aloud. 
User can also search database by reading aloud name and surname of the author. This functionality is possible due to `speech-recognition` module usage.

*NOTE*: from 0.6 version release, records added by user are now automatically proccessed with two stages:
* fetching image from Google of choosen writer
* fetching summary from wikipedia of choosen writer

## Requirements
* `Python` >= 3.3
* `Pip`
* `pyttsx3` module
* `PIL` module
* `wikipedia` module
* `simple img download` module
* more...

*Application is compatible on all OS platforms with required python packages.*

*NOTE*: To enlist full requirements, please see `requirements.txt` file and `get_version` shell script.

## Installation
Make sure you have all needed modules installed. In case you don't know, just type:


`$ pip install pyttsx3` / `$ pip install pillow` 

Or just simply call requirements to force pip to install all needed packages from file:

`$ pip install -r requirements.txt` and after that module for PIL - `$ pip install pillow`

## Shell script
You can also use `get_version` script to install proper packages. 

*NOTE*: Run script with root/admin privileges. Still in WIP state.

You can also just use PyCharm and manually download those from syntax guessing tool.

## T2S en-US package
If you are using Windows with polish language pack, please expect sloppy and weird pronunciation - text-to-speech module installation is based on provided language pack in system. Consider installing en-US Windows language pack from this Microsoft instruction: 
https://support.microsoft.com/en-us/windows/language-packs-for-windows-a5094319-a92d-18de-5b53-1cfc697cfca8
