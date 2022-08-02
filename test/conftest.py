'''Setting global fixture'''

from pytest import fixture

@fixture
def ultimate_amswer():
    return 42

@fixture
def new_answer(ultimate_amswer):
    return ultimate_amswer + 1
