import pytest
from calculator import Car, ElectricCar, Calculator


@pytest.fixture
def car():
    return Car('Test Car', 100000, 8.8, 5000, 10000)

@pytest.fixture
def electric_car():
    return ElectricCar("Tesla Model 3", 200000, 5500, 150)

@pytest.fixture
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return res