from time import sleep

from common.counter import Counter


def increase(by: int, counter: Counter) -> None:

    local_counter = counter.value
    local_counter += by

    sleep(0.1) # simulating process time

    counter.value = local_counter
