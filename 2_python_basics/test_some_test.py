import os
from unittest import mock

def some_method():
    print(os)

@mock.patch(__name__+'.os')
def test_some_method(mock_os):
    some_method()
    assert False


if __name__ == '__main__':
    some_method()