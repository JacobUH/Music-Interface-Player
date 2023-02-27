from tkinter import Tk, Listbox, Frame, Button, PhotoImage, Menu, filedialog, END
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("500x300")

pygame.mixer.init()

menuBar = Menu(root)
root.config(menu = menuBar)

songs =[]
currentSong = ""
paused = False

def loadMusic():
  global currentSong
  root.filenames = filedialog.askopenfilenames(initialdir="/home/runner/Music-Player", title="Select file",
                                                  filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
  for filename in root.filenames:
    name, ext = os.path.splitext(filename)
    if ext == '.mp3':
      songs.append(filename)
      songlist.insert("end", os.path.basename(filename))
  songlist.selection_set(0)
  currentSong = songs[songlist.curselection()[0]]

def playMusic():
  global currentSong, paused

  if not paused:
      pygame.mixer.music.load(currentSong)
      pygame.mixer.music.set_volume(100)
      pygame.mixer.music.play()
  else:
    pygame.mixer.music.unpause()
    paused = False
  
def pauseMusic():
  global paused
  pygame.mixer.music.pause()
  paused = True
  
def nextMusic():
  global currentSong, paused

  try:
    songlist.selection_clear(0, END) #check
    songlist.selection_set(songs.index(currentSong) + 1)
    currentSong = songs[songlist.curselection()[0]]
    playMusic()
  except:
    pass

def previousMusic():
  global currentSong, paused

  try:
    songlist.selection_clear(0, END)
    songlist.selection_set(songs.index(currentSong) - 1)
    currentSong = songs[songlist.curselection()[0]]
    playMusic
  except:
    pass

organizeMenu = Menu(menuBar, tearoff=False)
organizeMenu.add_command(label = 'Select Folder', command = loadMusic)
menuBar.add_cascade(label = 'Organize', menu = organizeMenu)

songlist = Listbox(root, bg = "black", fg = "white", width = 100, height = 15)
songlist.pack()

playButtonImage = PhotoImage(file='images/Play.png').subsample(12, 12)
pauseButtonImage = PhotoImage(file='images/Pause.png').subsample(12, 12)
nextButtonImage = PhotoImage(file='images/Next.png').subsample(12, 12)
previousButtonImage = PhotoImage(file='images/Previous.png').subsample(12, 12)

controlFrame = Frame(root)
controlFrame.pack()

playButton = Button(controlFrame, image = playButtonImage, borderwidth=0, command = playMusic)
pauseButton = Button(controlFrame, image = pauseButtonImage, borderwidth=0, command = pauseMusic)
nextButton = Button(controlFrame, image = nextButtonImage, borderwidth=0, command = nextMusic)
previousButton = Button(controlFrame, image = previousButtonImage, borderwidth=0, command = previousMusic)

previousButton.grid(row=0,column=0,padx=7,pady=10)
pauseButton.grid(row=0,column=1,padx=7,pady=10)
playButton.grid(row=0,column=2,padx=7,pady=10)
nextButton.grid(row=0,column=3,padx=7,pady=10)


#This start the loop of music
root.mainloop()