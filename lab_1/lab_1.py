from tkinter import *
from tkinter import filedialog
from tkinter import font
import json
from os import listdir
from os.path import isfile, join

root = Tk()
root.title('Laboratory Work No. 1 - Popescu Paula')
root.iconbitmap('C:/Users/Smart/Desktop/sem5/CS/Lab1/Audit/icon.ico')
root.geometry('1000x600')

# Create New File Function
def new_file():
	# Delete previous text
	my_text.delete('1.0', END)
	
	# Update status bars 
	root.title('New File')
	status_bar.config(text = 'New File       ')

# Open Files
def open_file():
	# Delete previous text
	my_text.delete('1.0', END)
	
	# Grab  Filename
	text_file = filedialog.askopenfilename(
		initialdir = 'C:/Users/Smart/Desktop/sem5/CS/Lab1/Audit/Ubuntu',
		title = 'Open File', filetypes = (('All Files', '*.*'), ) )
	
	# Update Status bars
	name = text_file
	status_bar.config(text = f'{name}       ')
	name = name.replace('C:/Users/Smart/Desktop/sem5/CS/Lab1/Audit/Ubuntu', '')
	root.title(f'{name} - Popescu Paula')

	# Open the file
	text_file = open(text_file, 'r')
	stuff = text_file.read()

	# Add file to textbox
	my_text.insert(END, stuff)

	# Close the opened file
	text_file.close()

# Save As File
def save_as_file():
	text_file = filedialog.asksaveasfilename(
		defaultextension = '.*',
		initialdir = 'C:/Users/Smart/Desktop/sem5/CS/Lab1',
		title = 'Save File', filetypes = (('All Files', '*.*'), ))
	if text_file:
		# Update Status Bars
		name = text_file
		status_bar.config(text = f'{name}       ')
		name = name.replace('C:/Users/Smart/Desktop/sem5/CS/Lab1/Audit/Ubuntu', '')
		root.title(f'{name} - Popescu Paula')

		# Save the file
		text_file = open(text_file, 'w')
		text_file.write(my_text.get(1.0, END))
		
		# Close the file
		text_file.close()

def find_all(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub) #use start += 1 to find overlapping matches

