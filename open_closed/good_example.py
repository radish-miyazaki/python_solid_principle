import math
from abc import ABCMeta, abstractmethod


class IEmployee(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_bonus(self, base: int) -> int:
        pass


class JuniorEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.1)


class MiddleEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.5)


class SeniorEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 2.0)


class ExpertEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 3.0)


if __name__ == "__main__":
    emp1 = JuniorEmployee("Yamada")
    emp2 = MiddleEmployee("Suzuki")
    emp3 = SeniorEmployee("Tanaka")
    emp4 = ExpertEmployee("Kimura")

    bonus_calculator = [emp1, emp2, emp3, emp4]
    for emp in bonus_calculator:
        print(emp.get_bonus(100))
