#!/usr/bin/env python

import requests
import os
import time
import datetime


# Disable the insecureplatform warning for https requests
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

    def getIncomingMessages(self, key, since, until):
        #specify since and until date objects as 'DD/MM/YYYY'"
        since = time.mktime(datetime.datetime.strptime(since, "%d/%m/%Y").timetuple())
	until = time.mktime(datetime.datetime.strptime(until, "%d/%m/%Y").timetuple())
        payload = dict(key = self.key, since = since, until = until)
	return requests.get(Whatools.BASE_URL + "/message", params = payload).text

    def sendMessage(self, key, to, body, honor = True):
        payload = dict(key = self.key, to = to, body = body)
        return requests.post(Whatools.BASE_URL + "/message", params = payload).text

    def sendVcard(self, key, to, name, src, honor = True):
        payload = dict(key = self.key, to = to, name = name, src = src, honor = honor)
        return requests.post(whatools.BASE_URL + "/vcard", params = payload).text

    def sendPicture(self, key, to, caption, attachment, honor = True):
        payload = dict(key = self.key, to = to, caption = caption, honor = honor)
        attachment = dict(attachment=open(attachment, "rb"))
        return requests.post(Whatools.BASE_URL + "/media/picture", params = payload, files=attachment).text

    def getNickname(self):
        payload = dict(key = self.key)
        return requests.get(Whatools.BASE_URL + "/nickname", params = payload).text

    def setNickname(self, nickname):
        payload = dict(key = self.key, nickname = nickname)
        return requests.post(Whatools.BASE_URL + "/nickname", params = payload).text

    def deleteNickname(self):
        payload = dict(key = self.key, nickname = "")
        return requests.post(Whatools.BASE_URL + "/nickname", params = payload).text

    def getStatusMessage(self):
        payload = dict(key = self.key)
        return requests.get(Whatools.BASE_URL + "/status", params = payload).text

    def setStatusMessage(self, message):
        payload = dict(key = self.key, message = message)
        return requests.post(Whatools.BASE_URL + "/status", params = payload).text

    def deleteStatusMessage(self):
        payload = dict(key = self.key, message = "")
        return requests.post(Whatools.BASE_URL + "/status", params = payload).text

    def getAvatar(self, phone):
        payload = dict(key = self.key, pn = phone)
        r = requests.get(Whatools.BASE_URL + "/avatar", params = payload, stream = True)
        if r.status_code == 200:
            if not os.path.exists("./avatars"):
                os.makedirs("./avatars")
            with open("./avatars/%savatar.jpg" %phone,  "wb") as f:
                for chunk in r:
                    f.write(chunk)
        else:
            pass

    def setAvatar(self, src):
        payload = dict(key = self.key)
        src = dict(src=open(src, "rb"))
        return requests.post(Whatools.BASE_URL + "/avatar", params = payload, files = src).text










