class TaskManager():

    def __init__(self):
        self.modifcation_menu_msg = '==MODIFICATION MENU== \n choose option'


    def print_task_list(self, task_list):
        for count, task in enumerate(task_list, 1):
            print(f'#{count}: {task}')

    def update_task_list(self, task_list):
        task_name = input("Please state briefly name of your task: \n")
        task_description = input("Please briefly describe your task: \n")
        task_list.append(tuple((str(task_name), str(task_description))))
        return task_list

    def modify_task_list(self, task_list):
        print(self.modifcation_menu_msg)
        option = input('Do you want to \n 1. DELETE TASK \n 2. WIPE \n 3. MODIFY \n')

        if option.isnumeric():
            if int(option) == 1:
                task_index = self.get_task(task_list)[1]
                print(f'deleting {task_list[task_index]}')
                del task_list[task_index]
            elif int(option) == 2:
                task_list.clear()
                print('list of tasks was wiped')
            elif int(option) == 3:
                task_index = self.get_task(task_list)[1]
                new_task_name = input("Please state briefly name of your task: \n")
                new_task_description = input("Please briefly describe your task: \n")
                new_task = tuple((new_task_name, new_task_description))
                task_list[task_index] = new_task
            else:
                print('wrong option')
        else:
            print('option needs to be numeric!')

    def get_task(self, task_list):
        task_list_length = len(task_list)
        task_to_change = input(f"Choose task number from the list \n {self.print_task_list(task_list)}")
        if task_to_change.isnumeric():
            task_index = int(task_to_change)
            print(f'your choice: {task_index}')
            if task_index > task_list_length:
                print('no such task')
            elif task_index < 0:
                print('task number must be zero or positive')
            elif task_index <= task_list_length:
                task_index -= task_index
                task = task_list[task_index]
                return task, task_index
        else:
            print('invalid option')
            return 0



