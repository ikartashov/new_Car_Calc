import pytest
from unittest.mock import patch
from apis import get_gas_price, get_power_price

mileages = [100, 1000, 2000, 5000]


class TestCar:
    @patch('calculator.get_gas_price', return_value=50)
    @pytest.mark.parametrize('mileage', mileages)
    def test_dynamic_cost(self, mock_get_gas_price, car, mileage):
        cost = car.dynamic_cost(mileage)
        expected_cost = 8.8 * mileage / 100 * 50
        assert cost == expected_cost

    def test_static_year_cost(self, car):
        cost = car.static_year_cost()
        expected_cost = 15000
        assert cost == expected_cost

    @patch('calculator.get_gas_price', return_value=50)
    @pytest.mark.parametrize('mileage', mileages)
    def test_year_cost(self, mock_get_gas_price, car, mileage):
        static = car.static_year_cost()
        dynamic = 8.8 * mileage / 100 * 50
        expected_cost = static + dynamic
        cost = car.year_cost(mileage)
        assert cost == expected_cost


class TestElectricCar:
    @patch('calculator.get_power_price', return_value=10)
    @pytest.mark.parametrize('mileage', mileages)
    def test_dynamic_cost(self, mock_get_power_price, electric_car, mileage):
        dynamic = electric_car.dynamic_cost(mileage)
        expected_cost = 150 * mileage / 1000 * 10
        assert dynamic == expected_cost


class TestAPI:
    @pytest.mark.parametrize('function', [get_gas_price, get_power_price])
    def test_get_price(self, function):
        res = function()
        assert isinstance(res, int) or isinstance(res, float)


class TestCalculator:
    def test_add_car(self, calculator,car):
        calculator.add_car(car)
        assert calculator.cars
        assert car in calculator.cars
        assert calculator.cars[car] > 0

    def test_print_cars(self,calculator):
        calculator.print_cars()

    def test_get_left_price(self,calculator, car):
        res = calculator.get_left_price(car)
        assert res


