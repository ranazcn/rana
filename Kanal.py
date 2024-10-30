import tkinter as tk
import webbrowser

def open_video():
    url = "https://www.youtube.com/watch?v=vQJVbrn-l8U"
    webbrowser.open(url)


root = tk.Tk()
root.title("Mesaj ve Video Açıcı")


label = tk.Label(root, text="Dünyanın en iyi kanalı Dr. Akadal", font=("Helvetica", 16))
label.pack(pady=20)


button = tk.Button(root, text="Videoyu Aç", command=open_video, font=("Helvetica", 14))
button.pack(pady=10)


root.mainloop()
