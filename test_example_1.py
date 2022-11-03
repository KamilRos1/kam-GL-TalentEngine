
from pytest import mark


def test_positive_int():
    num_1 = 5
    num_2 = 25 / 5
    assert num_1 == num_2


def test_positive_list():
    unknown_variable = []
    assert isinstance(unknown_variable, list)


def test_negative_string():
    string_to_test = "Negative Test"
    assert len(string_to_test) == 10


def test_negative_tuple():
    tuple_to_test = (2, 6, 8, 3, 1, 3, 5)
    assert callable(tuple_to_test)


@mark.xfail
def test_xfail_dict():
    dict_to_test = {
        "key1": 10,
        "key2": "name",
        "key3": None,
    }
    assert dict_to_test["key4"] == 20


@mark.xfail
def test_xfail_float():
    float_to_test = float("15")
    assert float_to_test == "15.0"


@mark.xfail
def test_xfail_positive_bool():
    variable_to_test = True
    assert variable_to_test
