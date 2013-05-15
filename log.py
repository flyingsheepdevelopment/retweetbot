#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# Copyright (c) 2013 Benjamin Leuckefeld, http://atroxlp.de
#

from datetime import datetime
import os
import codecs

INFO=0
IMPORTANT=36
ERROR=42
QUIET=666

class Log(object):
	
	loglevel_file = INFO
	loglevel_console = IMPORTANT
	
	def __init__(self, filename):
		self.logfile = codecs.open(filename, "a+", "utf-8")
		
	def __del__(self):
		self.logfile.close()
		
	def setFileLogLevel(self, level):
		self.loglevel_file = level
		
	def setConsoleLogLevel(self, level):
		self.loglevel_console = level
		
	def info(self, text):
		msg = "[" + self.gettimestamp() + "] [INFO] " + text
		if self.loglevel_file <= INFO:
			self.logfile.write(msg+"\n")
		if self.loglevel_console <= INFO:
			print msg
		
	def important(self, text):
		msg = "[" + self.gettimestamp() + "] [IMPORTANT] " + text
		if self.loglevel_file <= IMPORTANT:
			self.logfile.write(msg +"\n")
		if self.loglevel_console <= IMPORTANT:
			print msg
		
	def error(self, text):
		msg = "[" + self.gettimestamp() + "] [ERROR] " + text
		if self.loglevel_file <= ERROR:
			self.logfile.write(msg +"\n")
		if self.loglevel_console <= ERROR:
			print msg
	
	def gettimestamp(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
