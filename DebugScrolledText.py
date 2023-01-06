import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import *
from enum import _EnumDict
import time

import customtkinter as ctk


class Tag(_EnumDict):
	"""Debug logger tags"""
	SUCCESS = "#5cb85c"
	WARNING = "#f8141b"
	ERROR = "#0facf4"


class DebugScrolledText(ScrolledText):
	def __init__(self, master=None, font="Arial 10", bg="white"):
		super().__init__(master)
		self["font"] = font
		self["bg"] = bg
		self["state"] = DISABLED
		
		self.tag_config(Tag.SUCCESS, foreground=Tag.SUCCESS)
		self.tag_config(Tag.WARNING, foreground=Tag.WARNING)
		self.tag_config(Tag.ERROR, foreground=Tag.ERROR)
	
	def _writeline(self, text="", subtext="", tag="", ico=""):
		self["state"] = NORMAL
		self.insert(END, f"[{time.strftime('%H:%M:%S')}]")
		if ico != "": self.insert(END, ico, tag)
		self.insert(END, f" {text}")
		if subtext != "":
			self.insert(END, f" [{subtext}]\n")
		else:
			self.insert(END, f"\n")
		self["state"] = DISABLED
	
	def log(self, text: str = "something", subtext: str = ""):
		self._writeline(text, subtext)
	
	def success(self, text: str = "success", subtext: str = ""):
		self._writeline(text, subtext, Tag.SUCCESS, " [o]")
	
	def warning(self, text: str = "warning", subtext: str = ""):
		self._writeline(text, subtext, Tag.WARNING, " [x]")


if __name__ == '__main__':
	debug = DebugScrolledText()
	debug.pack(side=TOP, fill=BOTH, expand=True)
	
	for i in range(40):
		debug.log()
		debug.success()
		debug.warning()
	
	debug.mainloop()
