from pytest import mark

data = [('hello', 'world'),
        ('hello', ''),
        ('123', 'world'),]


@mark.parametrize('name,description', data)
def test_new_testcase(desktop_app_auth, name, description):
        desktop_app_auth.navegate_to('Create new test')
        desktop_app_auth.create_test(name, description)
        desktop_app_auth.navegate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(name)
        desktop_app_auth.test_cases.delete_test_by_name(name)