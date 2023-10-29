from time import sleep
from common.counter import Counter
from mutex_solution.worker import CounterMutexWorker


def increase(by: int, counter: Counter):

    worker = CounterMutexWorker()

    with worker:
        worker.lock_by_counter(counter.name)

        local_counter = counter.value
        local_counter += by

        sleep(0.1) # simulating process time of 7 seconds

        counter.value = local_counter

        worker.unlock_by_counter()
