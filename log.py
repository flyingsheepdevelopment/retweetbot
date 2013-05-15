#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# Copyright (c) 2013 Benjamin Leuckefeld, http://atroxlp.de
#

from datetime import datetime

class Log(object):
	def __init__(self, filename):
		if not os.access(os.path.join(os.path.dirname(__self__), filename), W_OK)
			print "Log file does not exists. Creating one for you."
			f = file(filename, 'w')
			f.close()
			print "Logfile saved!"
		self.file = filename
	
	def info(self, text, notify)
		now = datetime.now()
		msg = str("[" + now.month + "/" + now.day + "/" + now.year + " " + now.hour + ":" + now.minute + ":" + now.second + "] [INFO] " + text)
		with open(file, "w") as my_file:
			my_file.write(msg)
		if notify
			print msg
		
	def error(self, text, notify)
		now = datetime.now()
		msg = str("[" + now.month + "/" + now.day + "/" + now.year + " " + now.hour + ":" + now.minute + ":" + now.second + "] [ERROR] " + text)
		with open(file, "w") as my_file:
			my_file.write(msg)
		if notify
			print msg