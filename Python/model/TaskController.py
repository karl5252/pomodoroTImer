from threading import Timer
import time
import datetime


class TaskController:
    def __init__(self, timeout, current_task):
        self.current_task = current_task
        self.timer = None
        self.start_time = 0
        self.cancel_time = 0
        self.pause_time = 0
        self.timeout = timeout
        self.task_menu_message = f'=======RUNNING TASK MENU=======\n' \
                                 f'CONTROLS:\n' \
                                 f'P - to stop\n' \
                                 f'R - to resume paused\n' \
                                 f'S - to skip current task\n' \
                                 f'T - to print remaining time\n'
        self.started = True
        self.task_start()

    def get_current_timestamp(self):
        ct = datetime.datetime.now()
        print("task ends at: ", ct)

    def task_cancel(self):
        if self.timer and self.timer.is_alive():
            self.timer.cancel()
            print('task canceled')
        else:
            print('no task is currently running')

    def task_start(self):
        if not self.timer or not self.timer.is_alive():
            self.timer = Timer(self.timeout, self.get_current_timestamp)
            self.start_time = time.time()
            self.timer.start()
            print('task started')
            self.interaction()
        else:
            print('a task is already running!')

    def task_pause(self):
        if self.timer and self.timer.is_alive():
            self.timer.cancel()
            self.pause_time = self.task_get_remaining_time()
            print('task paused')
            return self.pause_time
        else:
            print('no task is currently running')
            return 0

    def task_resume(self):
        if self.started:
            print('Task already started, use "P" to pause')
        else:
            self.timeout = self.task_get_remaining_time_int()
            self.timer = Timer(self.timeout, self.get_current_timestamp)
            self.start_time = time.time()
            self.timer.start()
            print('task resumed')

    def task_get_remaining_time_int(self) -> int:
        if self.timer is None or not self.timer.is_alive():
            return 0
        else:
            elapsed_time = self.current_task.get_elapsed_time()
            remaining_time = self.timeout - elapsed_time + self.pause_time
            return remaining_time if remaining_time > 0 else 0

    def task_get_remaining_time(self) -> str:
        if self.timer is None or not self.timer.is_alive():
            return "0 seconds"
        else:
            elapsed_time = self.current_task.get_elapsed_time()
            remaining_time = self.timeout - elapsed_time + self.pause_time
            if remaining_time <= 0:
                return "0 seconds"
            else:
                minutes, seconds = divmod(remaining_time, 60)
                hours, minutes = divmod(minutes, 60)
                time_str = f"{minutes} minutes and {seconds} seconds"
                if hours > 0:
                    time_str = f"{hours} hours, " + time_str
                return time_str

    def __del__(self):
        self.task_cancel()

    def interaction(self):
        user_input = ''
        while user_input != 'q' or user_input != 'Q':
            user_input = self.get_user_choice()

            if user_input == 'p' or user_input == 'P':
                print('task paused')
                self.task_pause()

            elif user_input == 'r' or user_input == 'R':
                print('task resumed')
                self.task_resume()

            elif user_input == 's' or user_input == 'S':
                print('task canceled')
                self.task_cancel()
                return 0
            elif user_input == 't' or user_input == 'T':
                print("time remaining: \n")
                print(self.task_get_remaining_time())
            elif user_input == 'q' or user_input == 'Q':
                print("Quitting \n")
                self.task_cancel()
                exit(0)
            else:
                print("invalid command\n")

    def get_user_choice(self):
        # Let users know what they can do.
        print(self.task_menu_message)

        return input("...\n")
