#!/usr/bin/python3

import tkinter
import tkinter.ttk
import tkinter.messagebox
import string
import random

main_program = tkinter.Tk()
main_program.title('Password Generator')
main_program.resizable(0, 0)
main_program.geometry('640x360')

main_program.configure(bg='gray')

main_program.columnconfigure(index=0, weight=1)
main_program.columnconfigure(index=1, weight=1)
main_program.columnconfigure(index=2, weight=1)
main_program.columnconfigure(index=3, weight=1)
main_program.columnconfigure(index=4, weight=1)


def quit_window():

	main_program.destroy()

def activate_custom_entry():

	pass_custom_entry.configure(state=tkinter.NORMAL)

def deactivate_custom_entry():

	pass_custom_entry.configure(state=tkinter.DISABLED)

def reset_cmd():

	upper_char_val.set(0)
	lower_char_val.set(0)
	numeric_char_val.set(0)
	symbol_char_val.set(0)
	selected_pass_length.set(1)
	pass_custom_entry.configure(state=tkinter.NORMAL)
	pass_custom_entry.delete(0, tkinter.END)
	pass_custom_entry.configure(state=tkinter.DISABLED)
	generated_password_entry.configure(state=tkinter.NORMAL)
	generated_password_entry.delete(0, tkinter.END)
	generated_password_entry.configure(state='readonly')

def generate_password():

	generated_password_entry.configure(state=tkinter.NORMAL)
	generated_password_entry.delete(0, tkinter.END)
	generated_password_entry.configure(state='readonly')	

	upper_chosen = upper_char_val.get()
	lower_chosen = lower_char_val.get()
	numeric_chosen = numeric_char_val.get()
	symbol_chosen = symbol_char_val.get()

	upper_char_list = string.ascii_uppercase
	lower_char_list = string.ascii_lowercase
	numeric_char_list = string.digits
	symbol_char_list = string.punctuation

	if not upper_chosen and not lower_chosen and not numeric_chosen and not symbol_chosen:

		tkinter.messagebox.showwarning(title='Warning!', message='No charset selected!\nLowercase will be set as default!')
		lower_char_val.set(1)
		lower_chosen = lower_char_val.get()

	msg = ''
	custom_pass_chars = 0
	pw_length = 0

	if selected_pass_length.get() == 1:

		msg = 'Chose 8-12 chars\n'
		pw_length = random.randint(8, 12)
		msg += 'Random length is ' + str(pw_length)
		tkinter.messagebox.showinfo(title='Checkbox options status', message=msg)

	elif selected_pass_length.get() == 2:

		msg = 'Chose 13-16 chars\n'
		pw_length = random.randint(13, 16)
		msg += 'Random length is ' + str(pw_length)
		tkinter.messagebox.showinfo(title='Checkbox options status', message=msg)

	elif selected_pass_length.get() == 3:

		msg = 'Chose custom number of chars\n'
		try:
			custom_pass_chars = int(pass_custom_entry.get())
			if 4 <= custom_pass_chars <= 50:
				pw_length = custom_pass_chars
				msg += 'Random length is ' + str(pw_length)
				tkinter.messagebox.showinfo(title='Checkbox options status', message=msg)
			else:
				tkinter.messagebox.showerror(title='Error!', message='Number is not between 4 and 50!')
				pass_custom_entry.delete(0, tkinter.END)
		except:
			tkinter.messagebox.showerror(title='Error!', message='Not a numeric value!')
			pass_custom_entry.delete(0, tkinter.END)

	if 4 <= pw_length <= 50:

		pw_chars = []
		chars_valid_list = []

		if upper_chosen:
			chars_valid_list.append(upper_char_list)
			upper_index = random.randint(0, len(upper_char_list)-1)
			pw_chars.append(upper_char_list[upper_index])

		if lower_chosen:
			chars_valid_list.append(lower_char_list)
			lower_index = random.randint(0, len(lower_char_list)-1)
			pw_chars.append(lower_char_list[lower_index])

		if numeric_chosen:
			chars_valid_list.append(numeric_char_list)
			numeric_index = random.randint(0, len(numeric_char_list)-1)
			pw_chars.append(numeric_char_list[numeric_index])

		if symbol_chosen:
			chars_valid_list.append(symbol_char_list)
			symbol_index = random.randint(0, len(symbol_char_list)-1)
			pw_chars.append(symbol_char_list[symbol_index])

		full_char_str = ''.join(chars_valid_list)	

		for i in range(pw_length - len(pw_chars)):

			opt_elem_index = random.randint(0, len(full_char_str)-1)
			pw_chars.append(full_char_str[opt_elem_index])

		random.shuffle(pw_chars)
		final_password = ''.join(pw_chars)

		generated_password_entry.configure(state=tkinter.NORMAL)
		generated_password_entry.insert(0, final_password)
		generated_password_entry.configure(state='readonly')

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


