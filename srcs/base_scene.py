from abc import ABC, abstractmethod
from srcs.config import GAMEMODE


class BaseScene(ABC):
    @abstractmethod
    def update(self) -> GAMEMODE:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
