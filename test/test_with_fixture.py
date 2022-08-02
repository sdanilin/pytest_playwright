def test_get_answer(ultimate_amswer):
    assert 42 == ultimate_amswer


def test_get_new_answer(new_answer):
    assert 43 == new_answer


def test_get_answers(ultimate_amswer, new_answer):
    assert 42 + 43 == ultimate_amswer + new_answer


def test_native(request):
    assert 'test_with_fixture.py' == request.fspath.basename
