#!/usr/bin/python3

import tkinter
import tkinter.ttk
import tkinter.messagebox
import string
import random
import config


def create_main_program():

	main_program = tkinter.Tk()
	main_program.title(config.mw_title)
	main_program.resizable(0, 0)

	mw_width = config.mw_width
	mw_height = config.mw_height
	screen_width = main_program.winfo_screenwidth()
	screen_height = main_program.winfo_screenheight()
	x_lc = (screen_width//2) - (mw_width//2)
	y_lc = (screen_height//2) - (mw_height//2)

	main_program.geometry("{}x{}+{}+{}".format(mw_width, mw_height, x_lc, y_lc))
	main_program.configure(bg=config.mw_bgcolor)

	main_program.columnconfigure(index=0, weight=1)
	main_program.columnconfigure(index=1, weight=1)
	main_program.columnconfigure(index=2, weight=1)
	main_program.columnconfigure(index=3, weight=1)
	main_program.columnconfigure(index=4, weight=1)

	return main_program

def create_window_content():

	window_content = tkinter.ttk.Frame(main_program).grid(row=0, column=0)

	return window_content

def create_main_labels():

	test_label = tkinter.ttk.Label(window_content, text=config.tst_lbl_text, 
					font=config.tst_lbl_font, justify=tkinter.CENTER, 
					background=config.main_lbl_bgcol)
	test_label.grid(row=0, column=0, columnspan=5)

	welcome_label = tkinter.ttk.Label(window_content, text=config.wlc_lbl_text, 
					font=config.wlc_lbl_font, justify=tkinter.CENTER, background=config.main_lbl_bgcol, 
					foreground=config.main_lbl_fgcol, relief=config.main_lbl_rlf)
	welcome_label.grid(row=1, column=0, columnspan=5)

	main_msg_label = tkinter.ttk.Label(window_content, text=config.msg_lbl_text, 
						font=config.msg_lbl_font, justify=tkinter.CENTER, background=config.main_lbl_bgcol, 
						foreground=config.main_lbl_fgcol, relief=config.main_lbl_rlf)
	main_msg_label.grid(row=2, column=0, columnspan=5, pady=10)

	return test_label, welcome_label, main_msg_label

def create_ckb_vars():

	upper_char_val = tkinter.IntVar()
	lower_char_val = tkinter.IntVar()
	lower_char_val.set(1)
	numeric_char_val = tkinter.IntVar()
	symbol_char_val = tkinter.IntVar()

	return upper_char_val, lower_char_val, numeric_char_val, symbol_char_val

def create_rdb_vars():

	selected_pass_length = tkinter.IntVar()
	selected_pass_length.set(1)

	return selected_pass_length

def create_util_labels():

	chars_used_label = tkinter.ttk.Label(window_content, text=config.chrs_lbl_text, 
						font=config.chrs_lbl_font, justify=tkinter.CENTER, 
						background=config.chrs_lbl_bgcol, foreground=config.chrs_lbl_fgcol)
	chars_used_label.grid(row=3, column=0, padx=5, pady=20, ipadx=2, ipady=2, sticky=tkinter.E)

	pass_length_label = tkinter.ttk.Label(window_content, text=config.pwd_lbl_text, 
						font=config.pwd_lbl_font, background=config.pwd_lbl_bgcol, 
						foreground=config.pwd_lbl_fgcol)
	pass_length_label.grid(row=4, column=0, ipadx=2, padx=5, sticky=tkinter.E)

	return chars_used_label, pass_length_label

def make_pwchar_section():

	checkbox_style = tkinter.ttk.Style()
	checkbox_style_name = config.chk_stl_name
	checkbox_style.configure(checkbox_style_name, background=config.chk_stl_bgcol, 
					foreground=config.chk_stl_fgcol, font=config.chk_stl_font)
	checkbox_style.map(checkbox_style_name, background=config.chk_stl_bgcol_map, 
						font=config.chk_stl_font_map)	
	
	upper_char_checkbox = tkinter.ttk.Checkbutton(window_content, text=config.upper_ckb_text, 
						style=checkbox_style_name, onvalue=1, offvalue=0, variable=upper_char_val)
	lower_char_checkbox = tkinter.ttk.Checkbutton(window_content, text=config.lower_ckb_text, 
						style=checkbox_style_name, onvalue=1, offvalue=0, variable=lower_char_val)
	numeric_char_checkbox = tkinter.ttk.Checkbutton(window_content, text=config.numeric_ckb_text, 
						style=checkbox_style_name, onvalue=1, offvalue=0, variable=numeric_char_val)
	symbol_char_checkbox = tkinter.ttk.Checkbutton(window_content, text=config.symbol_ckb_text, 
						style=checkbox_style_name, onvalue=1, offvalue=0, variable=symbol_char_val)

	upper_char_checkbox.grid(row=3, column=1, padx=2, ipadx=2, ipady=2, sticky=tkinter.W)
	lower_char_checkbox.grid(row=3, column=2, padx=2, ipadx=2, ipady=2, sticky=tkinter.W)
	numeric_char_checkbox.grid(row=3, column=3, padx=2, ipadx=2, ipady=2, sticky=tkinter.W)
	symbol_char_checkbox.grid(row=3, column=4, padx=2, ipadx=10, ipady=2, sticky=tkinter.W)

	return upper_char_checkbox, lower_char_checkbox, numeric_char_checkbox, symbol_char_checkbox	

def make_pwlen_section():

	radiobutton_style = tkinter.ttk.Style()
	radiobutton_style_name = config.rdb_stl_name
	radiobutton_style.configure(radiobutton_style_name, background=config.rdb_stl_bgcol, 
						foreground=config.rdb_stl_fgcol, font=config.rdb_stl_font)
	radiobutton_style.map(radiobutton_style_name, background=config.rdb_stl_bgcol_map, 
						font=config.rdb_stl_font_map)	

	pass_small_option = tkinter.ttk.Radiobutton(window_content, text=config.pwsmall_rdb_text, 
						style=radiobutton_style_name, value=1, variable=selected_pass_length, 
						command=deactivate_custom_entry)
	pass_medium_option = tkinter.ttk.Radiobutton(window_content, text=config.pwdmedium_rdb_text, 
						style=radiobutton_style_name, value=2, variable=selected_pass_length, 
						command=deactivate_custom_entry)
	pass_custom_option = tkinter.ttk.Radiobutton(window_content, text=config.pwcustom_rdb_text, 
						style=radiobutton_style_name, value=3, variable=selected_pass_length, 
						command=activate_custom_entry)

	pass_small_option.grid(row=4, column=1, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)
	pass_medium_option.grid(row=4, column=2, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)
	pass_custom_option.grid(row=4, column=3, sticky=tkinter.W, padx=2, ipadx=2, ipady=2)

	pass_custom_entry = tkinter.Entry(window_content, width=5, state=tkinter.DISABLED)
	pass_custom_entry.grid(row=4, column=4, sticky=tkinter.W)

	return pass_small_option, pass_medium_option, pass_custom_option, pass_custom_entry

def make_pw_entry():

	generated_password_entry = tkinter.ttk.Entry(window_content, state=config.pwde_state_ro, 
								justify=tkinter.CENTER, cursor=config.pwde_cursor, width=40)
	generated_password_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=15)

	return generated_password_entry

def make_buttons():

	reset_button = tkinter.ttk.Button(window_content, text=config.reset_btn_text, 
					command=reset_cmd)
	reset_button.grid(row=6, column=1, padx=10, pady=5)

	generate_button = tkinter.ttk.Button(window_content, text=config.generate_btn_text, 
						command=generate_password)
	generate_button.grid(row=6, column=2, padx=10, pady=5)

	quit_button = tkinter.ttk.Button(window_content, text=config.quit_btn_text, 
					command=quit_window)
	quit_button.grid(row=6, column=3, padx=10, pady=5)

	return reset_button, generate_button, quit_button

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
	generated_password_entry.configure(state=config.pwde_state_ro)

def generate_password():

	generated_password_entry.configure(state=tkinter.NORMAL)
	generated_password_entry.delete(0, tkinter.END)
	generated_password_entry.configure(state=config.pwde_state_ro)	

	upper_chosen = upper_char_val.get()
	lower_chosen = lower_char_val.get()
	numeric_chosen = numeric_char_val.get()
	symbol_chosen = symbol_char_val.get()

	upper_char_list = string.ascii_uppercase
	lower_char_list = string.ascii_lowercase
	numeric_char_list = string.digits
	symbol_char_list = string.punctuation

	if not upper_chosen and not lower_chosen and not numeric_chosen and not symbol_chosen:

		tkinter.messagebox.showwarning(title=config.no_char_sel_title, message=config.no_char_sel_msg)
		lower_char_val.set(1)
		lower_chosen = lower_char_val.get()

	msg = ''
	custom_pass_chars = 0
	pw_length = 0

	if selected_pass_length.get() == 1:

		pw_length = random.randint(8, 12)

	elif selected_pass_length.get() == 2:

		pw_length = random.randint(13, 16)

	elif selected_pass_length.get() == 3:

		try:
			custom_pass_chars = int(pass_custom_entry.get())
			if 4 <= custom_pass_chars <= 50:
				pw_length = custom_pass_chars

			else:
				tkinter.messagebox.showerror(title=config.inc_num_sel_title, message=config.inc_num_sel_msg)
				pass_custom_entry.delete(0, tkinter.END)
		except:
			tkinter.messagebox.showerror(title=config.nan_sel_title, message=config.nan_sel_msg)
			pass_custom_entry.delete(0, tkinter.END)

	if 4 <= pw_length <= 50:

		pw_chars = []
		chars_valid_list = []
		join_char = ''

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

		full_char_str = join_char.join(chars_valid_list)	

		for i in range(pw_length - len(pw_chars)):

			opt_elem_index = random.randint(0, len(full_char_str)-1)
			pw_chars.append(full_char_str[opt_elem_index])

		random.shuffle(pw_chars)
		final_password = join_char.join(pw_chars)

		generated_password_entry.configure(state=tkinter.NORMAL)
		generated_password_entry.insert(0, final_password)
		generated_password_entry.configure(state=config.pwde_state_ro)

def quit_window():

	main_program.destroy()

if __name__ == '__main__':

	main_program = create_main_program()
	window_content = create_window_content()
	test_label, welcome_label, main_msg_label = create_main_labels()
	upper_char_val, lower_char_val, numeric_char_val, symbol_char_val = create_ckb_vars()
	selected_pass_length = create_rdb_vars()
	chars_used_label, pass_length_label = create_util_labels()
	upper_char_checkbox, lower_char_checkbox, numeric_char_checkbox, symbol_char_checkbox = make_pwchar_section()
	pass_small_option, pass_medium_option, pass_custom_option, pass_custom_entry = make_pwlen_section()
	generated_password_entry = make_pw_entry()
	reset_button, generate_button, quit_button = make_buttons()
	main_program.mainloop()