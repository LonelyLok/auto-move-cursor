import tkinter as tk
import pyautogui
import threading

auto_move_active = False

def start_action():
    global auto_move_active
    auto_move_active = True
    def auto_move():
        while auto_move_active:
            x, y = pyautogui.position()
            pyautogui.moveTo(x+100, y+100, duration=0.5)
            pyautogui.moveTo(x, y, duration=0.5)
    threading.Thread(target=auto_move, daemon=True).start()

def stop_action():
    global auto_move_active
    auto_move_active = False

def on_key_press(event):
    print(f"Key pressed: {event.char}")
    if(event.char == 'q'):
        #stop moving mouse
        stop_action()

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Auto move cursor app")

    root.tk_setPalette(background='#2B2B2B', foreground='#FFFFFF')
    root.bind('<Key>', on_key_press)

    # Set the window size
    root.geometry("400x300")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    # Create a label with "Hello, World!" text
    label = tk.Label(frame, text="Auto move cursor", font=("Arial", 16))
    label.pack()

    start_button = tk.Button(frame, text="Start", command=start_action)
    start_button.pack(pady=10)

    stop_message = tk.Label(frame, text="Press 'q' to stop", font=("Arial", 12))
    stop_message.pack()

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()