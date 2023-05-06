import os
import sys
import time

from plyer import notification

from Python.model.Constants import TASK_TIME, SHORT_BREAK, PREP_INTERVAL, LONG_BREAK
from Python.model.TaskController import TaskController

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)


class TomatoTimerActions:
    def __init__(self, task_list):
        self.task_list = task_list
        self.task_count = len(task_list)
        self.special_break_limit = TASK_TIME  # tops long as task

        self.pomodoro_clock()

    def pomodoro_clock(self):
        current_task = 0

        while current_task < self.task_count:
            notification.notify(
                title="To work!",
                message=f"Focusing now on {self.task_list[current_task].name} \n"
                        f" {self.task_list[current_task].description}",
                app_icon=f'{ROOT_DIR}\\tomato.ico',
                timeout=PREP_INTERVAL
            )

            self.task_list[current_task].start_task()
            TaskController(TASK_TIME, self.task_list[current_task]).task_start()
            time.sleep(TASK_TIME)

            time.sleep(TASK_TIME)
            print(f'current task number is {self.task_list[current_task]}')
            current_task += 1

            if current_task % 4 == 0:
                notification.notify(
                    title="Good work!",
                    message="Take a 15 minute break and go grab a coffee or refill water bottle!\n"
                            "Remember to stay hydrated!"
                            f" You have completed {current_task} pomodoros so far",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=PREP_INTERVAL
                )
                TaskController(LONG_BREAK, self.task_list[current_task - 1]).task_start()  # 900
                time.sleep(LONG_BREAK)
            else:
                notification.notify(
                    title="Good work!",
                    message=f" Take a 5 minute break and stretch! You have completed pomodoro {current_task} "
                            f"out of {self.task_count}",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=PREP_INTERVAL
                )
                TaskController(SHORT_BREAK, self.task_list[current_task - 1]).task_start()  # 300
                time.sleep(SHORT_BREAK)

        notification.notify(
            title="Done for today(?)",
            message=f"no more tasks on the list. Today you have done {current_task} tasks!",
            app_icon=f'{ROOT_DIR}\\tomato.ico',
            timeout=PREP_INTERVAL)
        return self

