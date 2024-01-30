import tkinter as tk


class AnimationApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.x = 200
        self.y = 200
        self.speed = 2
        self.master.bind('<KeyPress>', self.on_key_press)
        self.draw_object()

    def draw_object(self):
        self.canvas.delete('object')
        self.canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill='blue', tags='object')

    def on_key_press(self, event):

        if event.keysym == 'Up':
            self.move_object(0, -self.speed)
        elif event.keysym == 'Down':
            self.move_object(0, self.speed)
        elif event.keysym == 'Left':
            self.move_object(-self.speed, 0)
        elif event.keysym == 'Right':
            self.move_object(self.speed, 0)

    def move_object(self, dx, dy):

        new_x = self.x + dx
        new_y = self.y + dy
        if new_x > 20 and new_x < 380:
            self.x = new_x
        if new_y > 20 and new_y < 380:
            self.y = new_y
        self.draw_object()

    def increase_speed(self):

        self.speed += 1

    def decrease_speed(self):

        if self.speed > 1:
            self.speed -= 1

root = tk.Tk()
app = AnimationApp(root)
increase_button = tk.Button(root, text="Увеличить скорость", command=app.increase_speed)
increase_button.pack()
decrease_button = tk.Button(root, text="Уменьшить скорость", command=app.decrease_speed)
decrease_button.pack()
root.mainloop()