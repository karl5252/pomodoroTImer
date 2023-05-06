import time


class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._started_time = None

    @property
    def started_time(self):
        return self._started_time

    @started_time.setter
    def started_time(self, value):
        self._started_time = value

    def edit_task(self, new_task_name: str, new_task_description: str):
        self.name = new_task_name
        self.description = new_task_description

    def start_task(self):
        self.started_time = time.time()

    def get_elapsed_time(self):
        if self.started_time is None:
            return 0
        return int(time.time() - self.started_time)
