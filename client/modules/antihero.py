# -*- coding: utf-8-*-
import requests
import re

WORDS = ["ANTI HERO", "ANTIHERO", "ANTI", "HERO", "AUNTIE", "ANTI-HERO"]

def handle(text, mic, profile):

    mic.say("Vending ANTIHERO")

    response = requests.post('http://4.35.101.62:2020/vendSlot/4')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bantihero\b|\bhero\b|\banti\b|\baunty\b|\bauntie\b|\banti-hero\b', text, re.IGNORECASE))
