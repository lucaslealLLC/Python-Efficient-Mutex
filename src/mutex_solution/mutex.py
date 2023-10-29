import threading

from mutex_solution.singleton_thread_safe import SingletonThreadSafeMeta


class CustomMutex(metaclass=SingletonThreadSafeMeta):

    def __init__(self):
        self.__lockers: dict[str, threading.Lock] = {}
        self.__lockers_counter: dict[str, int] = {}

    def __decrease_counter(self, key: str) -> None:
        self.__lockers_counter[key] -= 1

        if self.__lockers_counter == 0:
            del self.__lockers[key]
            del self.__lockers_counter[key]

    def __get_thread_locker(self, key: str) -> threading.Lock:
        if key in self.__lockers:
            self.__lockers_counter[key] += 1
            return self.__lockers[key]

        self.__lockers_counter[key] = 1
        thread_locker = threading.Lock()
        self.__lockers[key] = thread_locker

        return thread_locker

    def lock_with_key(self, key: str) -> None:
        """Locks the thread associated with the key"""

        thread_locker = self.__get_thread_locker(key)
        thread_locker.acquire()

    def unlock_with_key(self, key: str) -> None:
        """Unlocks the thread associated with the key"""

        if key in self.__lockers:

            thread_locker = self.__lockers[key]
            self.__decrease_counter(key)
            thread_locker.release()
