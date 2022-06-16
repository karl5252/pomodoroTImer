import os
import sys

from Python.model.clock import Clock
from Python.model.task_manager import TaskManager
from Python.model.writer import Loader


class TomatoMain():
    ROOT_DIR = os.path.dirname(
        sys.modules['__main__'].__file__)  # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):

        self.task_list = list()
        self.message = "Hello! Welcome to POMODORO TIMER \n -----------MAIN MENU----------- \n" \
                       "1. {A}DD TASK \n 2. {L}OAD TASKS \n 3. {S}TART \n" \
                       "4. SA{V}E TASKS \n 5. {M}ODIFY TASKS \n 6. {E}XIT \n CURRENT TASK LIST: \n"
        self.task_manager = TaskManager()
        self.interaction()

    def interaction(self):

        user_input = ''
        while user_input != 'e':
            user_input = self.get_user_choice()

            if user_input == 'a' or user_input == 'A':
                self.task_manager.update_task_list(self.task_list)
            elif user_input == 'l' or user_input == 'L':
                self.task_list = Loader.read()
            elif user_input == 's' or user_input == 'S':
                Clock(self.task_list)
            elif user_input == 'v' or user_input == 'V':
                Loader.write(self.task_list)
            elif user_input == 'm' or user_input == 'M':
                self.task_manager.modify_task_list(self.task_list)
            elif user_input == 'e' or user_input == 'E':
                print("thank you")
                break
            else:
                print("invalid command\n")

    def get_user_choice(self):
        # Let users know what they can do.
        print(self.message)
        self.task_manager.print_task_list(self.task_list)
        return input("Pick your poison\n")


