import pyautogui
import time
import threading
import keyboard
import tkinter as tk
from tkinter import simpledialog, messagebox

def spam_message(text, delay_ms):
    time.sleep(5)
    while True:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('t')
        time.sleep(delay_ms / 1000)

def auto_clicker(hotkey, delay_ms, button):
    delay = delay_ms / 1000
    while True:
        if keyboard.is_pressed(hotkey):
            pyautogui.click(button=button)
            time.sleep(delay)
        else:
            time.sleep(0.01)

def spam_party_invite(playername, delay_ms):
    time.sleep(5)
    while True:
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
    while True:
        pyautogui.keyDown('shift')
        time.sleep(0.1)
        pyautogui.keyUp('shift')
        time.sleep(delay_ms / 1000)

def spam_private_message(playername, message, delay_ms):
    time.sleep(5)
    while True:
        pyautogui.typewrite(f"/message {playername} {message}")
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('t')
        time.sleep(delay_ms / 1000)

def start_spam_message():
    text = simpledialog.askstring("Chat Spammer", "Enter message to spam:")
    if not text:
        return
    delay = simpledialog.askinteger("Chat Spammer", "Delay between messages (ms):", minvalue=1)
    if not delay:
        return
    threading.Thread(target=spam_message, args=(text, delay), daemon=True).start()
    messagebox.showinfo("Started", "Chat spamming started! Switch to Minecraft.")

def start_auto_clicker():
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
    threading.Thread(target=auto_clicker, args=(hotkey, delay, button.lower()), daemon=True).start()
    messagebox.showinfo("Started", f"Auto clicker started! Hold '{hotkey}' in Minecraft.")

def start_party_spam():
    playername = simpledialog.askstring("Party Spammer", "Enter player name to invite:")
    if not playername:
        return
    delay = simpledialog.askinteger("Party Spammer", "Delay between spam (ms):", minvalue=1)
    if not delay:
        return
    threading.Thread(target=spam_party_invite, args=(playername, delay), daemon=True).start()
    messagebox.showinfo("Started", "Party spam started! Switch to Minecraft.")

def start_sneak_spam():
    delay = simpledialog.askinteger("Sneak Spammer", "Delay between sneak toggles (ms):", minvalue=1)
    if not delay:
        return
    threading.Thread(target=spam_sneak, args=(delay,), daemon=True).start()
    messagebox.showinfo("Started", "Sneak spam started! Switch to Minecraft.")

def start_private_message_spam():
    playername = simpledialog.askstring("Private Message Spammer", "Enter player name:")
    if not playername:
        return
    message = simpledialog.askstring("Private Message Spammer", "Enter message to send:")
    if not message:
        return
    delay = simpledialog.askinteger("Private Message Spammer", "Delay between messages (ms):", minvalue=1)
    if not delay:
        return
    threading.Thread(target=spam_private_message, args=(playername, message, delay), daemon=True).start()
    messagebox.showinfo("Started", "Private message spam started! Switch to Minecraft.")

def on_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Minecraft Helper")
root.geometry("300x350")

tk.Label(root, text="Minecraft Helper Menu", font=("Arial", 16)).pack(pady=10)

btn1 = tk.Button(root, text="1. Chat Spammer", width=25, command=start_spam_message)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="2. Auto Clicker", width=25, command=start_auto_clicker)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="3. Party Invite Spammer", width=25, command=start_party_spam)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="4. Sneak Spammer", width=25, command=start_sneak_spam)
btn4.pack(pady=5)

btn5 = tk.Button(root, text="5. Private Message Spammer", width=25, command=start_private_message_spam)
btn5.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=25, command=on_exit)
btn_exit.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
