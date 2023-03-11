import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
#PseudoRandomPicker

window = tk.Tk()
window.title('PRP')
window.configure(bg = '#282923')
window.geometry('900x700')
window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=1)


def initOptionsBar():
	frm_buttons = tk.Frame(window, relief = tk.RAISED, bd = 2, bg = '#282923')
	btn_open = tk.Button(frm_buttons, text="Open", relief = tk.FLAT, bg = '#42433e', fg = "white", command = openFile)
	btn_save = tk.Button(frm_buttons, text="Save", relief = tk.FLAT, bg = '#42433e', fg = "white", command = saveFile)
	btn_text = tk.Button(frm_buttons, text="Text", relief = tk.FLAT, bg = '#42433e', fg = "white", command = returnToTxtFile)
	btn_picker = tk.Button(frm_buttons, text="Picker", relief = tk.FLAT, bg = '#42433e', fg = "white", command = initiatePicker)
	btn_conclusion = tk.Button(frm_buttons, text="Conclusion", relief = tk.FLAT, bg = '#42433e', fg = "white", command = initiateConclusion)
	sprt_picker = ttk.Separator(frm_buttons,orient='horizontal')
	sprt_conclusion = ttk.Separator(frm_buttons,orient='horizontal')

	btn_open.grid(row = 0, column=0,sticky="ew", padx=5, pady=5)
	btn_save.grid(row = 1, column=0,sticky="ew", padx=5, pady=5)
	sprt_picker.grid(row = 2, column = 0)
	btn_text.grid(row = 3, column=0,sticky="ew", padx=5, pady=5)
	btn_picker.grid(row = 4, column=0,sticky="ew", padx=5, pady=5)
	sprt_conclusion.grid(row = 5, column = 0)
	btn_conclusion.grid(row = 6, column = 0, sticky = 'ew', padx = 5, pady = 5)

	frm_buttons.grid(row=0, column=0, sticky="nws")

def initTextBox():
	global txt_edit
	txt_edit = tk.Text(window, bg = '#42433e', fg = '#FFFFFF')

	txt_edit.grid(row=0, column=1, sticky="nsew")

def openFile():
	global txt_edit
	global text
	filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)
	if not filepath:
		return
	txt_edit.delete("1.0", tk.END)
	with open(filepath, mode="r", encoding="utf-8") as input_file:
		text = input_file.read()
		txt_edit.insert(tk.END, text)
	window.title(f"PRP - {filepath}")

def saveFile():
	filepath = asksaveasfilename(
		defaultextension=".txt",
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
	)
	if not filepath:
		return
	with open(filepath, mode="w", encoding="utf-8") as output_file:
		text = txt_edit.get("1.0", tk.END)
		output_file.write(text)
	window.title(f"PRP - {filepath}")

def returnToTxtFile():
	global txt_edit
	global text
	global frm_picker
	global lbl_text_remained
	global lbl_text1
	global lbl_text2
	global btn_chose1
	global btn_chose2

	frm_picker.destroy()
	lbl_text_remained.destroy()
	lbl_text1.destroy()
	lbl_text2.destroy()
	btn_chose1.destroy()
	btn_chose2.destroy()

	txt_edit = tk.Text(window, bg = '#42433e', fg = '#FFFFFF')

	txt_edit.grid(row=0, column=1, sticky="nsew")

	txt_edit.insert(tk.END, text)	

def initiatePicker():
	global titles
	global indexes
	global txt_edit
	global frm_picker
	global lbl_text_remained
	global lbl_text1
	global lbl_text2
	global btn_chose1
	global btn_chose2

	if txt_edit != '':
		titles = textFileDestructor()
		
	indexes = randomPicker()

	remained_var = StringVar()
	text1_var = StringVar()
	text2_var = StringVar()


	frm_picker = tk.Frame(window, bg = '#282923')
	lbl_text_remained = tk.Label(frm_picker,fg = 'white', bg = '#282923', textvariable = remained_var)
	lbl_text1 = tk.Label(frm_picker, fg = 'white', bg = '#282923', font="Bold",textvariable = text1_var)
	lbl_text2 = tk.Label(frm_picker, fg = 'white', bg = '#282923', font="Bold",textvariable = text2_var)
	btn_chose1 = tk.Button(frm_picker, text = 'Chose', relief = tk.FLAT, command = pickerSelectFirst)
	btn_chose2 = tk.Button(frm_picker, text = 'Chose', relief = tk.FLAT, command = pickerSelectSecond)

	remained_var.set(f'remained: {len(titles)}')
	text1_var.set(titles[indexes[0]])
	text2_var.set(titles[indexes[1]])

	frm_picker.grid(row = 0, column = 1, sticky = 'news')
	lbl_text_remained.grid(row = 0, column = 0, sticky = 'we')
	lbl_text1.grid(row = 1, column = 0, sticky = 'ew', pady = (window.winfo_height()/2.7, window.winfo_height()/8), padx = window.winfo_width()/5.5)
	lbl_text2.grid(row = 1, column = 1, sticky = 'ew', pady = (window.winfo_height()/2.7, window.winfo_height()/8), padx = window.winfo_width()/5.5)
	btn_chose1.grid(row = 2, column = 0, sticky = 'ew', padx = 20)
	btn_chose2.grid(row = 2, column = 1, sticky = 'ew', padx = 20)