chars_used_label = tkinter.ttk.Label(window_content, text='Password Chars:', font=('Calibri', 10),
										justify=tkinter.CENTER, background='red', foreground='black')
chars_used_label.grid(row=3, column=0, padx=5, pady=20, ipadx=2, ipady=2, sticky=tkinter.E)

upper_char_val = tkinter.IntVar()
lower_char_val = tkinter.IntVar()
lower_char_val.set(1)
numeric_char_val = tkinter.IntVar()
symbol_char_val = tkinter.IntVar()

upper_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use uppercase', onvalue=1, offvalue=0, variable=upper_char_val)
lower_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use lowercase', onvalue=1, offvalue=0, variable=lower_char_val)
numeric_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use numbers', onvalue=1, offvalue=0, variable=numeric_char_val)
symbol_char_checkbox = tkinter.ttk.Checkbutton(window_content, text='Use symbols', onvalue=1, offvalue=0, variable=symbol_char_val)

upper_char_checkbox.grid(row=3, column=1, padx=2, ipadx=2, ipady=2, sticky=tkinter.W)
lower_char_checkbox.grid(row=3, column=2, padx=2, ipadx=2, ipady=2, sticky=tkinter.W)
numeric_char_checkbox.grid(row=3, column=3, padx=2, ipadx=2, ipady=2, sticky=tkinter.W)
symbol_char_checkbox.grid(row=3, column=4, padx=2, ipadx=10, ipady=2, sticky=tkinter.W)

pass_length_label = tkinter.ttk.Label(window_content, text='Length -> 4 - 50:', font=('Calibri', 10),
										background='red', foreground='black')
pass_length_label.grid(row=4, column=0, ipadx=2, padx=5, sticky=tkinter.E)

selected_pass_length = tkinter.IntVar()

selected_pass_length.set(1)

pass_small_option = tkinter.ttk.Radiobutton(window_content, text='8-12 chars', value=1, variable=selected_pass_length, command=deactivate_custom_entry)
pass_medium_option = tkinter.ttk.Radiobutton(window_content, text='13-16 chars', value=2, variable=selected_pass_length, command=deactivate_custom_entry)
pass_custom_option = tkinter.ttk.Radiobutton(window_content, text='Custom no. :', value=3, variable=selected_pass_length, command=activate_custom_entry)

pass_small_option.grid(row=4, column=1, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)
pass_medium_option.grid(row=4, column=2, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)
pass_custom_option.grid(row=4, column=3, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)

pass_custom_entry = tkinter.Entry(window_content, width=5, state=tkinter.DISABLED)
#pass_custom_entry = tkinter.ttk.Entry(window_content, width=5, state=tkinter.DISABLED)
pass_custom_entry.grid(row=4, column=4, sticky=tkinter.W)

generated_password_entry = tkinter.ttk.Entry(window_content, state='readonly', justify=tkinter.CENTER,
											cursor='xterm', width=40)
generated_password_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=15)

reset_button = tkinter.ttk.Button(window_content, text='Reset', command=reset_cmd)
reset_button.grid(row=6, column=1, padx=10, pady=5)

generate_button = tkinter.ttk.Button(window_content, text='Generate', command=generate_password)
generate_button.grid(row=6, column=2, padx=10, pady=5)

quit_button = tkinter.ttk.Button(window_content, text='Quit', command=quit_window)
quit_button.grid(row=6, column=3, padx=10, pady=5)

main_program.mainloop()