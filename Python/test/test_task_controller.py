import pytest


class TestTaskController:

    def test_if_task_controller_exists(self):
        from Python.model.TaskController import TaskController
        controller = TaskController()
        assert controller

