# Менеджер задач


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Некорректный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Сделать домашнее задание", "2023-10-10")
    manager.add_task("Купить продукты", "2023-10-05")

    print("Список всех задач:")
    manager.display_tasks()

    print("\nОтметим первую задачу как выполненную:")
    manager.mark_task_as_completed(0)

    print("\nСписок всех задач после изменения статуса:")
    manager.display_tasks()

    print("\nТекущие (не выполненные) задачи:")
    current_tasks = manager.get_current_tasks()
    for task in current_tasks:
        print(task)