#!/usr/bin/python3

import tkinter
import tkinter.ttk
import random

main_program = tkinter.Tk()
main_program.title('Password Generator')
main_program.resizable(0, 0)
#main_program.aspect(minNumer=16, minDenom=9, maxNumer=16, maxDenom=9)
main_program.geometry('640x360')

main_program.configure(bg='gray')

main_program.columnconfigure(index=0, weight=1)
main_program.columnconfigure(index=1, weight=1)
main_program.columnconfigure(index=2, weight=1)
main_program.columnconfigure(index=3, weight=1)
main_program.columnconfigure(index=4, weight=1)

window_content = tkinter.ttk.Frame(main_program).grid(row=0, column=0)

test_label = tkinter.ttk.Label(window_content, text='', font=('Calibri', 14), justify=tkinter.CENTER,
								background='gray')
test_label.grid(row=0, column=0, columnspan=5)

welcome_label = tkinter.ttk.Label(window_content, text=' Welcome! ', font=('Calibri', 14), justify=tkinter.CENTER,
									background='gray', foreground='black', relief='flat')
welcome_label.grid(row=1, column=0, columnspan=5)

main_msg_label = tkinter.ttk.Label(window_content, text=' Use this tool to generate a random password! ', font=('Calibri', 12), 
								justify=tkinter.CENTER, background='gray', foreground='black', relief='flat')
main_msg_label.grid(row=2, column=0, columnspan=5, pady=10)


chars_used_label = tkinter.ttk.Label(window_content, text='Password Characters:', font=('Calibri', 10),
										justify=tkinter.CENTER, background='red', foreground='black')
#chars_used_label.grid(row=3, column=0, padx=10, pady=20, ipadx=5, ipady=2)
chars_used_label.grid(row=3, column=0, padx=5, pady=20, ipadx=2, ipady=2)

upper_char_val = tkinter.IntVar()
lower_char_val = tkinter.IntVar()
numeric_char_val = tkinter.IntVar()
symbol_char_val = tkinter.IntVar()

upper_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use uppercase', onvalue=1, offvalue=0, variable=upper_char_val)
lower_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use lowercase', onvalue=1, offvalue=0, variable=lower_char_val)
numeric_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use numbers', onvalue=1, offvalue=0, variable=numeric_char_val)
symbol_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use symbols', onvalue=1, offvalue=0, variable=symbol_char_val)

upper_char_checkbox.grid(row=3, column=1, padx=2, ipadx=2, ipady=2)
lower_char_checkbox.grid(row=3, column=2, padx=2, ipadx=2, ipady=2)
numeric_char_checkbox.grid(row=3, column=3, padx=2, ipadx=2, ipady=2)
symbol_char_checkbox.grid(row=3, column=4, padx=2, ipadx=10, ipady=2)

pass_length_label = tkinter.ttk.Label(window_content, text='Password Length:', font=('Calibri', 10),
										background='red', foreground='black')
pass_length_label.grid(row=4, column=0, ipadx=2, padx=5, sticky=tkinter.E)

selected_pass_length = tkinter.StringVar()

pass_small_option = tkinter.ttk.Radiobutton(window_content, text='8-12 Chars', value=random.randint(0, 9), variable=selected_pass_length)
pass_medium_option = tkinter.ttk.Radiobutton(window_content, text='13-16 Chars', value=random.randint(9, 13), variable=selected_pass_length)
pass_custom_option = tkinter.ttk.Radiobutton(window_content, text='Specify No.', value=random.randint(13, 17), variable=selected_pass_length)

pass_small_option.grid(row=4, column=1, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)
pass_medium_option.grid(row=4, column=2, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)
pass_custom_option.grid(row=4, column=3, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)

pass_custom_entry = tkinter.ttk.Entry(window_content, width=5, state=tkinter.DISABLED)
pass_custom_entry.grid(row=4, column=4, sticky=tkinter.W)

#chars_used_frame = tkinter.ttk.LabelFrame(window_content, text="Password Character Options") #, width=360, height=120)
#chars_used_frame = tkinter.Frame(window_content) #, width=360, height=120)
#chars_used_frame.grid(row=0, column=0, columnspan=3)

#password_length_frame = tkinter.ttk.LabelFrame(window_content, text="Password Length Options") #, width=360, height=120)
#password_length_frame = tkinter.Frame(window_content) #, width=360, height=120)
#password_length_frame.grid(row=0, column=3, columnspan=3)

#upper_char_val = tkinter.IntVar()
#lower_char_val = tkinter.IntVar()
#numeric_char_val = tkinter.IntVar()
#symbol_char_val = tkinter.IntVar()

#upper_char_checkbox = tkinter.ttk.Checkbutton(chars_used_frame, text='Use uppercase', onvalue=1, offvalue=0, variable=upper_char_val)
#lower_char_checkbox = tkinter.ttk.Checkbutton(chars_used_frame, text='Use lowercase', onvalue=1, offvalue=0, variable=lower_char_val)
#numeric_char_checkbox = tkinter.ttk.Checkbutton(chars_used_frame, text='Use numbers', onvalue=1, offvalue=0, variable=numeric_char_val)
#symbol_char_checkbox = tkinter.ttk.Checkbutton(chars_used_frame, text='Use symbols', onvalue=1, offvalue=0, variable=symbol_char_val)

#upper_char_checkbox.grid(row=0, column=0, padx=25, pady=10)
#lower_char_checkbox.grid(row=1, column=0, padx=25, pady=10)
#numeric_char_checkbox.grid(row=0, column=1, padx=25, pady=10)
#symbol_char_checkbox.grid(row=1, column=1, padx=25, pady=10)


#selected_pass_length = tkinter.StringVar()

#pass_small = tkinter.ttk.Radiobutton(password_length_frame, text='0-8 Chars', value=random.randint(0, 9), variable=selected_pass_length)
#pass_medium = tkinter.ttk.Radiobutton(password_length_frame, text='9-12 Chars', value=random.randint(9, 13), variable=selected_pass_length)
#pass_big = tkinter.ttk.Radiobutton(password_length_frame, text='13-16 Chars', value=random.randint(13, 17), variable=selected_pass_length)
#pass_custom = tkinter.ttk.Radiobutton(password_length_frame, text='Custom Chars No.', value=random.randint(13, 17), variable=selected_pass_length)

#pass_small.grid(row=0, column=0, sticky=tkinter.W, padx=25, pady=10)
#pass_medium.grid(row=1, column=0, sticky=tkinter.W, padx=25, pady=10)
#pass_big.grid(row=0, column=1, sticky=tkinter.W, padx=25, pady=10)
#pass_custom.grid(row=1, column=1, sticky=tkinter.W, padx=25, pady=10)



main_program.mainloop()