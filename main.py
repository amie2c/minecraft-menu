import pyautogui
import time
import threading
import keyboard
import tkinter as tk
from tkinter import simpledialog, messagebox
import random

stop_flags = {
    "spam_message": False,
    "auto_clicker": False,
    "party_spam": False,
    "sneak_spam": False,
    "private_message_spam": False,
    "anti_afk": False
}

threads = {}

def spam_message(text, delay_ms):
    time.sleep(5)
    while not stop_flags["spam_message"]:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('t')
        time.sleep(delay_ms / 1000)

def auto_clicker(hotkey, delay_ms, button):
    delay = delay_ms / 1000
    while not stop_flags["auto_clicker"]:
        if keyboard.is_pressed(hotkey):
            pyautogui.click(button=button)
            time.sleep(delay)
        else:
            time.sleep(0.01)

def spam_party_invite(playername, delay_ms):
    time.sleep(5)
    while not stop_flags["party_spam"]:
        pyautogui.typewrite(f"/party invite {playername}")
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('t')
        pyautogui.typewrite("/party disband")
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('t')
        time.sleep(delay_ms / 1000)

def spam_sneak(delay_ms):
    time.sleep(5)
    while not stop_flags["sneak_spam"]:
        pyautogui.keyDown('shift')
        time.sleep(0.1)
        pyautogui.keyUp('shift')
        time.sleep(delay_ms / 1000)

def spam_private_message(playername, message, delay_ms):
    time.sleep(5)
    while not stop_flags["private_message_spam"]:
        pyautogui.typewrite(f"/message {playername} {message}")
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('t')
        time.sleep(delay_ms / 1000)

def anti_afk():
    time.sleep(5)
    keys = ['w', 'a', 's', 'd']
    last_switch = time.time()
    switch_interval = random.uniform(5, 15)

    while not stop_flags["anti_afk"]:
        current_time = time.time()

        if current_time - last_switch > switch_interval:
            slot = str(random.randint(1, 9))
            pyautogui.press(slot)
            last_switch = current_time
            switch_interval = random.uniform(5, 15)

        action = random.choice(['move', 'jump', 'sneak', 'click', 'mouse'])
        duration = random.uniform(0.2, 1.0)

        if action == 'move':
            key = random.choice(keys)
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown(key)
            time.sleep(duration)
            pyautogui.keyUp(key)
            pyautogui.keyUp('ctrl')

        elif action == 'jump':
            pyautogui.press('space')

        elif action == 'sneak':
            pyautogui.keyDown('shift')
            time.sleep(duration)
            pyautogui.keyUp('shift')

        elif action == 'click':
            pyautogui.click()

        elif action == 'mouse':
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            pyautogui.moveRel(x, y, duration=0.3)

        time.sleep(random.uniform(1.0, 3.0))

def start_spam_message():
    if "spam_message" in threads and threads["spam_message"].is_alive():
        messagebox.showwarning("Warning", "Chat Spammer is already running!")
        return
    text = simpledialog.askstring("Chat Spammer", "Enter message to spam:")
    if not text:
        return
    delay = simpledialog.askinteger("Chat Spammer", "Delay between messages (ms):", minvalue=1)
    if not delay:
        return
    stop_flags["spam_message"] = False
    t = threading.Thread(target=spam_message, args=(text, delay), daemon=True)
    threads["spam_message"] = t
    t.start()
    update_stop_button("spam_message", True)
    messagebox.showinfo("Started", "Chat spamming started! Switch to Minecraft.")

def stop_spam_message():
    stop_flags["spam_message"] = True
    update_stop_button("spam_message", False)

def start_auto_clicker():
    if "auto_clicker" in threads and threads["auto_clicker"].is_alive():
        messagebox.showwarning("Warning", "Auto Clicker is already running!")
        return
    hotkey = simpledialog.askstring("Auto Clicker", "Hold which key to start clicking? (e.g., f6):")
    if not hotkey:
        return
    hotkey = hotkey.lower()
    delay = simpledialog.askinteger("Auto Clicker", "Delay between clicks (ms):", minvalue=1)
    if not delay:
        return
    button = simpledialog.askstring("Auto Clicker", "Click type? (left, right, middle):")
    if not button or button.lower() not in ['left', 'right', 'middle']:
        button = 'left'
    stop_flags["auto_clicker"] = False
    t = threading.Thread(target=auto_clicker, args=(hotkey, delay, button.lower()), daemon=True)
    threads["auto_clicker"] = t
    t.start()
    update_stop_button("auto_clicker", True)
    messagebox.showinfo("Started", f"Auto clicker started! Hold '{hotkey}' in Minecraft.")

def stop_auto_clicker():
    stop_flags["auto_clicker"] = True
    update_stop_button("auto_clicker", False)

def start_party_spam():
    if "party_spam" in threads and threads["party_spam"].is_alive():
        messagebox.showwarning("Warning", "Party Spammer is already running!")
        return
    playername = simpledialog.askstring("Party Spammer", "Enter player name to invite:")
    if not playername:
        return
    delay = simpledialog.askinteger("Party Spammer", "Delay between spam (ms):", minvalue=1)
    if not delay:
        return
    stop_flags["party_spam"] = False
    t = threading.Thread(target=spam_party_invite, args=(playername, delay), daemon=True)
    threads["party_spam"] = t
    t.start()
    update_stop_button("party_spam", True)
    messagebox.showinfo("Started", "Party spam started! Switch to Minecraft.")

