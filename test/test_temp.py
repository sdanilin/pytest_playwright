def test_assert():
    print('befor' * 5)
    result =  False
    print('after' * 5)
    assert result, 'this test faild intentionally'