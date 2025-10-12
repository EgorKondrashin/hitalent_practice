from collections.abc import Generator


class DoubleLinkedList:
    class Node:
        def __init__(
            self,
            value: int,
            _prev: 'DoubleLinkedList.Node | None' = None,
            _next: 'DoubleLinkedList.Node | None' = None,
        ) -> None:
            self.value = value
            self.prev = _prev
            self.next = _next

        def __repr__(
            self,
        ) -> str:
            return repr(self.value)

    def __init__(
        self,
    ) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def __getitem__(self, item: int) -> int:
        return self._get_node_at_index(item).value

    def append(
        self,
        value: int,
    ) -> None:
        new_node = self.Node(value, _prev=self.tail)

        if self.head is None:
            self.head = self.tail = new_node  # type: ignore[assignment]
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(
        self,
        value: int,
    ) -> None:
        new_node = self.Node(value, _next=self.head)

        if self.head is None:
            self.head = self.tail = new_node  # type: ignore[assignment]
        else:
            self.head.prev = new_node
            self.head = new_node

        self._size += 1

    def insert(
        self,
        index: int,
        value: int,
    ) -> None:
        if index < 0 or index > self._size:
            msg = 'Index out of range'
            raise IndexError(msg)

        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            current = self._get_node_at_index(index)
            new_node = self.Node(
                value,
                _prev=current.prev,
                _next=current,
            )
            current.prev.next = new_node  # type: ignore[union-attr]
            current.prev = new_node

            self._size += 1

    def delete(
        self,
        value: int,
    ) -> bool:
        current = self.head

        for _ in range(self._size):
            if current.value == value:  # type: ignore[attr-defined, union-attr]
                if current == self.head:
                    self.head = current.next  # type: ignore[attr-defined, union-attr]
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev  # type: ignore[attr-defined]
                    self.tail.next = None  # type: ignore[attr-defined]
                else:
                    current.prev.next = current.next  # type: ignore[attr-defined]
                    current.next.prev = current.prev  # type: ignore[attr-defined]

                self._size -= 1
                return True

            current = current.next  # type: ignore[attr-defined, union-attr]

        return False

    def find(
        self,
        value: int,
    ) -> int:
        current = self.head

        for index in range(self._size):
            if current.value == value:  # type: ignore[attr-defined, union-attr]
                return index
            current = current.next  # type: ignore[attr-defined, union-attr]

        return -1

    def _get_node_at_index(
        self,
        index: int,
    ) -> Node:
        if index < 0 or index >= self._size:
            msg = 'Index out of range'
            raise IndexError(msg)
        current = self.head
        for _ in range(index):
            current = current.next  # type: ignore[union-attr, attr-defined]
        return current  # type: ignore[return-value]

    def __len__(
        self,
    ) -> int:
        return self._size

    def __iter__(
        self,
    ) -> Generator[int]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(
        self,
    ) -> str:
        return ' <-> '.join([str(item) for item in self]) if self.head else 'Empty list'
