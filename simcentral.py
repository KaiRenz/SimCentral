import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
import os
from pathlib import Path
import configparser
import subprocess

# Initialization
config = configparser.RawConfigParser()

def browseFiles(entry):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")
    entry.delete(0,'end')
    entry.insert(0,filename)
    # Autosave
    if chkbtn_autosave_changes.getvar('chkbtn_autosave_changes_state') == 1:
        save_config()

def openTool(entry):
    if entry['state'] == 'normal':
        subprocess.Popen(entry.get())


def checkCheckbuttonState(index):
    if index=="1":
        if checkbutton_1.getvar('checkbutton_1_state') == "0":
            entry_1.config(state='disabled')
            browse_button_1.config(state='disabled')
            open_button_1.config(state='disabled')
        else:
            entry_1.config(state='enabled')
            browse_button_1.config(state='enabled')
            open_button_1.config(state='enabled')
    if index=="2":
        if checkbutton_2.getvar('checkbutton_2_state') == "0":
            entry_2.config(state='disabled')
            browse_button_2.config(state='disabled')
            open_button_2.config(state='disabled')
        else:
            entry_2.config(state='enabled')
            browse_button_2.config(state='enabled')
            open_button_2.config(state='enabled')
    if index=="3":
        if checkbutton_3.getvar('checkbutton_3_state') == "0":
            entry_3.config(state='disabled')
            browse_button_3.config(state='disabled')
            open_button_3.config(state='disabled')
        else:
            entry_3.config(state='enabled')
            browse_button_3.config(state='enabled')
            open_button_3.config(state='enabled')
    if index=="4":
        if checkbutton_4.getvar('checkbutton_4_state') == "0":
            entry_4.config(state='disabled')
            browse_button_4.config(state='disabled')
            open_button_4.config(state='disabled')
        else:
            entry_4.config(state='enabled')
            browse_button_4.config(state='enabled')
            open_button_4.config(state='enabled')
    if index=="5":
        if checkbutton_5.getvar('checkbutton_5_state') == "0":
            entry_5.config(state='disabled')
            browse_button_5.config(state='disabled')
            open_button_5.config(state='disabled')
        else:
            entry_5.config(state='enabled')
            browse_button_5.config(state='enabled')
            open_button_5.config(state='enabled')
    if index=="7":
        save_config()
        load_config()
    # Autosave
    if chkbtn_autosave_changes.getvar('chkbtn_autosave_changes_state') == 1:
        save_config()

def start_all():
    if (entry_1['state'] == 'normal') or (entry_1['state'] == 'enabled'):
        subprocess.Popen(entry_1.get())
    if (entry_2['state'] == 'normal') or (entry_2['state'] == 'enabled'):
        subprocess.Popen(entry_2.get())
    if (entry_3['state'] == 'normal') or (entry_3['state'] == 'enabled'):
        subprocess.Popen(entry_3.get())
    if (entry_4['state'] == 'normal') or (entry_4['state'] == 'enabled'):
        subprocess.Popen(entry_4.get())
    if (entry_5['state'] == 'normal') or (entry_5['state'] == 'enabled'):
        subprocess.Popen(entry_5.get())

def on_focus_out(event):
    # Autosave
    if chkbtn_autosave_changes.getvar('chkbtn_autosave_changes_state') == 1:
        save_config()

