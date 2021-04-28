from abc import ABC, abstractmethod


class Counter:  # отсутствие инкапсуляции
    def __init__(self):
        self.count = 0


class Counter2:  # инкапсуляция с помощью getter / setter
    def __init__(self):
        self.__count = 0

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, value: int) -> None:
        if value <= 0:
            raise Exception('count should be >= 0')
        self.__count = value


class Counter3:  # инкапсуляция через специализированные протоколы доступа
    def __init__(self):
        self.__count = 0

    @property
    def count(self) -> int:
        return self.__count

    def inc(self) -> None:
        self.__count += 1

    def dec(self) -> None:
        if self.__count <= 0:
            raise Exception('count should be >= 0')
        self.__count -= 1


# ------------------------------
# реализация за счёт интерфейса
# ------------------------------


class IPrinter(ABC):
    @abstractmethod
    def print_(self, message: str):
        pass


class ConsolePrinter(IPrinter):
    def print_(self, message: str):
        print(message)


class ColorPrinter(IPrinter):
    def print_(self, message: str):
        print(f'Message with color: {message}')


# клиентский код
def print_(printer: IPrinter):
    message = input()
    printer.print_(message)


if __name__ == '__main__':
    cp = ConsolePrinter()
    ColorP = ColorPrinter()

    print_(cp)
    print_(ColorP)
