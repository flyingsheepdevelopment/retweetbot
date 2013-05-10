#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# Copyright (c) 2013 Benjamin Leuckefeld, http://atroxlp.de
# Copyright (c) 2012 Juan C. Olivares <juancri@juancri.com>
# based on original code by Christian Palomares <palomares.c@gmail.com>
# 
# Distributed under the MIT/X11 license. Check LICENSE for details.
# 

import time
import _twitter
import bot

class MyBot(bot.RetweetBot):
	# config
	config = {
			"me": "myownscreenname", # Your own screen name
			"hashtag": '#myhashtag1', # Any hashtag or magic word that triggers the retweet
			"additionalHashtags": ["tag1", "#tag2"], # At least one of the most be contained in the tweet. write "[]" for no additionalHashtags
			"sleep": 5, # Time betweet queries to Twitter
			"count": 100, # Amount of tweets per request (max 100)
			"nativeRetweet": True, # If true, retweets natively. If false, retweets using "RT @user:" 
			
			# Twitter API Config
			"Consumer_Key": "",
			"Consumer_Secret": "",
			"Acces_Token_Key": "",
			"Acces_Token_Secret": ""
		}
		
	def additional_conditions(self, status):
		# is it a mention?
		if status.text.lower().startswith("@"):
			return False
			
		# is it a RT?
		if status.text.lower().startswith("rt"):
			return False

		# does not contain "nsfw"
		if status.text.lower().find("nsfw") > 0:
			return False

		# at least 3 words
		if len(status.text.split(" ")) < 3:
			return False
		return True

def main():
	bot = MyBot()
	bot.run()

if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
