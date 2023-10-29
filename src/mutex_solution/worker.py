import threading

from mutex_solution.mutex import CustomMutex
from mutex_solution.worker_abstract import MutexWorkerAbstract


class CounterMutexWorker(MutexWorkerAbstract):

    def __init__(self):
        self.__general_mutex = CustomMutex()
        self.__counter_key_lock: int | None = None
        self.__timeout = 5 # seconds
        self.__timeout_timer = threading.Timer(
            self.__timeout, 
            function=self.__timeout_callback
        )

    @property
    def custom_mutex(self) -> CustomMutex:
        return self.__general_mutex

    def __enter__(self) -> "CounterMutexWorker":
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.unlock_by_counter()

    def __format_key_lock_thread(self, counter_name: int) -> str:
        key = f"COUNTER_WORKER_KEY_{counter_name}"
        return key

    def __timeout_callback(self) -> None:
        print(f"Lock timeout! worker=CounterMutexWorker | key={self.__counter_key_lock}")
        print(f"Releasing Lock... worker=CounterMutexWorker key={self.__counter_key_lock}")

        self.unlock_by_counter()

    def lock_by_counter(self, counter_name: str) -> None:
        """Locks thread by counter name"""

        key = self.__format_key_lock_thread(counter_name)
        self.custom_mutex.lock_with_key(key=key)
        self.__timeout_timer.start()
        self.__counter_key_lock = counter_name

    def unlock_by_counter(self) -> None:
        """Unlocks thread by counter name"""

        if self.__timeout_timer.is_alive():
            self.__timeout_timer.cancel()

        if self.__counter_key_lock:
            key = self.__format_key_lock_thread(self.__counter_key_lock)
            self.custom_mutex.unlock_with_key(key=key)
            self.__counter_key_lock = None
