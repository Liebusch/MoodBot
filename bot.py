# bot.py
# Main code for bot

import playSong
import cfg_auth
import utils
import socket
import re
import thread
from time import sleep

def main():
    # Networking functions
    s = socket.socket()
    s.connect((cfg_auth.HOST, cfg_auth.PORT))
    s.send("PASS {}\r\n".format(cfg_auth.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg_auth.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg_auth.CHAN).encode("utf-8"))

    # Media Player Setup
    player = playSong.MediaPlayer()
    thread.start_new_thread(player.play_video, ())

    # Bot Setup
    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    utils.chat(s, "Hi everyone!")

    thread.start_new_thread(utils.threadFillOpList,())

    while True:
        try:
            response = s.recv(1024).decode("utf-8")
        except socket.error, e:
            print e
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)  # return the entire match
            message = CHAT_MSG.sub("", response)
            print(username + ": " + message)

            # Custom Commands
            if message.strip() == "!vote energy":
                player.mood="energy"
            if message.strip() == "!vote chill":
                player.mood="chill"

        sleep(1.5)




if __name__ == "__main__":
    main()
