import os
import sys

from Python.model.TomatoTimerActions import TomatoTimerActions
from Python.model.TaskManager import TaskManager, update_task_list, print_task_list
from Python.model.Writer import Loader


class TomatoMain:

    ROOT_DIR = os.path.dirname(
        sys.modules['__main__'].__file__)  # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):

        self.task_list = list()
        self.message = "Hello! Welcome to POMODORO TIMER \n -----------MAIN MENU----------- \n" \
                       " 1. {A}DD TASK \n 2. {L}OAD TASKS \n 3. {S}TART \n" \
                       " 4. SA{V}E TASKS \n 5. {M}ODIFY TASKS \n 6. {E}XIT \n CURRENT TASK LIST: \n"
        self.task_manager = TaskManager()
        self.interaction()

    def interaction(self):
        while True:
            user_input = self.get_user_choice().upper()
            options = {
                'A': lambda: update_task_list(self.task_list),
                'L': lambda: setattr(self, 'task_list', Loader.read()),
                'S': lambda: TomatoTimerActions(self.task_list),
                'V': lambda: Loader.write(self.task_list),
                'M': lambda: self.task_manager.modify_task_list(self.task_list),
                'E': lambda: exit(0)
            }
            options.get(user_input, lambda: print('Invalid command!'))()

    def get_user_choice(self):
        # Let users know what they can do.
        print(self.message)
        print_task_list(self.task_list)
        return input("Pick your poison\n")

    @property
    def get_task_list(self):
        return self.task_list


