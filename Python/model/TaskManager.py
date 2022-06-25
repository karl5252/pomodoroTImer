from Python.model.Task import Task


def print_task_list(task_list):
    for count, task in enumerate(task_list, 1):
        print(f'#{count}: {task.name}')


def update_task_list(task_list):
    task_name = input("Please state briefly name of your task: \n")
    task_description = input("Please briefly describe your task: \n")
    task_list.append(Task(task_name, task_description))
    return task_list


def extend_task(task_list):
    task_from_list = get_task(task_list)[0]
    task_index = get_task(task_list)[1]
    task_list.insert(task_from_list, task_index + 1)


def get_task(task_list):
    task_list_length = len(task_list)
    task_to_change = input(f"Choose task number from the list \n {print_task_list(task_list)}")
    if task_to_change.isnumeric():
        task_index = int(task_to_change)
        print(f'your choice: {task_index}')
        if task_index > task_list_length:
            print('no such task')
        elif task_index < 0:
            print('task number must be zero or positive')
        elif task_index <= task_list_length:
            task_index -= task_index
            task = task_list[task_index]
            return task, task_index
    else:
        print('invalid option')
        return 0


class TaskManager:

    def __init__(self):
        self.task_list = list()
        self.modification_menu_msg = '==MODIFICATION MENU== \n choose option'

    def modify_task_list(self, task_list):
        print(self.modification_menu_msg)
        option = input('Do you want to \n 1. DELETE TASK \n 2. WIPE \n 3. MODIFY \n')

        if option.isnumeric():
            if int(option) == 1:
                task_index = get_task(self.task_list)[1]
                print(f'deleting {self.task_list[task_index]}')
                del self.task_list[task_index]
            elif int(option) == 2:
                self.task_list.clear()
                print('list of tasks was wiped')
            elif int(option) == 3:
                task_from_list = get_task(self.task_list)[0]
                task_index = get_task(self.task_list)[1]
                new_task_name = input("Please state briefly name of your task: \n")
                new_task_description = input("Please briefly describe your task: \n")
                task_from_list.edit_task(new_task_name, new_task_description)
                self.task_list[task_index] = task_from_list
            else:
                print('wrong option')
        else:
            print('option needs to be numeric!')


    # @task_list.setter
    # def task_list(self, value):
    #     self._task_list = value
