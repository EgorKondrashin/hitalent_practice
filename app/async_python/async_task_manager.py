import asyncio
import logging
import random
from typing import Final

MAX_WORKER_COUNT: Final[int] = 5
WORKER_COUNT: Final[int] = 5
TASK_COUNT: Final[int] = 100
MIN_TASK_SLEEP_SECONDS: Final[float] = 0.5
MAX_TASK_SLEEP_SECONDS: Final[float] = 2.0


type Task = dict[str, int | float]
type TaskQueue = asyncio.Queue[Task]

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def worker(
    queue: TaskQueue,
    semaphore: asyncio.Semaphore,
) -> None:
    while queue.qsize():
        async with semaphore:
            task_info = await queue.get()

            logger.info(f'Task-{task_info["task_id"]} started!')  # noqa: G004
            await asyncio.sleep(task_info['duration'])
            logger.info(f'Task-{task_info["task_id"]} done!')  # noqa: G004

            queue.task_done()


def generate_task_info(task_id: int) -> Task:
    return {
        'task_id': task_id,
        'duration': random.uniform(MIN_TASK_SLEEP_SECONDS, MAX_TASK_SLEEP_SECONDS),  # nosec # noqa: S311
    }


async def fill_queue() -> TaskQueue:
    queue: TaskQueue = asyncio.Queue()
    for i in range(TASK_COUNT):
        await queue.put(generate_task_info(task_id=i))

    return queue


async def main() -> None:
    queue = await fill_queue()

    sem = asyncio.Semaphore(MAX_WORKER_COUNT)

    tasks = [worker(queue=queue, semaphore=sem) for _ in range(WORKER_COUNT)]

    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
