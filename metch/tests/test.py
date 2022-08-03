def test_list():
    print(List())
    assert list(List()) == list()
    assert list(List(1)) == list([1])
    l = List(1)
    l.pop()
    assert l == []
