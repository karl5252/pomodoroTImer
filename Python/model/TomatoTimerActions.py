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
            #elapsed_time = self.task_list[current_task].get_elapsed_time()
            #print(f'Task {current_task + 1} elapsed time: {elapsed_time} seconds')

            #TaskController(TASK_TIME, current_task).task_start()
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

# def task_controller(self, task_time):
#     time_elapsed = 0
#     special_break_time = 0
#     user_input = self.get_user_choice()
#
#     while time_elapsed < task_time or user_input != 'q' or user_input != 'Q':
#         time_elapsed = timer()
#
#         if user_input == 'B' or user_input == 'b':
#             self.print_timestamp()
#             time_spent = time_elapsed
#             print('requested 5 minute break')
#             notification.notify(
#                 title="Requested a break!",
#                 message=f"Take additional 5 minute break and stretch!",
#                 app_icon=f'{ROOT_DIR}\\tomato.ico',
#                 timeout=self.preparation_interval
#             )
#             while special_break_time < self.short_break:
#                 special_break_time = timer()
#             time_elapsed = time_spent
#
#         elif user_input == 'P' or user_input == 'p':
#             self.print_timestamp()
#             time_spent = time_elapsed
#             notification.notify(
#                 title="Requested a pause!",
#                 message=f"Pause?! A PAUSE?! There is so much to do!",
#                 app_icon=f'{ROOT_DIR}\\tomato.ico',
#                 timeout=self.task_time
#             )
#             while user_input != 'R' or user_input != 'r':
#                 temp_input = input()
#                 print('press R to resume')
#                 time.sleep(1)
#                 if temp_input == 'R' or temp_input == 'r':
#                     break
#             time_elapsed = time_spent
#             notification.notify(
#                 title="Got back to work!",
#                 message=f"Finally! Back to senses!",
#                 app_icon=f'{ROOT_DIR}\\tomato.ico',
#                 timeout=self.preparation_interval
#             )
#         elif user_input == 'S' or user_input == 's':
#             print('skipping task...')
#             notification.notify(
#                 title="Task skipped",
#                 message=f"SKIPPED A TASK",
#                 app_icon=f'{ROOT_DIR}\\tomato.ico',
#                 timeout=self.preparation_interval
#             )
#             break
#         elif user_input == 'E' or user_input == 'e':
#             task_from_list = task_manager.get_task(self.task_list)[0]
#             task_index = task_manager.get_task(self.task_list)[1]
#             print(f'extending task {task_from_list} by additional slot')
#
#             self.task_list.insert(task_from_list, task_index)
#         elif user_input == 'Q' or user_input == 'q':
#             print('exiting')
#             exit(0)
#         else:
#             print('invalid request')
