from time import sleep
from common.counter import Counter
import threading


lock = threading.Lock()


def increase(by: int, counter: Counter) -> None:

    with lock:

        local_counter = counter.value
        local_counter += by

        sleep(0.1) # simulating process time

        counter.value = local_counter