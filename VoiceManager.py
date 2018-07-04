#!/usr/bin/env python
from __future__ import print_function       #should be on the top
import threading
import time
import psutil
import myledprogFile
import urllib2
#import AudioManager
#bashCommand = "cd /home/pi/sdk-folder/sdk-build/SampleApp/src && ./SampleApp /home/pi/sdk-folder/sdk-build/Integration/AlexaClientSDKConfig.json /home/pi/sdk-folder/third-party/snowboy/resources/alexa ERROR"
bashCommandAlexa = "/home/pi/sdk-folder/sdk-build/SampleApp/src/./SampleApp /home/pi/sdk-folder/sdk-build/Integration/AlexaClientSDKConfig.json /home/pi/sdk-folder/third-party/snowboy/resources/alexa ERROR"
bashCommandGoogle = "bash /home/pi/google-assistant-init.sh"
import subprocess
#process = subprocess.Popen(["ls", "-l"])
class MyThread(threading.Thread):
	isRunning=True
	
	def run(self):
		print ("started!")              # "Thread-x started!"
		print (self.name)
		if self.name=="GOOGLE":
			self.process = subprocess.Popen(bashCommandGoogle.split(), stdout=subprocess.PIPE)
		else:
			self.process = subprocess.Popen(bashCommandAlexa.split(), stdout=subprocess.PIPE)                             # Pretend to work for a second
		#print (self.isRunning + " exist")
		while True:
			myledprogFile.setup()
			if self.name==myledprogFile.main():
				print (self.name + " is Active")
				myledprogFile.destroy()
			else:
				print (self.name + " is inactive")
				self.kill()
				myledprogFile.destroy()
				self.isRunning=False
				return 0
			#if process.poll() is  None:
			#	self.isRunning = True
			#	print ("Alexa True")
			#else:
			#	self.isRunning = False
			#	print ("Alexa False")
			#	return 0
			time.sleep(1)
	def kill(self):
		process = psutil.Process(self.process.pid)
		for proc in process.children(recursive=True):
			proc.kill()
		process.kill()
def LaunchVoiceService():
	myledprogFile.setup()
	res=myledprogFile.main()
	myledprogFile.destroy()
	print ("switch is at " + res)
	if res=="GOOGLE":
		mythread = MyThread(name = "GOOGLE")
	else:
		mythread = MyThread(name = "ALEXA")
	mythread.start()

	while True:
		if mythread.isRunning:
			print ("Voice is running")
		else:
			print ("Voice is dead")
			return 0
		time.sleep(1)
class MyUpdate(threading.Thread):
	def run(self):
		while True:
			#print("My version is " + str(AudioManager.getMyVersionNumber()))
			#print("Current version is " + str(AudioManager.getCurrentVersionNumber()))
			#AudioManager.updateAudioContent()
			#AudioManager.updateHiAudioContent()
			#AudioManager.playRandomFile()
			time.sleep(5)
def MainRoutine():
	#myupdate = MyUpdate(name = "Updater")
	#myupdate.start()
	while True:
		LaunchVoiceService()
		print("Return to Main")
		time.sleep(1)
if __name__ == '__main__':
	MainRoutine()
