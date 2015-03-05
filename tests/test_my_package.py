from my_package import make_nwoo


def test_default_woo():
    assert make_nwoo() == 'woo'


def test_default_woo_5():
    assert make_nwoo(5) == 'wooooo'

