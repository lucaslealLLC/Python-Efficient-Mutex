from abc import ABC, abstractmethod

from mutex_solution.mutex import CustomMutex


class MutexWorkerAbstract(ABC):
    @abstractmethod
    def __enter__(self) -> "MutexWorkerAbstract":
        """implement context manager"""

    @abstractmethod
    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        """implement context manager"""

    @property
    @abstractmethod
    def custom_mutex(self) -> CustomMutex:
        """Enforcing composition with CustomMutex"""

