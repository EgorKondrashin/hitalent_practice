from collections.abc import Callable, Generator
from contextlib import contextmanager
from functools import wraps
from inspect import iscoroutinefunction
from logging import Logger
import time
from typing import ParamSpec, TypeVar, cast

P = ParamSpec('P')
R = TypeVar('R')


@contextmanager
def execution_error_manager(
    logger: Logger,
    func: Callable[P, R],
) -> Generator[None]:
    start_time = time.perf_counter()
    try:
        yield
        execution_time = time.perf_counter() - start_time
        logger.info(
            'Функция %s выполнена успешно, время выполнения %s.',
            func.__name__,
            execution_time,
        )
    except Exception:
        execution_time = time.perf_counter() - start_time
        logger.exception(
            'Функция %s завершилась с ошибкой, время выполнения %s',
            func.__name__,
            execution_time,
        )
        raise


def log_execution_time(logger: Logger) -> Callable[P, R]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        if iscoroutinefunction(func):

            @wraps(func)
            async def wrapper(
                *args: P.args,
                **kwargs: P.kwargs,
            ) -> R:
                with execution_error_manager(logger, func):
                    return await func(*args, **kwargs)
        else:

            @wraps(func)
            def wrapper(
                *args: P.args,
                **kwargs: P.kwargs,
            ) -> R:
                with execution_error_manager(logger, func):
                    return func(*args, **kwargs)

        return cast('Callable[P, R]', wrapper)

    return cast('Callable[P, R]', decorator)
