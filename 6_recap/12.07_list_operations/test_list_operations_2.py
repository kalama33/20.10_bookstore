from list_operations import list_operations

def test_result():
    result = list_operations([2, 3])
    assert result[0] == 5

def test_largest_number():
    result = list_operations([5, 9, 15])
    assert result[1] == 15

def test_even():
    result = list_operations([2, 4, 6, 8])
    assert result[2][0] == 4