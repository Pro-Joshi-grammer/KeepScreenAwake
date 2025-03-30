# KeepScreenAwake

**About**:
This script prevents your laptop from hibernating or sleeping while running long installations, downloads, or any process that shouldn't be interrupted.

**Why**:
I encountered a problem while coding late at night. I wanted to get some sleep, but I had a list of packages to install along with their dependencies. The issue was that my laptop would hibernate if I didn’t move the cursor, causing the background installation to stop.

To solve this, I created a Python script using the pyautogui module. This script automatically moves the cursor 1 pixels to the left for 25 seconds and then returns it to its original position. You can easily adjust the timing by modifying the interval variable.

Additionally, the keepawake function has a parameter for hours, which is set to three by default, but you can change it to suit your needs.

There are **two versions** of this script:  
1. **Mouse Movement Method (Uses `pyautogui`)**  ==> Mouse_awake.py
2. **Keyboard Simulation Method (Uses `keyboard`)**  ==>Keyboard_awake.py

Credits:**Made with the help of ChatGPT.**  

---

## Method 1: Mouse Movement (PyAutoGUI)  
This version moves the mouse slightly **every 25 seconds** to trick the system into thinking you're active.  
Dependencies: PyAutoGUI Module

## Method 2:Keyboard Simulation (Keyboard Module)
Instead of moving the mouse, this version presses Shift, Control, Caps Lock, and Alt in rotation every 25 seconds. This keeps the system awake without affecting your work.
The shift control CapsLock and Alt are added in consideration that it doesent effect the installation of packages.If any of the button interrupts your work or causes disturbencies you can update it in the list keys.

Dependencies: Keyboard Module



People working in companies can use as your afk time is monitored 😉





![SoGoodWinkGIF](https://github.com/user-attachments/assets/4e006bf5-5720-4eb4-9411-cc501c057cd9)


**NOTE**: This script will not work in web browsers (online compilers).
          pyautogui and keyboard require access to the system's input devices, which online Python compilers do not provide due to security restrictions.
          Run this script locally on your PC for it to work.

This project is licensed under the GNU General Public License v3.0 (GPLv3).
See the LICENSE file for details.