def stop_party_spam():
    stop_flags["party_spam"] = True
    update_stop_button("party_spam", False)

def start_sneak_spam():
    if "sneak_spam" in threads and threads["sneak_spam"].is_alive():
        messagebox.showwarning("Warning", "Sneak Spammer is already running!")
        return
    delay = simpledialog.askinteger("Sneak Spammer", "Delay between sneak toggles (ms):", minvalue=1)
    if not delay:
        return
    stop_flags["sneak_spam"] = False
    t = threading.Thread(target=spam_sneak, args=(delay,), daemon=True)
    threads["sneak_spam"] = t
    t.start()
    update_stop_button("sneak_spam", True)
    messagebox.showinfo("Started", "Sneak spam started! Switch to Minecraft.")

def stop_sneak_spam():
    stop_flags["sneak_spam"] = True
    update_stop_button("sneak_spam", False)

def start_private_message_spam():
    if "private_message_spam" in threads and threads["private_message_spam"].is_alive():
        messagebox.showwarning("Warning", "Private Message Spammer is already running!")
        return
    playername = simpledialog.askstring("Private Message Spammer", "Enter player name:")
    if not playername:
        return
    message = simpledialog.askstring("Private Message Spammer", "Enter message to send:")
    if not message:
        return
    delay = simpledialog.askinteger("Private Message Spammer", "Delay between messages (ms):", minvalue=1)
    if not delay:
        return
    stop_flags["private_message_spam"] = False
    t = threading.Thread(target=spam_private_message, args=(playername, message, delay), daemon=True)
    threads["private_message_spam"] = t
    t.start()
    update_stop_button("private_message_spam", True)
    messagebox.showinfo("Started", "Private message spam started! Switch to Minecraft.")

def stop_private_message_spam():
    stop_flags["private_message_spam"] = True
    update_stop_button("private_message_spam", False)

def start_anti_afk():
    if "anti_afk" in threads and threads["anti_afk"].is_alive():
        messagebox.showwarning("Warning", "Anti-AFK is already running!")
        return
    stop_flags["anti_afk"] = False
    t = threading.Thread(target=anti_afk, daemon=True)
    threads["anti_afk"] = t
    t.start()
    update_stop_button("anti_afk", True)
    messagebox.showinfo("Started", "Anti-AFK started! Switch to Minecraft.")

def stop_anti_afk():
    stop_flags["anti_afk"] = True
    update_stop_button("anti_afk", False)

def update_stop_button(name, running):
    if running:
        stop_buttons[name].pack(side=tk.TOP, padx=5, pady=3)
    else:
        stop_buttons[name].pack_forget()

def on_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        for key in stop_flags:
            stop_flags[key] = True
        root.destroy()

root = tk.Tk()
root.title("Minecraft Menu")
root.geometry("350x470")

tk.Label(root, text="Minecraft Helper Menu", font=("Arial", 16)).pack(pady=10)

btn1 = tk.Button(root, text="1. Chat Spammer", width=30, command=start_spam_message)
btn1.pack(pady=5)
btn2 = tk.Button(root, text="2. Auto Clicker", width=30, command=start_auto_clicker)
btn2.pack(pady=5)
btn3 = tk.Button(root, text="3. Party Invite Spammer", width=30, command=start_party_spam)
btn3.pack(pady=5)
btn4 = tk.Button(root, text="4. Sneak Spammer", width=30, command=start_sneak_spam)
btn4.pack(pady=5)
btn5 = tk.Button(root, text="5. Private Message Spammer", width=30, command=start_private_message_spam)
btn5.pack(pady=5)
btn6 = tk.Button(root, text="6. Anti AFK", width=40, command=start_anti_afk)
btn6.pack(pady=10)

label_fun = tk.Label(root, text="just for fun", font=("Arial", 8), fg="gray")
label_fun.pack(side='bottom', anchor='e', padx=5, pady=2)

frame_stop = tk.Frame(root)
frame_stop.pack(anchor='nw', padx=10)

stop_buttons = {}

stop_buttons["spam_message"] = tk.Button(frame_stop, text="Stop Chat Spammer", width=20, fg="red", command=stop_spam_message)
stop_buttons["auto_clicker"] = tk.Button(frame_stop, text="Stop Auto Clicker", width=20, fg="red", command=stop_auto_clicker)
stop_buttons["party_spam"] = tk.Button(frame_stop, text="Stop Party Spammer", width=20, fg="red", command=stop_party_spam)
stop_buttons["sneak_spam"] = tk.Button(frame_stop, text="Stop Sneak Spammer", width=20, fg="red", command=stop_sneak_spam)
stop_buttons["private_message_spam"] = tk.Button(frame_stop, text="Stop Private Msg Spammer", width=20, fg="red", command=stop_private_message_spam)
stop_buttons["anti_afk"] = tk.Button(frame_stop, text="Stop Anti AFK", width=20, fg="red", command=stop_anti_afk)

for btn in stop_buttons.values():
    btn.pack_forget()

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
