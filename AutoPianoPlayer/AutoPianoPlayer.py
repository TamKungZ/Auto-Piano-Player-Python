import tkinter as tk
import json
import time
import threading
import keyboard
from pynput.keyboard import Controller
from tkinter import messagebox
from tkinter import Label

root = tk.Tk()
root.title("Auto Piano Player")
root.geometry("500x400")

root.attributes('-topmost', True)

root.iconbitmap('icon.ico')

import tkinter.font as tkFont
root.option_add('*Font', 'Kanit 10')

keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

settings = {
    "keys_to_play": [],
    "loop": False
}

keyboard_controller = Controller()

stop_event = threading.Event()

def play_key(key):
    keyboard_controller.press(key)
    keyboard_controller.release(key)

def play_auto():
    while True:
        for key_group, delay in settings["keys_to_play"]:
            if stop_event.is_set():
                return
            for key in key_group:
                play_key(key)
            time.sleep(delay)
        if not settings["loop"]:
            break

def save_settings():
    with open('piano_settings.json', 'w') as f:
        json.dump(settings, f)
    messagebox.showinfo("Settings", "Settings saved successfully.")

def load_settings():
    global settings
    try:
        with open('piano_settings.json', 'r') as f:
            settings = json.load(f)
        messagebox.showinfo("Settings", "Settings loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Settings file not found.")

def add_key_row():
    row_frame = tk.Frame(root)
    row_frame.pack(pady=5)

    key_vars = []
    key_var = tk.StringVar()
    key_vars.append(key_var)
    key_menu = tk.OptionMenu(row_frame, key_var, *keys)
    key_menu.pack(side=tk.LEFT, padx=5)

    delay_var = tk.DoubleVar(value=0.5)
    delay_entry = tk.Entry(row_frame, textvariable=delay_var, width=5)
    delay_entry.pack(side=tk.LEFT, padx=5)

    def add_more_key():
        key_var = tk.StringVar()
        key_vars.append(key_var)
        key_menu = tk.OptionMenu(row_frame, key_var, *keys)
        key_menu.pack(side=tk.LEFT, padx=5)

    add_more_button = tk.Button(row_frame, text="Add More Key", command=add_more_key)
    add_more_button.pack(side=tk.LEFT, padx=5)

    def remove_row():
        row_frame.destroy()
        settings["keys_to_play"].remove(([var.get() for var in key_vars], delay_var.get()))

    remove_button = tk.Button(row_frame, text="Remove", command=remove_row)
    remove_button.pack(side=tk.LEFT, padx=5)

    def add_key():
        settings["keys_to_play"].append(([var.get() for var in key_vars], delay_var.get()))

    add_button = tk.Button(row_frame, text="Add", command=add_key)
    add_button.pack(side=tk.LEFT, padx=5)

def stop_auto():
    stop_event.set()

save_button = tk.Button(root, text="Save", command=save_settings, bg="lightblue", width=10)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load", command=load_settings, bg="lightblue", width=10)
load_button.pack(pady=5)

def start_auto():
    stop_event.clear()
    threading.Thread(target=play_auto).start()

play_button = tk.Button(root, text="Play Auto", command=start_auto, bg="green", fg="white", width=10)
play_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_auto, bg="red", fg="white", width=10)
stop_button.pack(pady=5)

add_key_button = tk.Button(root, text="Add Key", command=add_key_row, bg="lightgrey", width=10)
add_key_button.pack(pady=5)

def setup_keybind():
    keyboard.add_hotkey('ctrl+shift+p', start_auto)
    keyboard.add_hotkey('ctrl+shift+s', stop_auto)
    messagebox.showinfo("Keybind", "Keybind set:\nctrl+shift+p to Play Auto\nctrl+shift+s to Stop")

setup_keybind() 

def toggle_loop():
    settings["loop"] = not settings["loop"]
    loop_button.config(text="Loop: ON" if settings["loop"] else "Loop: OFF")

loop_button = tk.Button(root, text="Loop: OFF", command=toggle_loop, bg="lightgrey", width=10)
loop_button.pack(pady=5)

def clear_all():
    global settings
    settings = {"keys_to_play": [], "loop": False}
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    messagebox.showinfo("Clear", "All settings cleared.")

clear_button = tk.Button(root, text="Clear", command=clear_all, bg="orange", fg="white", width=10)
clear_button.pack(pady=5)

l = Label(text = "Auto Piano Player v0.0.1")
t = Label(text = "By TamKungZ_")
l.pack()
t.pack()

root.mainloop()
