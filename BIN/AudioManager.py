import urllib2
import wget
import os
import shutil
import glob
import subprocess
from random import randint
def getMyVersionNumber():
	try:
		F=open("AudioVersion.txt","r")
		VersionNo=F.read()
		F.close()
		return VersionNo
	except IOError:
		print("error?")
		F=open("AudioVersion.txt","w")
		F.write("0.0")
		F.close()
		return 0.0
def getCurrentVersionNumber():
	response = urllib2.urlopen('https://raw.githubusercontent.com/marath007/AnimatedProject/master/AudioData/AudioList')
	for line in response.readlines():
		return line[1:]
def getMyHiVersionNumber():
	try:
		F=open("HiVersion.txt","r")
		VersionNo=F.read()
		F.close()
		return VersionNo
	except IOError:
		print("error?")
		F=open("HiVersion.txt","w")
		F.write("0.0")
		F.close()
		return 0.0
def getCurrentHiVersionNumber():
	response = urllib2.urlopen('https://raw.githubusercontent.com/marath007/AnimatedProject/master/HiSounds/HiVersion')
	for line in response.readlines():
		return line[1:]	    
def updateAudioContent():
	if float(getMyVersionNumber())<float(getCurrentVersionNumber()):
		print "request update"
		response = urllib2.urlopen('https://raw.githubusercontent.com/marath007/AnimatedProject/master/AudioData/AudioList')
		count=0
		for line in response.readlines():
			if count==0:
				count=count+1
			else:
				print (line)
				count=count+1
				url = 'https://raw.githubusercontent.com/marath007/AnimatedProject/master/AudioData/' + line[:-1] + '.wav'
				filename = "/home/pi/led_switch/AudioData/"+line[:-1] + '.wav'
				file = wget.download(url,out="/home/pi/led_switch/AudioData/"+line[:-1] + '.wav')
				if os.path.exists(filename):
    					shutil.move(file,filename)
				print (file)
		updateVersionNumber()
def updateHiAudioContent():
	if float(getMyHiVersionNumber())<float(getCurrentHiVersionNumber()):
		print "request update"
		response = urllib2.urlopen('https://raw.githubusercontent.com/marath007/AnimatedProject/master/HiSounds/HiVersion')
		count=0
		for line in response.readlines():
			if count==0:
				count=count+1
			else:
				print (line)
				count=count+1
				url = 'https://raw.githubusercontent.com/marath007/AnimatedProject/master/HiSounds/' + line[:-1]
				filename = "/home/pi/led_switch/HiSounds/"+line[:-1]
				file = wget.download(url,out="/home/pi/led_switch/HiSounds/"+line[:-1])
				if os.path.exists(filename):
    					shutil.move(file,filename)
				print (file)
		updateHiVersionNumber()
def updateVersionNumber():
	F=open("AudioVersion.txt","w")
	F.write(getCurrentVersionNumber())
	F.close()
def updateHiVersionNumber():
	F=open("HiVersion.txt","w")
	F.write(getCurrentHiVersionNumber())
	F.close()
def playConfirmSound():
	os.chdir("/home/pi/led_switch/HiSounds")
	fCount = 0
	for file in glob.glob("*.???"):
		fCount=fCount+1
	iPlay = randint(1, fCount)
	print (iPlay)
	fCount=0
	for file in glob.glob("*.???"):
		fCount=fCount+1
		if fCount==iPlay:
			bashCommand ="play " +  file
			process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			while True:
				if process.poll() is not None:
					break
			shutil.move(file,file+".xxm")
			break
	for file in glob.glob("*.x*"):
		print (file)
		shutil.move(file,file[:-2])
	os.chdir("/home/pi/led_switch")

def playRandomFile():
	os.chdir("/home/pi/led_switch/AudioData")
	fCount = 0
	for file in glob.glob("*.wav"):
		fCount=fCount+1
	iPlay = randint(1, fCount)
	print (iPlay)
	fCount=0
	for file in glob.glob("*.wav"):
		fCount=fCount+1
		if fCount==iPlay:
			bashCommand ="play " +  file
			process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			while True:
				if process.poll() is not None:
				#	print("audio playing")
				#else:
					break
			shutil.move(file,file+".xxmuted")
			break
	for file in glob.glob("*.x*"):
		print (file)
		shutil.move(file,file[:-2])
	os.chdir("/home/pi/led_switch")
if __name__ == "__main__":
	print("My version is " + str(getMyVersionNumber()))
	print("Current version is " + str(getCurrentVersionNumber()))
	updateAudioContent()
	playRandomFile()
