from figureclass import Rectangle, Square, Circle

"""Создаем экземпляры на основе клоссов"""
rect1 = Rectangle(3, 4)
rect2 = Rectangle(12,5)

square1 = Square(5)
square2 = Square(10)

circule1 = Circle(25)
circule2 = Circle(50)

"""Вычисляем площадь"""
figures = [rect1, rect2, square1, square2, circule1, circule2]
for figure in figures:
    if isinstance(figure, Square): # функция isinstance, поддерживающая наследование. Она проверяет, является ли аргумент объекта экземпляром класса или экземпляром класса из кортежа.
        print(figure.get_area_square()) # если экземпляр класса figure является квадратом, то вызываем метод get_area_square(),
    if figure == circule1:
        print(figure.get_area_circle())  # иначе мы обрабатываем данные для прямоугольника методом get_area_circle()
    if figure == circule2:
        print(figure.get_area_circle())
    if figure == rect1:
        print(figure.get_area()) # иначе мы обрабатываем данные для прямоугольника методом get_area().
    elif figure == rect2:
        print(figure.get_area())
