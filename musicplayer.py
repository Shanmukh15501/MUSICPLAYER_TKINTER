from tkinter.filedialog import *
import os
import pygame
root = Tk()
index=0
songs=[]
root["bg"] = "blue"
root.minsize(250,200)
def directory():
    folder=askdirectory()
    os.chdir(folder)
    for file in os.listdir(folder):
        if(file.endswith("mp3")):
            songs.append(file)
directory()
much=len(songs)
var = StringVar()
label = Label(root, textvariable= var,width=30,height=5,bd=5,bg="red")
label.pack()
labell=Label(root,text="VOLUME")
labell.pack(side=LEFT)
varr= Scale(root,from_=0, to=100)
varr.pack(side=LEFT)
def nextsong(event):
    global index
    global much
    index=index+1
    if(index==much):
        index=0
    pygame.mixer.music.load(songs[index]) 
    pygame.mixer.music.play()
    updatelabel()
def prevsong(event):
    global index
    index=index-1
    if(index==-1):
        index=0
    pygame.mixer.music.load(songs[index]) 
    pygame.mixer.music.play()
    updatelabel()
def stopsong(event): 
    pygame.mixer.music.stop()
    indexx=0
def pausesong(event):
    global indexx
    indexx=indexx+1
    if(indexx%2!=0):
         pygame.mixer.music.pause()
    else:
         pygame.mixer.music.unpause()
def vol(event):
    selection = varr.get()
    print(selection)
    pygame.mixer.music.set_volume(selection)
def updatelabel():
    global label
    global index
    var.set(songs[index])
    return label
pygame.mixer.init()
updatelabel()
pygame.mixer.music.load(songs[0]) 
pygame.mixer.music.play()
label=Label(root,text='MyMusicPlayer')
label.pack()
listbox = Listbox(root)
print(listbox)
listbox.pack()
i=-1
for items in songs:
    i=i+1
    listbox.insert(i,items)
    listbox['bg']="black"
    listbox['fg']='white'
print(songs)
nextbutton=Button(root,text='Next Song')
nextbutton.pack()
prevbutton=Button(root,text='Prev Song')
prevbutton.pack()
stopbutton=Button(root,text='Stop Song')
stopbutton.pack()
pausebutton=Button(root,text='Pause/Play Song')
pausebutton.pack()
Volumebutton = Button(root, text="Set Volume")
Volumebutton.pack()
nextbutton.bind("<Button-1>",nextsong)
stopbutton.bind("<Button-1>",stopsong)
prevbutton.bind("<Button-1>",prevsong)
pausebutton.bind("<Button-1>",pausesong)
Volumebutton.bind("<Button-1>",vol);
root.mainloop()
