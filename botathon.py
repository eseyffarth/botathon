#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Esther'
import athon_config
import tweepy
import traceback
import time
import random
import simplejson as json

def login():
    # for info on the tweepy module, see http://tweepy.readthedocs.org/en/

    # Authentication is taken from athon_config.py
    consumer_key = athon_config.consumer_key
    consumer_secret = athon_config.consumer_secret
    access_token = athon_config.access_token
    access_token_secret = athon_config.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def stick_together_output():
    verbfile = open("verbs.json", "r", encoding="utf8")
    verbfile = verbfile.read()
    verbs = json.loads(verbfile)["verbs"]

    bases = set()

    for item in verbs:
        if " " not in item["present"].strip():
            bases.add(item["present"].strip().lower())

    sentences = ["I feel like my whole life up to now has been one single {}athon.",
                 "Are you up for a 24-hour {}athon?",
                 "The most relaxing thing to do after a hard day of work is a nice long {}athon.",
                 "Wow, did you see the neighbours' {}athon last night? Awkward!",
                 "Come to my party on Friday, it will be a total {}athon!",
                 "Listen, I can't join you, my family is having a huge {}athon this weekend.",
                 "Don't you agree that this show has become an absolute {}athon?",
                 "Why would anyone in their right mind participate in an obvious {}athon like that?",
                 "I'm not sure I'm up for your {}athon. I'd rather stay home.",
                 "Did you hear the news about tomorrow's {}athon?",
                 "Hey, what are you doing here? I thought you had an important {}athon planned.",
                 "Does anyone know how a real {}athon works? Is it dangerous?",
                 "Darling, did you remember to mail the invites for our {}athon? People have to prepare!",
                 "I feel like our entire relationship is basically just one {}athon.",
                 "Wanna join me for a quick {}athon? No strings attached!"]


    output = random.choice(sentences).format(random.sample(bases, 1)[0])
    return output

def tweet_something(debug):
    api = login()
    try:
        output = stick_together_output()
        if debug:
            print(output)
        else:
            api.update_status(status=output)
            print(output)
    except:
        error_msg = traceback.format_exc().split("\n", 1)[1][-130:]
        api.send_direct_message(screen_name = "ojahnn", text = error_msg + " " + time.strftime("%H:%M:%S"))

tweet_something(False)