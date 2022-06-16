import os
import sys

from Python.model.clock import Clock
from Python.model.writer import Loader


class TomatoMain():
    ROOT_DIR = os.path.dirname(
        sys.modules['__main__'].__file__)  # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):

        self.task_list = list()
        self.message = "Hello! Welcome to POMODORO TIMER \n -----------MAIN MENU----------- \n  " \
                       "1. {A}DD TASK \n 2. {L}OAD TASKS \n 3. {S}TART \n" \
                       " 4. SA{V}E TASKS \n 5. {M}ODIFY TASKS \n 6. {E}XIT \n CURRENT TASK LIST: \n"

        self.interaction()

    def interaction(self):

        user_input = ''
        while user_input != 'e':
            user_input = self.get_user_choice()

            if user_input == 'a' or user_input == 'A':
                self.update_task_list()
            elif user_input == 'l' or user_input == 'L':
                self.task_list = Loader.read()
            elif user_input == 's' or user_input == 'S':
                Clock(self.task_list)
            elif user_input == 'v' or user_input == 'V':
                Loader.write(self.task_list)
            elif user_input == 'm' or user_input == 'M':
                self.modify_task_list()
            elif user_input == 'e' or user_input == 'E':
                print("thank you")
                break
            else:
                print("invalid command\n")

    def get_user_choice(self):
        # Let users know what they can do.
        print(self.message)
        self.print_task_list()
        return input("Pick your poison\n")

    def update_task_list(self):
        task_name = input("Please state briefly name of your task: \n")
        task_description = input("Please briefly describe your task: \n")
        self.task_list.append(tuple((str(task_name), str(task_description))))
        return self.task_list

    def print_task_list(self):
        for count, task in enumerate(self.task_list, 1):
            print(f'#{count}: {task}')

    def modify_task_list(self):
        task_list_length = len(self.task_list)
        self.print_task_list()
        task_to_change = input()
        if task_to_change.isnumeric():
            task_index = int(task_to_change)
            print(f'your choice: {task_index}')
            if task_index > task_list_length:
                print('no such task')
            elif task_index < 0:
                print('task number must be zero or positive')
            elif task_index <= task_list_length:
                task = self.task_list[task_index - 1]
                print(task)
                new_task_name = input("Please state briefly name of your task: \n")
                new_task_description = input("Please briefly describe your task: \n")
                new_task = tuple((new_task_name, new_task_description))
                self.task_list[task_index - 1] = new_task

