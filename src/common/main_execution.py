from time import time
from typing import Callable
import threading
from common.counter import Counter


def main(increase_function: Callable) -> None:

    first_counter = Counter(value=0, name="first_counter")
    second_counter = Counter(value=0, name="second_counter")
    third_counter = Counter(value=0, name="third_counter")
    fourth_counter = Counter(value=0, name="fourth_counter")
    fith_counter = Counter(value=0, name="fith_counter")
    sixth_counter = Counter(value=0, name="sixth_counter")
    
    threads = [
        threading.Thread(target=increase_function, args=(1,first_counter)),
        threading.Thread(target=increase_function, args=(1,fourth_counter)),
        threading.Thread(target=increase_function, args=(1,sixth_counter)),
        threading.Thread(target=increase_function, args=(1,third_counter)),
        threading.Thread(target=increase_function, args=(1,first_counter)),
        threading.Thread(target=increase_function, args=(1,fith_counter)),
        threading.Thread(target=increase_function, args=(1,first_counter)),
        threading.Thread(target=increase_function, args=(1,second_counter)),
        threading.Thread(target=increase_function, args=(1,fourth_counter)),
        threading.Thread(target=increase_function, args=(1,first_counter)),
        threading.Thread(target=increase_function, args=(1,second_counter)),
        threading.Thread(target=increase_function, args=(1,first_counter)),
        threading.Thread(target=increase_function, args=(1,fourth_counter)),
        threading.Thread(target=increase_function, args=(1,first_counter)),
        threading.Thread(target=increase_function, args=(1,sixth_counter)),
        threading.Thread(target=increase_function, args=(1,third_counter)),
        threading.Thread(target=increase_function, args=(1,third_counter)),
        threading.Thread(target=increase_function, args=(1,fith_counter)),
        threading.Thread(target=increase_function, args=(1,third_counter)),
        threading.Thread(target=increase_function, args=(1,sixth_counter)),
        threading.Thread(target=increase_function, args=(1,third_counter)),
    ]

    initial_time = time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    final_time = time()

    print(f"\nFinal value {first_counter.name}:", first_counter.value)
    print(f"Final value {second_counter.name}:", second_counter.value)
    print(f"Final value {third_counter.name}:", third_counter.value)
    print(f"Final value {fourth_counter.name}:", fourth_counter.value)
    print(f"Final value {fith_counter.name}:", fith_counter.value)
    print(f"Final value {sixth_counter.name}:", sixth_counter.value)
    
    print(f"\nExecution time: {round(final_time - initial_time, 3)} seconds")