def save_to_json():
	text_file = filedialog.asksaveasfilename(
		defaultextension = '.*',
		initialdir = 'C:/Users/Smart/Desktop/sem5/CS/Lab1',
		title = 'Save File', filetypes = (('All Files', '*.*'), ))

	if text_file:
		# Update Status Bars
		name = text_file
		status_bar.config(text = f'{name}      ')
		name = name.replace('C:/Users/Smart/Desktop/sem5/CS/Lab1/Audit/Ubuntu', '')
		root.title(f'{name} - Popescu Paula')

		# Save the file
		with open(text_file, 'w') as outfile:
			

			contents = my_text.get(1.0, END)
			contents = contents.replace('            :', ':')
			contents = contents.replace('           :', ':')
			contents = contents.replace('          :', ':')
			contents = contents.replace('         :', ':')
			contents = contents.replace('        :', ':')
			contents = contents.replace('       :', ':')
			contents = contents.replace('      :', ':')
			contents = contents.replace('     :', ':')
			contents = contents.replace('    :', ':')
			contents = contents.replace('   :', ':')
			contents = contents.replace('  :', ':')
			contents = contents.replace(' :', ':')

			start = list(find_all(contents, '<custom_item>'))
			ending = list(find_all(contents, '</custom_item>'))

			custom_item = {} 

			custom_item['AUDIT_XML'] = {'type' : [], 'description' : [], 'file' : [], 'xsl_stmt' : [], 'select' : [], 'regex' : [], 'not_expect' : []}
			custom_item['AUDIT_ALLOWED_OPEN_PORTS'] = {'type' : [], 'description' : [], 'port_type' : [], 'ports': []}
			custom_item['AUDIT_DENIED_OPEN_PORTS'] = {'type' : [], 'description' : [], 'port_type' : [], 'ports' : []}
			custom_item['AUDIT_PROCESS_ON_PORT'] = {'type' : [], 'description' : [], 'port_type' : [], 'ports' : [], 'name' : []}
			custom_item['BANNER_CHECK'] = {'type' : [], 'description' : [], 'file' : [], 'content' : [], 'is_substring' : []}
			custom_item['CHKCONFIG'] = {'type' : [], 'description' : [], 'service' : [], 'levels' : [], 'status' : [], 'check_option' : []}
			custom_item['CMD_EXEC'] = {'type' : [], 'description' : [], 'cmd' : [], 'timeout' : [], 'expect' : [], 'dont_echo_cmd': []}
			custom_item['FILE_CHECK'] = {'uid' : [], 'gid' : [], 'check_uneveness' : [], 'system' : [], 'description' : [], 'file' : [], 'file_required' : [], 'owner' : [], 'group' : [], 'mode' : [], 'mask' : [], 'md5' : [], 'ignore' : [], 'attr' : []}
			custom_item['FILE_CHECK_NOT'] = custom_item['FILE_CHECK'].copy()
			custom_item['FILE_CONTENT_CHECK'] = {'system' : [], 'type' : [], 'description' : [], 'file' : [], 'regex' : [], 'expect' : [], 'search_locations' : [], 'ignore' : [], 'file_required' : [], 'string_required' : []}
			custom_item['FILE_CONTENT_CHECK_NOT'] = {'type' : [], 'description' : [], 'file' : [], 'regex' : [], 'expect' : [], 'file_required' : [], 'string_required' : []}
			custom_item['GRAMMAR_CHECK'] = {'type' : [], 'description' : [], 'file' : [], 'regex' : []}
			custom_item['MACOSX_DEFAULTS_READ'] = {'system' : [], 'type' : [], 'description' : [], 'plist_name' : [], 'plist_item' : [], 'plist_option' : [], 'byhost' : [], 'not_regex' : [], 'managed_path' : [], 'plist_user' : [], 'regex' : []}
			custom_item['PKG_CHECK'] = {'system' : [], 'type' : [], 'description' : [], 'pkg' : [], 'required' : [], 'version' : [], 'operator' : []}
			custom_item['PROCESS_CHECK'] = {'system' : [], 'type' : [], 'name' : [], 'status' : []}
			custom_item['RPM_CHECK'] = {'type' : [], 'description' : [], 'rpm' : [], 'operator' : [], 'required' : []}
			custom_item['SVC_DROP'] = {'type' : [], 'description' : [], 'service' : [], 'property' : [], 'value' : [], 'regex' : [], 'svcprop_option' : []}
			custom_item['XINETD_SVC'] = {'type' : [], 'description' : [], 'service' : [], 'status' : []}

			for i in range(len(start)):
				content_type_block = contents[start[i] + 13 : ending[i]]
				type_ = content_type_block[content_type_block.find('type:') + 6: content_type_block[content_type_block.find('type:') + 5 :].find('\n') + content_type_block.find('type:') + 5 ]
				for element in list(custom_item[type_].keys()):
					length_of_element = len(element) + 1
					if content_type_block.find(element) != -1:
						custom_item[type_][element].append(content_type_block[content_type_block.find(element + ':') + length_of_element: content_type_block[content_type_block.find(element + ':') + length_of_element :].find('\n') + content_type_block.find(element + ':') + length_of_element ].strip())
					else:
						custom_item[type_][element].append('')

			json.dump(custom_item, outfile)


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady = 5)

# Create out Scollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

# Create Text Box
my_text = Text(my_frame, width = 97, height = 25,
			 font = ('Helvetica', 16), selectbackground = 'blue',
			 selectforeground = 'black', undo = True,
			 yscrollcommand = text_scroll.set)
my_text.pack()

# Configure out Scrollbar
text_scroll.config(command = my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'New', command = new_file)
file_menu.add_command(label = 'Open', command = open_file)
file_menu.add_command(label = 'Save')
file_menu.add_command(label = 'Save As', command = save_as_file)
file_menu.add_command(label = 'Save to JSON', command = save_to_json)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = 'Edit', menu = edit_menu)
edit_menu.add_command(label = 'Cut')
edit_menu.add_command(label = 'Copy')
edit_menu.add_command(label = 'Paste')
edit_menu.add_command(label = 'Undo')
edit_menu.add_command(label = 'Redo')

# Add Status Bar to Bottom
status_bar = Label(root, text = 'Ready     ', anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)
root.mainloop()