import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Toyota Corolla", 110000,
                       7,1200, 2500))
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 200000,
                               5500, 150))
    calc.add_car(
        calculator.Car("Citroen", 650000,
                       3, 3000, 7000))
    calc.print_cars()