def save_config():
    # Check if config folder exists. If not, create it
    directory = os.path.expanduser('~') + '\\AppData\\Local\\SimCentral\\'
    filename = directory + 'config.ini'
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Check if the file exists. If not, create it
    if not os.path.exists(filename):
        config_template = """
            [SETTINGS]
            autostart_tools = 1

            [CHECKBUTTONS]
            checkbutton_1 = 0
            checkbutton_2 = 0
            checkbutton_3 = 0
            checkbutton_4 = 0
            checkbutton_5 = 0

            [ENTRIES]
            entry_1 = none
            entry_2 = none
            entry_3 = none
            entry_4 = none
            entry_5 = none
            """
        with open(filename, "w") as f:
            f.write(config_template)
            f.close()
            
    # Set the config
    config.read(filename)
    if checkbutton_1.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_1', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_1', '0')
    if checkbutton_2.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_2', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_2', '0')
    if checkbutton_3.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_3', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_3', '0')
    if checkbutton_4.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_4', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_4', '0')
    if checkbutton_5.instate(['selected']):
        config.set('CHECKBUTTONS', 'Checkbutton_5', '1')
    else:
        config.set('CHECKBUTTONS', 'Checkbutton_5', '0')
    config.set('ENTRIES', 'entry_1', entry_1.get())
    config.set('ENTRIES', 'entry_2', entry_2.get())
    config.set('ENTRIES', 'entry_3', entry_3.get())
    config.set('ENTRIES', 'entry_4', entry_4.get())
    config.set('ENTRIES', 'entry_5', entry_5.get())
    if chkbtn_autostart_tools.instate(['selected']):
        print("yes")
        config.set('SETTINGS', 'autostart_tools', '1')
    else:
        config.set('SETTINGS', 'autostart_tools', '0')
    if chkbtn_autosave_changes.instate(['selected']):
        config.set('SETTINGS', 'autosave_changes', '1')
    else:
        config.set('SETTINGS', 'autosave_changes', '0')

    # Write the config
    with open(filename, "w") as f:
        config.write(f)
    
def load_config():
    # Check for the config
    # Check if config folder exists. If not, create it
    directory = os.path.expanduser('~') + '\\AppData\\Local\\SimCentral\\'
    filename = directory + 'config.ini'
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Check if the file exists. If not, create it
    if not os.path.exists(filename):
        config_template = """
[SETTINGS]
autostart_tools = 0
autosave_changes = 0

[CHECKBUTTONS]
checkbutton_1 = 0
checkbutton_2 = 0
checkbutton_3 = 0
checkbutton_4 = 0
checkbutton_5 = 0

[ENTRIES]
entry_1 = none
entry_2 = none
entry_3 = none
entry_4 = none
entry_5 = none
            """
        with open(filename, "w") as f:
            f.write(config_template)
            f.close()


    directory = os.path.expanduser('~') + '\\AppData\\Local\\SimCentral\\'
    filename = directory + 'config.ini'
    if os.path.exists(filename):
        config.read(filename)
        entry_1.delete(0,'end')
        entry_1.insert(0,config['ENTRIES']['entry_1'])
        entry_2.delete(0,'end')
        entry_2.insert(0,config['ENTRIES']['entry_2'])
        entry_3.delete(0,'end')
        entry_3.insert(0,config['ENTRIES']['entry_3'])
        entry_4.delete(0,'end')
        entry_4.insert(0,config['ENTRIES']['entry_4'])
        entry_5.delete(0,'end')
        entry_5.insert(0,config['ENTRIES']['entry_5'])
        if config['CHECKBUTTONS']['Checkbutton_1'] == "1":
            checkbutton_1.setvar('checkbutton_1_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_1_state', 0)
            entry_1.config(state='disabled')
            browse_button_1.config(state='disabled')
            open_button_1.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_2'] == "1":
            checkbutton_1.setvar('checkbutton_2_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_2_state', 0)
            entry_2.config(state='disabled')
            browse_button_2.config(state='disabled')
            open_button_2.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_3'] == "1":
            checkbutton_1.setvar('checkbutton_3_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_3_state', 0)
            entry_3.config(state='disabled')
            browse_button_3.config(state='disabled')
            open_button_3.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_4'] == "1":
            checkbutton_1.setvar('checkbutton_4_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_4_state', 0)
            entry_4.config(state='disabled')
            browse_button_4.config(state='disabled')
            open_button_4.config(state='disabled')
        if config['CHECKBUTTONS']['Checkbutton_5'] == "1":
            checkbutton_1.setvar('checkbutton_5_state', 1)
        else: 
            checkbutton_1.setvar('checkbutton_5_state', 0)
            entry_5.config(state='disabled')
            browse_button_5.config(state='disabled')
            open_button_5.config(state='disabled')
        if config['SETTINGS']['autostart_tools'] == "1":
            chkbtn_autostart_tools.setvar('chkbtn_autostart_tools_state', 1)
        else:
            chkbtn_autostart_tools.setvar('chkbtn_autostart_tools_state', 0)
        if config['SETTINGS']['autosave_changes'] == "1":
            chkbtn_autostart_tools.setvar('chkbtn_autosave_changes_state', 1)
        else:
            chkbtn_autostart_tools.setvar('chkbtn_autosave_changes_state', 0)



