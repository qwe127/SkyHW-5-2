# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, coordinate_x, coordinate_y):
        self.field = field
        self.x = coordinate_x
        self.y = coordinate_y
        self.state = 'walk'
        self.speed = 1

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2

        if self.state == 'walk':
            return self.speed * 1

        if self.state == 'crawl':
            return self.speed * 0.5

        else:
            raise ValueError('error')

    def move(self, direction):
        speed = self._get_speed

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        if direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        if direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        if direction == 'RIGHT':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
