import platform
from customtkinter import *

# ************************
# Scrollable Frame Class
# ************************

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class CTkScrollFrame(CTkFrame):
	"""All widgets add to {CTkScrollFrame}.viewPort"""
	def __init__(self, master):
		super().__init__(master)
		self.canvas = CTkCanvas(self, borderwidth=0, highlightthickness=0)
		bgc = master.cget("fg_color")
		
		self.canvas.configure(bg=bgc[1 if get_appearance_mode() == "Dark" else 0] if type(bgc) == list else bgc)
		
		self.viewPort = CTkFrame(self.canvas, fg_color=bgc, height=int(self.canvas.cget("height"))) # place a frame on the canvas, this frame will hold the child widgets
		self.vsb = CTkScrollbar(self, orientation=VERTICAL, command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		
		self.vsb.pack(side=RIGHT, fill=Y)
		self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
		self.canvas_window = self.canvas.create_window((4, 4), window=self.viewPort, anchor=NW, tags="self.viewPort")
		
		self.viewPort.bind("<Configure>", self.onFrameConfigure)
		self.canvas.bind("<Configure>", self.onCanvasConfigure)
		
		self.viewPort.bind('<Enter>', self.onEnter)
		self.viewPort.bind('<Leave>', self.onLeave)
		
		self.onFrameConfigure(None)
	
	def onFrameConfigure(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
	
	def onCanvasConfigure(self, event):
		canvas_width = event.width
		self.canvas.itemconfig(self.canvas_window, width=canvas_width)
	
	def onMouseWheel(self, event):
		if platform.system() == 'Windows':
			self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
		elif platform.system() == 'Darwin':
			self.canvas.yview_scroll(int(- 1 * event.delta), "units")
		else:
			if event.num == 4:
				self.canvas.yview_scroll(-1, "units")
			elif event.num == 5:
				self.canvas.yview_scroll(1, "units")
	
	def onEnter(self, event):
		if platform.system() == 'Linux':
			self.canvas.bind_all("<Button-4>", self.onMouseWheel)
			self.canvas.bind_all("<Button-5>", self.onMouseWheel)
		else:
			self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)
	
	def onLeave(self, event):
		if platform.system() == 'Linux':
			self.canvas.unbind_all("<Button-4>")
			self.canvas.unbind_all("<Button-5>")
		else:
			self.canvas.unbind_all("<MouseWheel>")


if __name__ == "__main__":
	root=CTk()
	scrollFrame = CTkScrollFrame(root)
	scrollFrame.pack(side="top", fill="both", expand=True)
	
	for row in range(100):
		
		# VERY IMPORTANT place it on viewPort, not just scrollFrame
		CTkLabel(scrollFrame.viewPort, text=str(row), width=3).grid(row=row, column=0)
		CTkButton(scrollFrame.viewPort, text=f"second column of row {row}").grid(row=row, column=1)
	root.mainloop()
