import pytest

from app.base_python.my_dict import MyDict


@pytest.fixture
def my_dict_() -> MyDict:
    return MyDict()


@pytest.fixture
def int_value() -> int:
    return 10


@pytest.fixture
def int_key() -> int:
    return 1


@pytest.fixture
def str_key() -> str:
    return 'test'


def test_set_item(
    my_dict_: MyDict,
    str_key: str,
    int_value: int,
) -> None:
    my_dict_[str_key] = int_value
    assert my_dict_[str_key] == int_value


def test_re_set_item(
    my_dict_: MyDict,
    str_key: str,
    int_value: int,
) -> None:
    my_dict_[str_key] = int_value + 1
    my_dict_[str_key] = int_value
    assert my_dict_[str_key] == int_value


def test_del_item(
    my_dict_: MyDict,
    int_value: int,
    int_key: int,
) -> None:
    my_dict_[int_key] = int_value
    assert list(my_dict_.items()) == [(int_key, int_value)]
    del my_dict_[int_key]
    assert list(my_dict_.items()) == []


def test_get_item(
    my_dict_: MyDict,
    int_value: int,
    int_key: int,
) -> None:
    my_dict_[int_key] = int_value
    assert my_dict_.get(int_key) == int_value


def test_get_default_item(
    my_dict_: MyDict,
    int_value: int,
    int_key: int,
) -> None:
    assert my_dict_.get(int_key) is None
    assert my_dict_.get(key=int_key, default=int_value) == int_value


def test_get_keys(
    my_dict_: MyDict,
    int_value: int,
    int_key: int,
    str_key: str,
) -> None:
    my_dict_[int_key] = int_value
    my_dict_[str_key] = int_value
    assert list(my_dict_.keys()) == [int_key, str_key]


def test_get_values(
    my_dict_: MyDict,
    str_key: str,
    int_key: int,
    int_value: int,
) -> None:
    my_dict_[int_key] = int_value
    my_dict_[str_key] = int_value
    assert list(my_dict_.values()) == [int_value, int_value]


def test_get_items(
    my_dict_: MyDict,
    int_value: int,
    int_key: int,
    str_key: str,
) -> None:
    my_dict_[int_key] = int_value
    my_dict_[str_key] = int_value
    assert list(my_dict_.items()) == [(int_key, int_value), (str_key, int_value)]


def test_iteration_my_dict(
    my_dict_: MyDict,
    int_key: int,
    int_value: int,
) -> None:
    my_dict_[int_key] = int_value
    iterator = iter(my_dict_)
    assert next(iterator) == int_key
    with pytest.raises(StopIteration):
        next(iterator)