# Window
window = ttk.Window(themename='superhero')
window.title('SimCentral')
window.iconbitmap("icons8-automation-48.ico")
window.bind("<FocusOut>", on_focus_out)

# left frame
left_frame = ttk.Frame(master=window)
left_frame.pack(side='left', expand='True', fill='both', padx=5)

# menu frame
menu_frame = ttk.Frame(master=left_frame, width=15)
menu_label = ttk.Label(master=menu_frame, text="Menu", font=['Segoe UI', 15, 'bold'])
menu_label.pack(pady=5)

# load config button
load_cfg_button = ttk.Button(master=menu_frame, text='Load config', command=lambda:load_config())
load_cfg_button.configure(width='15')
load_cfg_button.pack(pady=10)

# save config button
save_cfg_button = ttk.Button(master=menu_frame, text="Save config", command=lambda:save_config())
save_cfg_button.configure(width='15')
save_cfg_button.pack()
menu_frame.pack(expand='True', fill='both')

# Exit frame
exit_frame = ttk.Frame(master=window)
exit_frame.pack()

# Exit button
exit_button = ttk.Button(master=left_frame, text="Exit", command=window.destroy)
exit_button.configure(width='15')
exit_button.pack(pady=10)


# notebook widget
notebook = ttk.Notebook(master=window)

# Tab quickstart
tab_quickstart = ttk.Frame(master=notebook)
frame_entries = ttk.Frame(master=tab_quickstart, borderwidth=10)
frame_entries.pack()

# entries
frame_entry1 = ttk.Frame(master=frame_entries, width=30)
frame_entry2 = ttk.Frame(master=frame_entries, width=30)
frame_entry3 = ttk.Frame(master=frame_entries, width=30)
frame_entry4 = ttk.Frame(master=frame_entries, width=30)
frame_entry5 = ttk.Frame(master=frame_entries, width=30)
frame_entry1.pack()
frame_entry2.pack()
frame_entry3.pack()
frame_entry4.pack()
frame_entry5.pack()
entry_1 = ttk.Entry(master=frame_entry1, width=100)
entry_2 = ttk.Entry(master=frame_entry2, width=100)
entry_3 = ttk.Entry(master=frame_entry3, width=100)
entry_4 = ttk.Entry(master=frame_entry4, width=100)
entry_5 = ttk.Entry(master=frame_entry5, width=100)
browse_button_1 = ttk.Button(master=frame_entry1, text="Browse", command=lambda:browseFiles(entry_1))
browse_button_2 = ttk.Button(master=frame_entry2, text="Browse", command=lambda:browseFiles(entry_2))
browse_button_3 = ttk.Button(master=frame_entry3, text="Browse", command=lambda:browseFiles(entry_3))
browse_button_4 = ttk.Button(master=frame_entry4, text="Browse", command=lambda:browseFiles(entry_4))
browse_button_5 = ttk.Button(master=frame_entry5, text="Browse", command=lambda:browseFiles(entry_5))
open_button_1 = ttk.Button(master=frame_entry1, text='Open', command=lambda:openTool(entry_1))
open_button_2 = ttk.Button(master=frame_entry2, text='Open', command=lambda:openTool(entry_2))
open_button_3 = ttk.Button(master=frame_entry3, text='Open', command=lambda:openTool(entry_3))
open_button_4 = ttk.Button(master=frame_entry4, text='Open', command=lambda:openTool(entry_4))
open_button_5 = ttk.Button(master=frame_entry5, text='Open', command=lambda:openTool(entry_5))
checkbutton_1 = ttk.Checkbutton(master=frame_entry1, style='Roundtoggle.Toolbutton', variable='checkbutton_1_state', command=lambda:checkCheckbuttonState("1"))
checkbutton_2 = ttk.Checkbutton(master=frame_entry2, style='Roundtoggle.Toolbutton', variable='checkbutton_2_state', command=lambda:checkCheckbuttonState("2"))
checkbutton_3 = ttk.Checkbutton(master=frame_entry3, style='Roundtoggle.Toolbutton', variable='checkbutton_3_state', command=lambda:checkCheckbuttonState("3"))
checkbutton_4 = ttk.Checkbutton(master=frame_entry4, style='Roundtoggle.Toolbutton', variable='checkbutton_4_state', command=lambda:checkCheckbuttonState("4"))
checkbutton_5 = ttk.Checkbutton(master=frame_entry5, style='Roundtoggle.Toolbutton', variable='checkbutton_5_state', command=lambda:checkCheckbuttonState("5"))
checkbutton_1.pack(pady=10, side='left')
checkbutton_2.pack(pady=10, side='left')
checkbutton_3.pack(pady=10, side='left')
checkbutton_4.pack(pady=10, side='left')
checkbutton_5.pack(pady=10, side='left')
entry_1.pack(pady=10, side='left')
entry_2.pack(pady=10, side='left')
entry_3.pack(pady=10, side='left')
entry_4.pack(pady=10, side='left')
entry_5.pack(pady=10, side='left')
browse_button_1.pack(side='left')
browse_button_2.pack(side='left')
browse_button_3.pack(side='left')
browse_button_4.pack(side='left')
browse_button_5.pack(side='left')
open_button_1.pack(padx=5, side='left')
open_button_2.pack(padx=5, side='left')
open_button_3.pack(padx=5, side='left')
open_button_4.pack(padx=5, side='left')
open_button_5.pack(padx=5, side='left')

