#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# Copyright (c) 2013 Benjamin Leuckefeld, http://atroxlp.de
#

import bot
import os

config = {
		"me": "myownscreenname", # Your own screen name
		"hashtag": '#myhashtag1', # Any hashtag or magic word that triggers the retweet
		"additionalHashtags": ["tag1", "#tag2"], # At least one of the most be contained in the tweet. write "[]" for no additionalHashtags
		"blacklist": ["nsfw", "#porn"], # If one the these words is contained in the tweet, it won't retweet. write "[]" for no blacklist
		"blacklistusers": ["example"], # The bot ignores tweets by these users. USERNAMES WITHOUT @! write "[]" for no blacklistuser
		"sleep": 5, # Time betweet queries to Twitter
		"count": 100, # Amount of tweets per request (max 100)
		"nativeRetweet": True, # If true, retweets natively. If false, retweets using "RT @user:" 
		
		# Twitter API Config
		"Consumer_Key": "",
		"Consumer_Secret": "",
		"Acces_Token_Key": "",
		"Acces_Token_Secret": ""
	}
	
def get_conditions():
	def check_conditions(tweet):
		# is it a mention?
		if tweet.text.lower().startswith("@"):
			return False
			
		# is it a RT?
		if tweet.text.lower().startswith("rt"):
			return False

		# at least 3 words
		if len(tweet.text.split(" ")) < 3:
			return False			
		return True
	return check_conditions	

def main():
	rtbot = bot.RetweetBot()
	rtbot.run(
			config["me"],
			config["hashtag"],
			config["additionalHashtags"],
			config["blacklist"],
			config["blacklistusers"],
			config["sleep"],
			config["count"],
			config["nativeRetweet"],
			config["Consumer_Key"],
			config["Consumer_Secret"],
			config["Acces_Token_Key"],
			config["Acces_Token_Secret"],
			get_conditions(),
			os.path.join(os.path.dirname(__file__), ".".join(os.path.basename(__file__).split(".")[:-1])+".log")
			)

if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
