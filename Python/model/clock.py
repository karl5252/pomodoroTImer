import os
import sys
import time

from plyer import notification
from timeit import default_timer as timer

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)


class Clock:
    def __init__(self, task_list):
        self.task_list = task_list
        self.task_count = 0

        self.task_time = 1800  # 30 minutes
        self.long_break = 900  # 15 minutes
        self.short_break = 300  # 5 minutes
        self.preparation_interval = 5
        self.special_break_limit = self.task_time  # tops long as task

        self.pomodoro_clock()

    def pomodoro_clock(self):
        for task in self.task_list:
            self.task_count += 1
        time.sleep(2)  # delay
        count = 0

        while count < self.task_count:
            time_elapsed = 0

            notification.notify(
                title="To work!",
                message=f"Focusing now on {self.task_list[count][0]} \n {self.task_list[count][1]}",
                app_icon=f'{ROOT_DIR}\\tomato.ico',
                timeout=self.preparation_interval
            )
            count += 1

            # time.sleep(self.task_time)  # 1800
            self.timer(self.task_time)
            if count % 4 == 0:
                notification.notify(
                    title="Good work!",
                    message="Take a 15 minute break and go grab a coffee or refill water bottle!\n"
                            "Remember to stay hydrated!"
                            f" You have completed {count} pomodoros so far",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=self.preparation_interval
                )
                self.timer(self.long_break)  # 900
            else:
                notification.notify(
                    title="Good work!",
                    message=f" Take a 5 minute break and stretch! You have completed pomodoro {count} "
                            f"out of {self.task_count}",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=self.preparation_interval
                )
                self.timer(self.short_break)  # 300

        notification.notify(
            title="Done for today(?)",
            message=f"no more tasks on the list. Today you have done {count} tasks!",
            app_icon=f'{ROOT_DIR}\\tomato.ico',
            timeout=self.preparation_interval)

    def get_user_choice(self):
        return input("press {b} to get break press {p} to stop \n {r} to resume paused {s} to skip\n")

    def timer(self, task_time):
        time_elapsed = 0
        special_break_time = 0
        user_input = self.get_user_choice()

        while time_elapsed < task_time or user_input != 'q' or user_input != 'Q':
            time_elapsed = timer()

            if user_input == 'B' or user_input == 'b':
                time_spent = time_elapsed
                notification.notify(
                    title="Requested a break!",
                    message=f"Take additional 5 minute break and stretch!",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=self.preparation_interval
                )
                while special_break_time < self.short_break:
                    special_break_time = timer()
                time_elapsed = time_spent

            elif user_input == 'P' or user_input == 'p':
                time_spent = time_elapsed
                notification.notify(
                    title="Requested a pause!",
                    message=f"Pause?! A PAUSE?! There is so much to do!",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=self.task_time
                )
                while user_input != 'R' or user_input != 'r':
                    temp_input = input()
                    print('press R to resume')
                    time.sleep(1)
                    if temp_input == 'R' or temp_input == 'r':
                        break
                time_elapsed = time_spent
                notification.notify(
                    title="Got back to work!",
                    message=f"Finally! Back to senses!",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=self.preparation_interval
                )
            elif user_input == 'S' or user_input == 's':
                print('skipping task...')
                notification.notify(
                    title="Task skipped",
                    message=f"SKIPPED A TASK",
                    app_icon=f'{ROOT_DIR}\\tomato.ico',
                    timeout=self.preparation_interval
                )
                break
            elif user_input == 'Q' or user_input == 'q':
                print('exiting')
                exit(0)
            else:
                print('invalid request')



