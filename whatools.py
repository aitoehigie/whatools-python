#!/usr/bin/env python

import requests
#I put this here to disable the insecureplatform warning for https requests
requests.packages.urllib3.disable_warnings()

class Whatools(object):
    BASE_URL = "https://api.wha.tools/v3"
    def __init__(self, key):
        self.key = key

    def login(self):
        payload = dict(key = self.key)
        return requests.get(Whatools.BASE_URL + "/login", params = payload).text

    def logout(self):
        payload = dict(key = self.key)
        return requests.get(Whatools.BASE_URL + "/logout", params = payload).text

    def getIncomingMessages(self, since, until):
        payload = dict(key = self.key, since = since, until = until)
        #To do

    def sendMessage(self, key, to, body):
        payload = dict(key = self.key, to = to, body = body)
        return requests.post(Whatools.BASE_URL + "/message", params = payload).text

    def sendVcard(self, key, to, name, src, honor = True):
        payload = dict(key = self.key, to = to, name = name, src = src, honor = honor)
        return requests.post(whatools.BASE_URL + "/vcard", params = payload).text

    def sendPicture(self, key, to, caption, attachment, honor = True):
        payload = dict(key = self.key, to = to, caption = caption, honor = honor)
        attachment = dict(attachment=open(attachment, "rb"))
        return requests.post(Whatools.BASE_URL + "/media/picture", params = payload, files=attachment).text






