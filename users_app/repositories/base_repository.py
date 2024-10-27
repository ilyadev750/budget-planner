from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def create_user():
        raise NotImplementedError

    @abstractmethod
    async def authenticate_user():
        raise NotImplementedError


class TokenRepository(ABC):
    @abstractmethod
    async def create_access_token():
        raise NotImplementedError
