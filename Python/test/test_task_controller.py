import time

import pytest

from Python.model.Task import Task
from Python.model.TaskController import TaskController


@pytest.fixture
def task_controller():
    task = Task("test", "test description")
    return TaskController(5, None)


def test_task_start(task_controller):
    task_controller.task_start()
    assert task_controller.timer.is_alive() == True


def test_task_pause(task_controller):
    task_controller.task_start()
    time.sleep(1)
    pause_time = task_controller.task_pause()
    assert task_controller.timer.is_alive() == False
    assert pause_time > 0


def test_task_resume(task_controller):
    task_controller.task_start()
    time.sleep(1)
    pause_time = task_controller.task_pause()
    task_controller.task_resume()
    assert task_controller.timer.is_alive() == True
    assert task_controller.pause_time == 0
    assert task_controller.task_get_remaining_time_int() > 0


def test_task_cancel(task_controller):
    task_controller.task_start()
    task_controller.task_cancel()
    assert task_controller.timer.is_alive() == False


def test_task_get_remaining_time_int(task_controller):
    task_controller.task_start()
    time.sleep(1)
    assert task_controller.task_get_remaining_time_int() == 4


def test_task_get_remaining_time(task_controller):
    task_controller.task_start()
    time.sleep(1)
    assert task_controller.task_get_remaining_time() == "4 minutes and 59 seconds"
