# PRODIGY_CS_04

# Simple Keylogger

# Overview
This is a basic keylogger program written in Python. The program listens for keyboard events, logs every keystroke (letters, numbers, and special keys), and saves them to a file named keylog.txt. The program will continue logging keystrokes until the Esc key is pressed, at which point the logging will stop.

# Disclaimer: 
This project is for educational purposes only. Unauthorized use of keyloggers is illegal. Ensure that you have explicit permission before running this program on any machine that isn't your own.

# Requirements
Python 3.x
pynput library

You can install the necessary library by running:
    pip install pynput

# How It Works
Log File: The program logs all keystrokes in a file called keylog.txt.

Key Press Events: When a key is pressed, it logs either the character (for letters and numbers) or the key name (for special keys such as Shift, Ctrl, etc.).

Stopping the Program: The keylogger runs continuously until the Esc key is pressed, at which point it will stop logging and exit.

# How to Use
Clone or Download the Project:
    git clone <repository_url>

Run the Keylogger: Run the program using Python:
    python keylogger.py

Check the Log File: After running the keylogger, open keylog.txt to see the logged keystrokes.

Stop the Keylogger: Press the Esc key to stop the keylogger.

# Ethical and Legal Notice
This program is designed for educational purposes only. Use it responsibly. Do not use this program to monitor other people’s devices without their consent. Unauthorized monitoring may be illegal in your jurisdiction.
