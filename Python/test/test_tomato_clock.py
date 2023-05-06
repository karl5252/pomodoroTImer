import pytest

from Python.model.Task import Task
from Python.model.TomatoTimerActions import TomatoTimerActions


class TestTomatoClock:
    task_1_input_list = [Task('test', 'test')]
    task_3_input_list = [Task('test', 'test'), Task('test', 'test'), Task('test', 'test')]
    task_4_input_list = [Task('test', 'test'), Task('test', 'test'), Task('test', 'test'), Task('test', 'test')]
    task_6_input_list = [Task('test1', 'test'), Task('test2', 'test'), Task('test3', 'test'), Task('test4', 'test'),
                         Task('test5', 'test'), Task('test6', 'test')]

    def test_actions_count_increase_one_task(self):
        clock = TomatoTimerActions(self.task_1_input_list)
        clock.TomatoActionsCounter()

        assert clock.task_count == 1

    def test_actions_count_increase_n_tasks(self):
        clock = TomatoTimerActions(self.task_4_input_list)
        clock.TomatoActionsCounter()

        assert clock.task_count == 4

    def test_short_interval(self):
        clock = TomatoTimerActions(self.task_3_input_list)
        break_type = clock.TimerBreakType()

        assert False == break_type

    def test_long_interval(self):
        clock = TomatoTimerActions(self.task_4_input_list)
        break_type = clock.TimerBreakType()

        assert break_type
