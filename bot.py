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

class RetweetBot(object):
	# config
	config = {
			"me": "myownscreenname", # Your own screen name
			"hashtag": '#myhashtag1', # Any hashtag or magic word that triggers the retweet
			"additionalHashtags": ["tag1", "#tag2"], # At least one of the most be contained in the tweet. write "[]" for no additionalHashtags
			"sleep": 5, # Time betweet queries to Twitter
			"count": 100, # Amount of tweets per request (max 100)
			"nativeRetweet": True # If true, retweets natively. If false, retweets using "RT @user:" 
		}
	def __init__(self, ckey, csec, akey, asec):
		# API initialization
		# WARNING: Don't share these keys
		self.api = _twitter.Api (
			consumer_key = ckey,
			consumer_secret = csec,
			access_token_key = akey,
			access_token_secret = asec
		)
		
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

	def run(self):
		# loop
		lastid = None
		first = 1
		while 1:
			# get last tweets
			print "Getting tweets..."
			timeline = self.api.GetSearch(self.config["hashtag"], since_id = lastid, per_page = self.config["count"])
			
			# update last ID
			if len (timeline) > 0:
				lastid = timeline [0].id
				print "Last ID updated:", lastid
			
			# skip the first time
			if first > 0:
				first = 0
				continue
			
			# check tweets
			for status in timeline:

				# do not rt own tweets
				if status.user.screen_name.lower() == self.config["me"]:
					continue
				
				# has the hashtag?
				if status.text.lower ().find (self.config["hashtag"]) < 0:
					continue
				# has additional hashtag
				if len(self.confgi["additionalHashtags"]) > 0:
					send = False
					for ht in self.config["additionalHashtags"]:
						if status.text.lower().find(ht) >= 0:
							send = True

					if not send:
						continue
				if not self.additional_conditions(status):
					continue
				
				# let's retweet
				if self.config["nativeRetweet"]:
					print "Retweeting:", status.user.screen_name, status.text
					self.api.PostRetweet (status.id)
				else:
					retweet = 'RT @' + status.user.screen_name + ": " + status.text
					if len (retweet) > 140:
						retweet = retweet [:137] + "..."
					print "Tweeting:", retweet
					self.api.PostUpdate (retweet)

			# zZzZzZ
			time.sleep(self.config["sleep"])

def main():
	bot = RetweetBot("Consumer Key", "Consumer Secret", "Acces Token Key", "Access Token Secret")
	bot.run()

if __name__=="__main__":
	main()
