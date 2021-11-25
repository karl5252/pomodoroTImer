import os
import sys
import time
from plyer import notification
'''tomato icon from https://www.flaticon.com/authors/justicon'''
count = 0
print("The pomodoro timer has started, start working!")
task_list = {}
line_count = 0
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)#os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    with open(f"{ROOT_DIR}\\taskList.txt") as list_of_tasks:
        for line in list_of_tasks:
            line_count += 1
            (key, val) = line.split('#')
            task_list[int(key)] = val
    time.sleep(2)  # delay

    while count < line_count:

        count += 1
        notification.notify(
            title="To work!",
            message=f"Focusing now on {task_list[count]}",
            app_icon=f'{ROOT_DIR}\\tomato.ico',
            timeout=10
        )
        time.sleep(1800)  # 1800
        if count % 4 == 0:
            notification.notify(
                title="Good work!",
                message="Take a 15 minute break and go grab a coffee or refill water bottle!\n"
                        "Remember to stay hydrated!"
                        f" You have completed {count} pomodoros so far",
                app_icon=f'{ROOT_DIR}\\tomato.ico',
                timeout=10
            )
            time.sleep(900)  # 900
        else:
            notification.notify(
                title="Good work!",
                message=f" Take a 5 minute break and stretch! You have completed pomodoro {count} out of {line_count}",
                app_icon=f'{ROOT_DIR}\\tomato.ico',
                timeout=10
            )
            time.sleep(300)  # 300

    notification.notify(
        title="Done for today(?)",
        message=f"no more tasks on the list. Today you have done {count} tasks!",
        app_icon=f'{ROOT_DIR}\\tomato.ico',
        timeout=10)
