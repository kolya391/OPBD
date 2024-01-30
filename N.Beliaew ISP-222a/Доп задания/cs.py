import tkinter as tk
from PIL import Image, ImageTk

def resize_image():
    new_width = int(width_entry.get())
    new_height = int(height_entry.get())
    resized_image = image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=photo)
    image_label.image = photo

def rotate_image():
    rotated_image = image.rotate(90)
    photo = ImageTk.PhotoImage(rotated_image)
    image_label.configure(image=photo)
    image_label.image = photo

window = tk.Tk()
image = Image.open("tiger.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.pack()
width_label = tk.Label(window, text="Ширина:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()
height_label = tk.Label(window, text="Высота:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()
resize_button = tk.Button(window, text="Изменить размер", command=resize_image)
resize_button.pack()
rotate_button = tk.Button(window, text="Повернуть", command=rotate_image)
rotate_button.pack()
window.mainloop()