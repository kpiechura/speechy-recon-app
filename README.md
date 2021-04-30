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

## User Guide
* To show bio and image for author, select right name from database list
* To request speechy to read bio aloud, click `Speech` button

![1](https://user-images.githubusercontent.com/56960469/116743484-4ab10c80-a9f9-11eb-9808-01262fa88781.gif)

* add new record to database with `Database` button
* type your author's name and sample bio
* image and bio should be fetched from web. In case of fetch failure from wikipedia, your sample bio will be displayed.

![2](https://user-images.githubusercontent.com/56960469/116743851-cc089f00-a9f9-11eb-8af2-fa1b5adc85a2.gif)

* restart application to see updated database records with your author's name

![3](https://user-images.githubusercontent.com/56960469/116743916-e3478c80-a9f9-11eb-9efd-99068b591092.gif)

* remove any record from database with `Remove` button in database instance window

![4](https://user-images.githubusercontent.com/56960469/116743963-f6f2f300-a9f9-11eb-8b1f-8dc42c7346cc.gif)

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
