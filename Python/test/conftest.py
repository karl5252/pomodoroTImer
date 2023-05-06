# import pytest
#
#
# def pytest_collection_modify_items(items):
#     for item in items:
#         if item.get_marker('timeout') is None:
#             item.add_marker(pytest.mark.timeout(6))
