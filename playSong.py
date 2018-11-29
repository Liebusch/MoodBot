
import pafy
import vlc
from random import randint
from time import sleep

class MediaPlayer:
    # Create new VLC Instance
    instance = vlc.Instance()
    mood = "chill"
    oldMood = ""
    # Create a MediaPlayer with the default instance
    player = instance.media_player_new()
    chill = "https://www.youtube.com/playlist?list=PLJ2DFXwybJACJtqhHhIz7xI1w8cfQ2Kiw"
    energy = "https://www.youtube.com/playlist?list=PLkMRAPworbEelkUPJrQEF5pBTVgzNLxWG"

    playlist_chill = pafy.get_playlist(chill)
    playlist_energy = pafy.get_playlist(energy)

    def getURL(self):
        try:

            # Youtube Playlist link
            if self.mood == "energy":
                video = self.playlist_energy['items'][randint(0, len(self.playlist_energy['items']))]['pafy']
            elif self.mood == "chill":
                video = self.playlist_chill['items'][randint(0, len(self.playlist_chill['items']))]['pafy']

            # Best url for video at best settings
            best = video.getbest(preftype="webm")

            # Load the media file
            media = self.instance.media_new(best.url)

            # Add the media to the player
            self.player.set_media(media)
        except:
            self.getURL()

    def play_video(self):
        while True:
            if self.oldMood!=self.mood:
                self.getURL()

                self.player.play()

                self.oldMood=self.mood
                sleep(100)


