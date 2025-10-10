from collections.abc import Generator


class DoubleLinkedList:
    class Node:
        def __init__(
            self,
            value: int,
        ) -> None:
            self.value = value
            self.prev = None
            self.next = None

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
        new_node = self.Node(value)

        if self.head is None:
            self.head = self.tail = new_node  # type: ignore[assignment]
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(
        self,
        value: int,
    ) -> None:
        new_node = self.Node(value)

        if self.head is None:
            self.head = self.tail = new_node  # type: ignore[assignment]
        else:
            new_node.next = self.head
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
            new_node = self.Node(value)
            new_node.prev = current.prev
            new_node.next = current  # type: ignore[assignment]
            current.prev.next = new_node  # type: ignore[attr-defined]
            current.prev = new_node  # type: ignore[assignment]

            self._size += 1

    def delete(
        self,
        value: int,
    ) -> bool:
        current = self.head

        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self._size -= 1
                return True

            current = current.next

        return False

    def find(
        self,
        value: int,
    ) -> int:
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

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
