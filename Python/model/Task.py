class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def edit_task(self, new_task_name: str, new_task_description: str):
        self.name = new_task_name
        self.description = new_task_description
