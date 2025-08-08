from abc import ABC, abstractmethod


class ResumidorPort(ABC):
    @abstractmethod
    def resumir(self, texto: str) -> str:
        pass
