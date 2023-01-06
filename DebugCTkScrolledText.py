from customtkinter import *
from enum import _EnumDict
import time

class Tag(_EnumDict):
	"""Debug logger tags"""
	SUCCESS = "#5cb85c"
	WARNING = "#f8141b"
	ERROR = "#0facf4"

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class DebugCTkScrolledText(CTkTextbox):
	def __init__(self, master=None, font=("Arial", 16), state=DISABLED):
		super().__init__(master)
		self.configure(font=font)
		self.configure(state=state)
		self.configure(wrap="word")
		
		self.tag_config(Tag.SUCCESS, foreground=Tag.SUCCESS)
		self.tag_config(Tag.WARNING, foreground=Tag.WARNING)
		self.tag_config(Tag.ERROR, foreground=Tag.ERROR)
	
	def _writeline(self, text="", subtext="", tag="", ico=""):
		self.configure(state=NORMAL)
		self.insert(END, f"[{time.strftime('%H:%M:%S')}]")
		if ico != "": self.insert(END, ico, tag)
		self.insert(END, f" {text}")
		if subtext != "":
			self.insert(END, f" [{subtext}]\n")
			print(f"[{time.strftime('%H:%M:%S')}{ico} {text} [{subtext}]")
		else:
			print(f"[{time.strftime('%H:%M:%S')}]{ico} {text}")
			self.insert(END, f"\n")
		self.configure(state=DISABLED)
	
	def log(self, text: str = "something", subtext: str = ""):
		self._writeline(text, subtext)
	
	def success(self, text: str = "success", subtext: str = ""):
		self._writeline(text, subtext, Tag.SUCCESS, " [o]")
	
	def warning(self, text: str = "warning", subtext: str = ""):
		self._writeline(text, subtext, Tag.WARNING, " [x]")


if __name__ == '__main__':
	debug = DebugCTkScrolledText()
	debug.pack(side=TOP, fill=BOTH, expand=True)
	
	for i in range(40):
		debug.log()
		debug.success()
		debug.warning()
	
	debug.mainloop()