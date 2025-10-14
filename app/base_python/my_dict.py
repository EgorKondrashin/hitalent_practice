from collections.abc import Generator
from typing import Any

DEFAULT_CAPACITY = 8
DEFAULT_LOAD_FACTOR = 0.75


class MyDict:
    def __init__(
        self,
        initial_capacity: int = DEFAULT_CAPACITY,
        load_factor: float = DEFAULT_LOAD_FACTOR,
    ) -> None:
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._buckets: list[list[tuple[int | str, Any]]] = [[] for _ in range(self._capacity)]
        self._size = 0
        self._iter_index = 0
        self._iter_bucket_index = 0

    def _hash(
        self,
        key: int | str,
    ) -> int:
        return hash(key) % self._capacity

    def _resize(
        self,
    ) -> None:
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self._direct_set(key, value)

    def _direct_set(
        self,
        key: int | str,
        value: Any,
    ) -> None:
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def __setitem__(
        self,
        key: int | str,
        value: Any,
    ) -> None:
        if self._size >= self._capacity * self._load_factor:
            self._resize()
        self._direct_set(key, value)

    def __getitem__(
        self,
        key: int | str,
    ) -> Any:
        index = self._hash(key)
        bucket = self._buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        msg = f'Key {key} not found'
        raise KeyError(msg)

    def __delitem__(
        self,
        key: int | str,
    ) -> None:
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self._size -= 1
                return

        msg = f'Key {key} not found'
        raise KeyError(msg)

    def __contains__(
        self,
        key: int | str,
    ) -> bool:
        index = self._hash(key)
        bucket = self._buckets[index]

        return any(existing_key == key for existing_key, _ in bucket)

    def __len__(
        self,
    ) -> int:
        return self._size

    def __iter__(
        self,
    ) -> Generator[int | str]:
        for bucket in self._buckets:
            for key, _ in bucket:
                yield key

    def get(
        self,
        key: int | str,
        default: Any = None,
    ) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def keys(
        self,
    ) -> Generator[int | str]:
        yield from self

    def values(
        self,
    ) -> Generator[Any]:
        for key in self:
            yield self[key]

    def items(
        self,
    ) -> Generator[tuple[int | str, Any]]:
        for key in self:
            yield key, self[key]

    def __repr__(
        self,
    ) -> str:
        items = []
        for key, value in self.items():
            items.append(f'{key}: {value}')
        return '{' + ', '.join(items) + '}'
