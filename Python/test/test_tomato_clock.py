import pytest

from Python.model.Task import Task
from Python.model.TomatoTimerActions import TomatoTimerActions


class TestTomatoClock:
    task_1_input_list = [Task('test', 'test')]
    task_3_input_list = [Task('test', 'test'), Task('test', 'test'), Task('test', 'test')]
    task_4_input_list = [Task('test', 'test'), Task('test', 'test'), Task('test', 'test'), Task('test', 'test')]
    task_6_input_list = [Task('test1', 'test'), Task('test2', 'test'), Task('test3', 'test'), Task('test4', 'test'),
                         Task('test5', 'test'), Task('test6', 'test')]

