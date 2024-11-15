import tkinter as tk

def add_task():
    task = task_entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox_start.insert(tk.END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца


def delete_task():
    selected_task = task_listBox_start.curselection() # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox_start.delete(selected_task) # удаляем выбранный элемент из списка


def mark_task():
    selected_task = task_listBox_start.curselection()
    if selected_task:
        task_listBox_start.itemconfig(selected_task, bg="slate blue")  # с помощью функции **itemconfig** выполненная задача изменит цвет заливки

class DragDropListbox(tk.Listbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Button-1>', self.on_click)
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_release)
        self.dragged_item_index = None
        self.start_x = 0
        self.start_y = 0
        self.dragging_label = None

    def on_click(self, event):
        # Получаем индекс нажатого элемента
        self.dragged_item_index = self.nearest(event.y)
        self.start_x = event.x
        self.start_y = event.y


    def on_drag(self, event):
        x, y = root.winfo_pointerxy()
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        relative_x = x - root_x
        relative_y = y - root_y
        if self.dragged_item_index is not None:
            # Создаем или обновляем метку для перетаскиваемого элемента
            item_text = self.get(self.dragged_item_index)
            if not self.dragging_label:
                self.dragging_label = tk.Label(self.master, text=item_text, bg='lightyellow')
                self.dragging_label.place(x=relative_x+5, y=relative_y+5, anchor='nw')
            else:
                self.dragging_label.place(x=relative_x+5, y=relative_y+5, anchor='nw')
        # Перетаскивание не реализовано, просто используем события для управления
        #self.select_clear(0, tk.END)

    def on_release(self, event):
        if self.dragged_item_index is not None:

            # Получаем текст перетаскиваемого элемента
            item_text = self.get(self.dragged_item_index)

            # Проверяем, был ли элемент отпущен в другом listbox
            widget = event.widget
            target = widget.winfo_containing(event.x_root, event.y_root)
            if isinstance(target, DragDropListbox) and target is not widget:
                # Добавляем элемент в целевой listbox
                target.insert(tk.END, item_text)
                # Удаляем элемент из текущего listbox
                self.delete(self.dragged_item_index)

            # Убираем метку
            if self.dragging_label:
                self.dragging_label.destroy()
                self.dragging_label = None

            self.dragged_item_index = None



root = tk.Tk()
root.title("Task list")

root.configure(background="alice blue")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="DeepPink1")

task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="HotPink")
text2.pack(pady=5)


text4 = tk.Label(root, text="Новые задачи:", bg="LightCyan1")
text4.pack(side=tk.LEFT)

text5 = tk.Label(root, text="Выполненные задачи", bg="LightGreen")
text5.pack(side=tk.RIGHT)


task_listBox_start = DragDropListbox(root, height=10, width=50, bg="LightCyan1")
task_listBox_done = DragDropListbox(root, height=10, width=50, bg="LightGreen")

task_listBox_start.pack(side=tk.LEFT, padx=10, pady=10)
task_listBox_done.pack(side=tk.RIGHT, padx=10, pady=10)



root.mainloop()