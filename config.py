#!/usr/bin/python3


### Main window configuration

mw_title = 'Password Generator  ©rootshellace'
mw_bgcolor = '#006400'
mw_width = 640
mw_height = 360

### Main labels configuration

tst_lbl_text = ''
wlc_lbl_text = ' Welcome! '
msg_lbl_text = ' Use this tool to generate a random password! '
tst_lbl_font = ('Calibri', 14)
wlc_lbl_font = ('Calibri', 16, 'bold')
msg_lbl_font = ('Calibri', 14, 'bold')
main_lbl_bgcol = '#006400'
main_lbl_fgcol = '#000000'
main_lbl_rlf = 'flat'

### Utility labels configuration

chrs_lbl_text = 'Password Chars:'
chrs_lbl_font = ('Calibri', 10, 'bold')
chrs_lbl_bgcol = '#006400'
chrs_lbl_fgcol = '#FBB117'
pwd_lbl_text = 'Length -> 4 - 50:'
pwd_lbl_font = ('Calibri', 10, 'bold')
pwd_lbl_bgcol = '#006400' 
pwd_lbl_fgcol = '#FBB117'

### Styles configuration

chk_stl_name = 'PwChar.TCheckbutton'
chk_stl_bgcol = '#006400'
chk_stl_fgcol = '#FBB117'
chk_stl_font = ('Calibri', 10)
chk_stl_bgcol_map = [('active', '#006400')]
chk_stl_font_map = [('selected', ('Calibri', 10, 'italic'))]
rdb_stl_name = 'PwLen.TRadiobutton'
rdb_stl_bgcol = '#006400'
rdb_stl_fgcol = '#FBB117'
rdb_stl_font = ('Calibri', 10)
rdb_stl_bgcol_map = [('active', '#006400')]
rdb_stl_font_map = [('selected', ('Calibri', 10, 'italic'))]

### Checkbuttons configuration

upper_ckb_text = 'Use uppercase'
lower_ckb_text = 'Use lowercase'
numeric_ckb_text = 'Use numbers'
symbol_ckb_text = 'Use symbols'

### Radiobuttons configuration

pwsmall_rdb_text = '8-12 chars'
pwdmedium_rdb_text = '13-16 chars'
pwcustom_rdb_text = 'Custom no. :'

### Password entry configuration

pwde_state_ro = 'readonly'
pwde_cursor = 'xterm'

### Buttons configuration

reset_btn_text = 'Reset'
generate_btn_text = 'Generate'
quit_btn_text = 'Quit'

### Output messages configuration

no_char_sel_title = 'Warning!'
no_char_sel_msg = 'No charset selected!\nLowercase will be set as default!'
inc_num_sel_title = 'Error!'
inc_num_sel_msg = 'Selected number is not between 4 and 50!'
nan_sel_title = 'Error!'
nan_sel_msg = 'You inserted a non-numeric value!'