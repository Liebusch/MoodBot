# utils.py
# A bunch of utility functions

import cfg_auth
import urllib2, json
import time, thread
from time import sleep


# Function: chat
# Send a chat message to the server.
#   Parameters:
#       sock -- the socket over which to send the message
#       msg -- the message to send
def chat(sock, msg):
        sock.send("PRIVMSG {} :{}\r\n".format(cfg_auth.CHAN, msg))

# Function: threadFillOpList
# In a separate thread, fill up the op list
def threadFillOpList():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/" + cfg_auth.CHAN + "/chatters"
            req = urllib2.Request(url, headers={"accept": "*/*"})
            response = urllib2.urlopen(req).read()
            if response.find("502 Bad Gateway") == -1:
                cfg_auth.oplist.clear()
                data = json.loads(response)
                for p in data["chatters"]["moderators"]:
                    cfg_auth.oplist[p] = "mod"
        except:
            'do nothing'
        sleep(5)

def isOp(user):
    return user in cfg_auth.oplist