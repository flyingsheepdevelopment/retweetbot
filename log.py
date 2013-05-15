#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# Copyright (c) 2013 Benjamin Leuckefeld, http://atroxlp.de
#

from datetime import datetime
import os

INFO=0
ERROR=42
QUIET=666

class Log(object):
<<<<<<< HEAD
	def __init__(self, filename):
		if not os.access(os.path.join(os.path.dirname(__self__), filename), W_OK):
			print "Log file does not exists. Creating one for you."
			f = file(filename, 'w')
			f.close()
			print "Logfile saved!"
		self.file = filename
	
	def info(self, text, notify):
		now = datetime.now()
		msg = str("[" + now.month + "/" + now.day + "/" + now.year + " " + now.hour + ":" + now.minute + ":" + now.second + "] [INFO] " + text)
		with open(file, "w") as my_file:
			my_file.write(msg)
		if notify:
			print msg
		
	def error(self, text, notify):
		now = datetime.now()
		msg = str("[" + now.month + "/" + now.day + "/" + now.year + " " + now.hour + ":" + now.minute + ":" + now.second + "] [ERROR] " + text)
		with open(file, "w") as my_file:
			my_file.write(msg)
		if notify:
			print msg
=======
	
	loglevel_file = INFO
	loglevel_console = ERROR
	
	def __init__(self, filename):
		self.logfile = open(filename, "a+")
		
	def __del__(self):
		self.logfile.close()
		
	def setFileLogLevel(self, level):
		self.loglevel_file = level
		
	def setConsoleLogLevel(self, level):
		self.loglevel_console = level
		
	def info(self, text):
		now = datetime.now()
		msg = "[" + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "] [INFO] " + text
		if self.loglevel_file <= INFO:
			self.logfile.write(msg+"\n")
		if self.loglevel_console <= INFO:
			print msg
		
	def error(self, text):
		now = datetime.now()
		msg = "[" + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "] [ERROR] " + text
		if self.loglevel_file <= ERROR:
			self.logfile.write(msg +"\n")
		if self.loglevel_console <= ERROR:
			print msg
>>>>>>> 740263c88b23250c1f16878fc4ad81bed9d157c9
