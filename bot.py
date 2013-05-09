#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# Copyright (c) 2012 Juan C. Olivares <juancri@juancri.com>
# based on original code by Christian Palomares <palomares.c@gmail.com>
# 
# Distributed under the MIT/X11 license. Check LICENSE for details.
# 

import time
import twitter

# config
me = "myownscreenname" # Your own screen name
hashtag = '#myhashtag1' # Any hashtag or magic word that triggers the retweet
sleep = 5 # Time betweet queries to Twitter
count = 100 # Amount of tweets per request (max 100)
nativeRetweet = True # If true, retweets natively. If false, retweets using "RT @user:" 

# API initialization
# WARNING: Don't share these keys
api = twitter.Api (
	consumer_key = '',
	consumer_secret = '',
	access_token_key = '',
	access_token_secret = '')

# loop
lastid = None
first = 1
while 1:
	# get last tweets
	print "Getting tweets..."
	timeline = api.GetSearch(hashtag, since_id = lastid, per_page = count)
	
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
		if status.user.screen_name.lower() == me:
			continue
		
		# has the hashtag?
		if status.text.lower ().find (hashtag) < 0:
			continue
		
		# is it a mention?
		if status.text.lower().startswith("@"):
			continue
			
		# is it a RT?
		if status.text.lower().startswith("RT"):
			continue

		# does not contain "nsfw"
		if status.text.lower().find("nsfw") > 0:
			continue

		# at least 3 words
		if len(status.text.split(" ")) < 3:
			continue
		
		# let's retweet
		if nativeRetweet:
			print "Retweeting:", status.user.screen_name, status.text
			api.PostRetweet (status.id)
		else:
			retweet = 'RT @' + status.user.screen_name + ": " + status.text
			if len (retweet) > 140:
				retweet = retweet [:137] + "..."
			print "Tweeting:", retweet
			api.PostUpdate (retweet)

	# zZzZzZ
	time.sleep(sleep)
