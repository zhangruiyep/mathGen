import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk
import types
import threading
import time
import random

class filesTreeview(ttk.Treeview):
	def __init__(self, master=None):
		ttk.Treeview.__init__(self, master)
		self['columns']=("a", "arith", "b", "equ", "result")
		self['height'] = 20
		#self.filesdata = filesData()
		self.grid(sticky=tk.NSEW)
		self.createWidgets()

	def createWidgets(self):
		self.column("#0", width=20, stretch=0)
		self.column("a", width=30)
		self.column("arith", width=20)
		self.column("b", width=30)
		self.column("equ", width=20)
		self.column("result", width=40)



class Application(ttk.Frame):
	def __init__(self, master=None):
		ttk.Frame.__init__(self, master)
		#self.cfg = cfg.configFile()
		self.columnconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.grid(sticky=tk.NSEW)
		self.createWidgets()
		#self.dev = None

	def createWidgets(self):
		tv_frame = ttk.Frame(self)
		tv_frame.grid(row = 2, sticky=tk.NSEW, pady = 3)

		self.tv = filesTreeview(tv_frame)
		self.tv.grid(row = 0, sticky=tk.NSEW)
		#self.tv.fill_treeview()

		self.sb = ttk.Scrollbar(tv_frame, orient=tk.VERTICAL, command=self.tv.yview)
		self.sb.grid(row = 0, column=1, sticky=tk.NS)

		self.tv.configure(yscrollcommand=self.sb.set)

		actionFrame = ttk.Frame(self)
		actionFrame.grid(row = 4, sticky=tk.NSEW, pady=3)

		self.genBtn = ttk.Button(actionFrame, text="生成题目", command=self.genMath)
		self.genBtn.grid(padx=10, row = 0, column = 0)

		self.resultBtn = ttk.Button(actionFrame, text="计算结果", command=self.getResult)
		self.resultBtn.grid(padx=10, row = 0, column = 1)

		#self.saveCfgFileBtn = ttk.Button(actionFrame, text="Save Configuration", command=self.saveCfgFile)
		#self.saveCfgFileBtn.grid(padx=10, row = 0, column = 1)
	def genMath(self):
		for item in self.tv.get_children():
			self.tv.delete(item)

		for idx in range(1, 21):
			sumInt = random.randint(2,99)
			a = random.randint(1,sumInt-1)
			addSym = random.randint(1,2)
			#print(sumInt, a, addSym)
			if addSym == 1:
				arith = '+'
				b = sumInt - a
				result = sumInt
			else:
				arith = '-'
				b = a
				a = sumInt
				result = a - b
			
			self.tv.insert('',"end",values=(a,arith,b,'=',result))
				
		
		self.tv["displaycolumns"]=("a", "arith", "b", "equ")
		return
	
	def getResult(self):
		self.tv["displaycolumns"]=self.tv["columns"]
		return


app = Application()
app.master.title('GenMath')
app.master.rowconfigure(0, weight=1)
app.master.columnconfigure(0, weight=1)
app.mainloop()
