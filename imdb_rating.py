__author__ = 'siddiqui'
import urllib


import json
import Tkinter
import tkMessageBox
import sys
import os

from os.path import basename
for arg in sys.argv:
    name = basename(os.path.splitext(arg)[0])



replace = [".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}"
    "x264","x265","720p","StyLishSaLH (StyLish Release)","DvDScr","MP3","HDRip","WebRip",
    "ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio","EngHindiIndonesian",
    "385MB","CooL GuY","a2zRG","x264","Hindi","AAC","PSK","CyBorG","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
    "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE",
    "BRRIP","XVID","AbSurdiTy","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
    "Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
    "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com",
    "1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
    "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
    "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
    "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
    "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
    "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
    "Exclusive","171","DiDee","v2","WEB","DL"

    ]

for value in replace:
        name = name.replace(value," ")

for y in range(1900,2015):
        if str(y) in name:
            name = name.replace(str(y)," ")

url = "http://www.omdbapi.com/?t="+name+"&tomatoes=true"
response = urllib.urlopen(url).read()
jsonvalues = json.loads(response)
title  = jsonvalues["Title"]
rating = jsonvalues["imdbRating"]
genre = jsonvalues["Genre"]
year = jsonvalues["Year"]
Actors = jsonvalues["Actors"]
Runtime = jsonvalues["Runtime"]
rotten = jsonvalues["tomatoRating"]


window = Tkinter.Tk()
window.wm_withdraw()



#centre screen message
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title= title, message="IMDb Rating = " + rating + "\n" +"Genre = " + genre + "\n" + "Year = " + year + "\n" + "Actors = " + Actors + "\n" + "Runtime = " + Runtime + "\n" + "Rotten Tomatoes user rating = " + rotten)
