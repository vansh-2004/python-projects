# importing all the required modules
import getpass
from pytube import *
import tkinter as tk
from functools import partial
from tkinter.ttk import *
from tkinter import *
import os


def yt(label_result,k):
	u=getpass.getuser()
	lk=(k.get())
	video = YouTube(lk)
	strea = video.streams.get_highest_resolution()
	strea.download(output_path='C:/Users/%s/Downloads'%u)
	result=video.title
	label_result.config(text="Downloaded: '%s' to C:/Users/{}/Downloads".format(u) % result)
	return

def audio(label_r,a):
	u=getpass.getuser()
	aulk=(a.get())
	l=YouTube(aulk)
	v=l.streams.filter(only_audio=True).first()
	out_file=v.download(output_path='C:/Users/%s/Downloads'%u)
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)
	result=v.title
	label_r.config(text="Downloaded: '%s' to C:/Users/{}/Downloads".format(u) % result)
	return



m = tk.Tk()

m.geometry("600x300")
m.title('Youtube to mp4')
tk.Label(m, text='Enter youtube link').pack()
l=tk.StringVar()
lr = tk.Label(m)
lr.pack()
link = tk.Entry(m, textvariable=l)
link.pack()
yt=partial(yt, lr, l)
audio=partial(audio, lr, l)


button = tk.Button(m, text='convert to mp4', width=25, command=yt )
button.pack()

b = tk.Button(m, text='convert to mp3', width=25, command=audio )
b.pack()



m.mainloop()