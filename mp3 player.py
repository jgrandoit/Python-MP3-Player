import pygame
import tkinter as tkr
import os

#create window
mp3 = tkr.Tk()
#fix window
mp3.title("Audio Player")
mp3.geometry("340x340")

#pygame
pygame.init()
pygame.mixer.init()


#action event
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLvl.get())

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def Unpause():
    pygame.mixer.music.unpause()
#buttons
Button1 = tkr.Button(mp3, width=5, height=3, text="PLAY", command=Play)
Button2 = tkr.Button(mp3, width=5, height=3, text="STOP", command=ExitPlayer)
Button3 = tkr.Button(mp3, width=5, height=3, text="PAUSE", command=Pause)
Button4 = tkr.Button(mp3, width=5, height=3, text="UNPAUSE", command=Unpause)
#playlistregistar
os.chdir("Anime Playlist")
songlist = os.listdir()

#Volume Level
VolumeLvl = tkr.Scale(mp3,from_=0.0, to_=1.0, orient = tkr.HORIZONTAL,resolution =0.1)



#Playlist Input
playlist = tkr.Listbox(mp3, highlightcolor="blue", selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    postion = 0
    playlist.insert(postion, item)
    postion = postion + 1


#song name
var = tkr.StringVar()
songtitle = tkr.Label(mp3, textvariable=var)
var.set((playlist.get(tkr.ACTIVE)))

#Place Widget
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
VolumeLvl.pack(fill="x")
playlist.pack(fill="both", expand="yes")
#active
mp3.mainloop()