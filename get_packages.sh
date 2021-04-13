#!/bin/bash

# URL for instance of pip install shell script
url=https://bootstrap.pypa.io/get-pip.py

# formatting fun
function format_status() {

	echo "--------------------------------"
	
}

# checking stage installation status
function check_insta_status() {

	if [ $? -eq 0 ]; then
		format_status
		echo "Packet installation complete"
		format_status
	else
		format_status
		echo "Unknown error during installation. ABORTING!"
		format_status
		sleep 1
		exit 1
	fi
}

# attempt to download pip
function try_pip_from_url() {

	format_status
	# ommitting in REG WIN to run IE - RUN WITH ROOT PRIVS!
	Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Internet Explorer\Main" -Name "DisableFirstRunCustomize" -Value 2
	wget $url
	check_insta_status

}

# checking for pip status
echo "Checking for pip instance..."
pip --version
if [ $? -eq 0 ]; then
	format_status
    	echo "Pip is installed. Proceeding..."
	format_status
else
	format_status
    	echo "Pip not installed. Pip is required to run speechy! Trying to get via wget...!"
	format_status
	
	sleep 1
	try_pip_from_url
fi
sleep 5

# installing modules from reqs
echo "Installing from requirements..."

pip install -r requirements.txt

check_insta_status

echo "Installing pillow..."
pip install pillow

check_insta_status


echo "Installing pyttsx3..."
pip install pyttsx3

check_insta_status


echo "Installing SpeechRecognition..."
pip install SpeechRecognition

check_insta_status


echo "Installing pipwin..."
pip install pipwin

check_insta_status


echo "Installing pyaudio from pipwin..."
pipwin install pyaudio

check_insta_status
