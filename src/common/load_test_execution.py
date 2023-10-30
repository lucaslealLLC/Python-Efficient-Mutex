from random import randint
from time import time
from typing import Callable
import threading
from common.counter import Counter


def main_load_test(increase_function: Callable) -> None:

    counters = [
        Counter(value=0, name="first_counter"),
        Counter(value=0, name="second_counter"),
        Counter(value=0, name="third_counter"),
        Counter(value=0, name="fourth_counter"),
        Counter(value=0, name="fifth_counter"),
        Counter(value=0, name="sixth_counter"),
        Counter(value=0, name="seventh_counter"),
        Counter(value=0, name="eighth_counter"),
        Counter(value=0, name="ninth_counter"),
        Counter(value=0, name="tenth_counter"),
        Counter(value=0, name="eleventh_counter"),
        Counter(value=0, name="twelfth_counter"),
    ]

    amount_of_threads = 1000

    threads = [
        threading.Thread(
            target=increase_function, 
            args=(
                1, 
                counters[randint(0, len(counters) -1)]
            )
        )
        for _ in range(amount_of_threads)
    ]

    initial_time = time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    final_time = time()

    print("\n=======================================\n")

    for c in counters:
        print(f"Final value {c.name}:", c.value)    

    print("\n=======================================\n")
    
    print(f"Execution time: {round(final_time - initial_time, 3)} seconds")
