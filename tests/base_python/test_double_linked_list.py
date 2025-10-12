import pytest

from app.base_python.double_linked_list import DoubleLinkedList


@pytest.fixture
def list_() -> DoubleLinkedList:
    return DoubleLinkedList()


@pytest.fixture
def size() -> int:
    return 0


@pytest.fixture
def item() -> int:
    return 1


def test_append_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    list_.append(item + 1)
    list_.append(item)
    assert list_[0] == item + 1
    assert list_[1] == item


def test_prepend_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    list_.prepend(item + 1)
    list_.prepend(item)
    assert list_[0] == item


def test_insert_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    list_.append(item + 1)
    list_.insert(1, item)
    assert list_[1] == item


def test_negative_index_out_of_range(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    with pytest.raises(IndexError):
        list_.insert(-1, item)


def test_index_out_of_range(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    with pytest.raises(IndexError):
        list_.insert(1, item)


def test_delete_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    list_.append(item)
    assert list_.delete(item) == True


def test_delete_nonexistent_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    assert list_.delete(item) == False


def test_find_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    list_.append(item + 1)
    list_.append(item)
    assert list_.find(item) == 1


def test_find_nonexistent_item(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    assert list_.find(item) == -1


def test_iteration_list(
    list_: DoubleLinkedList,
    item: int,
) -> None:
    list_.append(item)
    iterator = iter(list_)
    assert next(iterator) == item
    with pytest.raises(StopIteration):
        next(iterator)
