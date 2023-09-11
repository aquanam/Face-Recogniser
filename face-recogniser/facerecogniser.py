#! /usr/bin/env python3

"""
=================================================
|                                               |
|               Face recogniser                 |
|          Made by aquanam on GitHub            |
|            --Written in Python--              |
|                                               |
|            Using Python's OpenCV              |
|     Don't hesitate if you want to commit!     |
|                                               |
|          Make sure you have python3           |
|         and python3-opencv installed.         |
|                                               |
|                   Thanks!                     |
|                                               |
=================================================
"""

import cv2, os, sys
from tkinter import *
from tkinter import messagebox

if os.path.isfile("msgbox-enable.txt") != True:
    msgbox_enable_txt = open("msgbox-enable.txt", "w")
    msgbox_enable_txt.write("1")
    msgbox_enable_txt.close()

if len(sys.argv) >= 3:
    print("\33[0;49;91mArguments are greater or equal to 3.")
    exit(1)

if len(sys.argv) == 2:
    if sys.argv[1] == "--disable-messageboxes":
        msgbox_enable_txt = open("msgbox-enable.txt", "w")
        msgbox_enable_txt.write("0")
        msgbox_enable_txt.close()
    if sys.argv[1] == "--enable-messageboxes":
        msgbox_enable_txt = open("msgbox-enable.txt", "w")
        msgbox_enable_txt.write("1")
        msgbox_enable_txt.close()
    print("Success.")
    exit(0)

msgbox_enable_txt = open("msgbox-enable.txt", "r")
msgbox_enabled = msgbox_enable_txt.read()
msgbox_enable_txt.close()

if msgbox_enabled != "0" and msgbox_enabled != "1":
    print(f"\33[0;49;91mInvalid value in msgbox-enable.txt. It can only be 0(no) or 1(yes) not {msgbox_enabled}.")
    exit(1)

if msgbox_enabled == "1":
    print("\33[0;49;37mFace recogniser - Messagebox enabled")
else:
    print("\33[0;49;37mFace recogniser - Messagebox disabled")
print("\33[4;49;37mDo './facerecogniser.py --disable-messageboxes' to disable messageboxes (includes error ones).")
print("\33[4;49;37mDo './facerecogniser.py --enable-messageboxes' to enable messageboxes.")
print("\33[0;49;91m(Face recognition may not always be accurate)")

if msgbox_enabled == "1":
    messagebox.showinfo("Face recogniser", "Face recogniser - Made by aquanam on GitHub\nFace recogniser v2 coming soon.")
    messagebox.showinfo("Face recogniser", "Read console about disabling/enabling messageboxes.")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("\33[4;49;91mError: Could not open camera - Cap is not opened")
    if msgbox_enabled == "1":
        messagebox.showerror("Face recogniser", "Could not open camera - Cap is not opened")
    exit(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("\33[4;49;91mError: Could not read frame - Variable 'ret' is not true")
        if msgbox_enabled == "1":
            messagebox.showerror("Face recogniser", "Could not read frame - Variable 'ret' is not true")
        exit(1)
    
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'X: {x}, Y: {y}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Face recogniser", frame)
    
    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty("Face recogniser", cv2.WND_PROP_VISIBLE) < 1:
        print("\33[0;49;37mExiting...")
        break

cap.release()
cv2.destroyAllWindows()