def initiateConclusion():
	global titles
	pickerDestructor()

	conclusionText_var = StringVar()

	lbl_conclusion = tk.Label(window, fg = 'white', bg = '#282923', font="Bold", textvariable = conclusionText_var)

	conclusionText_var.set(f'Has ben choosen: {titles[0]}')

	lbl_conclusion.grid(row = 0, column = 1, sticky = 'nsew')

def textFileDestructor():
	global text
	global txt_edit

	text = txt_edit.get("1.0", tk.END)
	titles = text.split("\n")

	for i in range(len(titles)):
		if titles[i] == '':
			titles.pop(i)

	text = "\n".join(titles)

	txt_edit.destroy()
	return titles

def pickerDestructor():
	global frm_picker
	global lbl_text_remained
	global lbl_text1
	global lbl_text2
	global btn_chose1
	global btn_chose2

	frm_picker.destroy()

def randomPicker():
	global titles
	if len(titles) == 1:
		initiateConclusion()
	elif len(titles) == 2:
		firstIndex = 0
		secondIndex = 1
	else:
		firstIndex = random.randint(0, len(titles)-1)
		secondIndex = random.randint(0, len(titles)-1)

	return [firstIndex, secondIndex]

def pickerSelectFirst():
	global text
	global titles
	global indexes
	global frm_picker
	global lbl_text_remained
	global lbl_text1
	global lbl_text2

	remained_var = StringVar()
	text1_var = StringVar()
	text2_var = StringVar()

	titles.pop(indexes[1])
	text = "\n".join(titles)


	lbl_text_remained.destroy()
	lbl_text1.destroy()
	lbl_text2.destroy()

	lbl_text_remained = tk.Label(frm_picker,fg = 'white', bg = '#282923', textvariable = remained_var)
	lbl_text1 = tk.Label(frm_picker, fg = 'white', bg = '#282923', font="Bold",textvariable = text1_var)
	lbl_text2 = tk.Label(frm_picker, fg = 'white', bg = '#282923', font="Bold",textvariable = text2_var)

	indexes = randomPicker()
	if indexes[0] == [1]:
		indexes = randomPicker()

	remained_var.set(f'remained: {len(titles)}')
	text1_var.set(titles[indexes[0]])
	text2_var.set(titles[indexes[1]])

	lbl_text_remained.grid(row = 0, column = 0, sticky = 'we')
	lbl_text1.grid(row = 1, column = 0, sticky = 'ew', pady = (window.winfo_height()/2.7, window.winfo_height()/8), padx = window.winfo_width()/5.5)
	lbl_text2.grid(row = 1, column = 1, sticky = 'ew', pady = (window.winfo_height()/2.7, window.winfo_height()/8), padx = window.winfo_width()/5.5)

	


def pickerSelectSecond():
	global text
	global titles
	global indexes
	global frm_picker
	global lbl_text_remained
	global lbl_text1
	global lbl_text2

	remained_var = StringVar()
	text1_var = StringVar()
	text2_var = StringVar()

	titles.pop(indexes[0])
	text = "\n".join(titles)


	lbl_text_remained.destroy()
	lbl_text1.destroy()
	lbl_text2.destroy()

	lbl_text_remained = tk.Label(frm_picker,fg = 'white', bg = '#282923', textvariable = remained_var)
	lbl_text1 = tk.Label(frm_picker, fg = 'white', bg = '#282923', font="Bold",textvariable = text1_var)
	lbl_text2 = tk.Label(frm_picker, fg = 'white', bg = '#282923', font="Bold",textvariable = text2_var)

	indexes = randomPicker()
	if indexes[0] == [1]:
		indexes = randomPicker()

	remained_var.set(f'remained: {len(titles)}')
	text1_var.set(titles[indexes[0]])
	text2_var.set(titles[indexes[1]])

	lbl_text_remained.grid(row = 0, column = 0, sticky = 'we')
	lbl_text1.grid(row = 1, column = 0, sticky = 'ew', pady = (window.winfo_height()/2.7, window.winfo_height()/8), padx = window.winfo_width()/5.5)
	lbl_text2.grid(row = 1, column = 1, sticky = 'ew', pady = (window.winfo_height()/2.7, window.winfo_height()/8), padx = window.winfo_width()/5.5)


initOptionsBar()
initTextBox()

window.mainloop()