import pickle


class Loader:
    def __init__(self):
        pass

    @classmethod
    def write(cls, task_list):
        with open('task_list', 'wb') as fp:
            pickle.dump(task_list, fp)
        print('Data saved!')

    @classmethod
    def read(cls):
        print('loading data...\n')
        with open('task_list', 'rb') as fp:
            data = pickle.load(fp)
        return data