# start_all button
start_all_button = ttk.Button(master=tab_quickstart, text='Open all', command=lambda:start_all())
start_all_button.pack(side='right', padx=10, pady=10)


# Setups Tab
tab_setuptool = ttk.Frame(master=notebook)
frame_setuptool = ttk.Frame(master=tab_setuptool, borderwidth=10)
frame_setuptool.pack()
setups_notebook = ttk.Notebook(master=tab_setuptool)
tab_setups_gng = ttk.Frame(master=setups_notebook)
setups_notebook.add(tab_setups_gng, text="GNG")
tab_setups_vrs = ttk.Frame(master=setups_notebook)
setups_notebook.add(tab_setups_vrs, text="VRS")
setups_notebook.pack(side='left', expand='True', fill='both', padx=5)

# Briefing Tab
tab_briefing = ttk.Frame(master=notebook)



# Tab settings
tab_settings = ttk.Frame(master=notebook)
frame_settings = ttk.Frame(master=tab_settings, borderwidth=10)
frame_settings.pack(side='left', expand='True', fill='both', padx=5)

chkbtn_autostart_tools = ttk.Checkbutton(master=frame_settings, style='Roundtoggle.Toolbutton', variable='chkbtn_autostart_tools_state', command=lambda:checkCheckbuttonState("6"))
chkbtn_autostart_tools.grid(row=0, column=0)
lbl_autostart_tools = ttk.Label(master=frame_settings, text='Autostart enabled tools')
lbl_autostart_tools.grid(row=0, column=1, sticky='w')

chkbtn_autosave_changes = ttk.Checkbutton(master=frame_settings, style='Roundtoggle.Toolbutton', variable='chkbtn_autosave_changes_state', command=lambda:checkCheckbuttonState("7"))
chkbtn_autosave_changes.grid(row=1, column=0)
lbl_autosave_changes = ttk.Label(master=frame_settings, text="AutoSave settings on change")
lbl_autosave_changes.grid(row=1, column=1, sticky='w')



notebook.add(tab_quickstart, text='Tool Quickstart')
notebook.add(tab_setuptool, text='Setup Sync')
notebook.add(tab_briefing, text="Briefing")
notebook.add(tab_settings, text='Settings')
notebook.pack(padx=5, pady=10)




# run
load_config()
if config['SETTINGS']['autostart_tools'] == "1":
        start_all()
window.mainloop()