from abc import ABC, abstractmethod


class ModelRepository(ABC):

    @abstractmethod
    def create():
        raise NotImplementedError

    @abstractmethod
    def get_user_incomes():
        raise NotImplementedError

