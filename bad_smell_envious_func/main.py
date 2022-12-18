# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_volume(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:
    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_volume()


cube_sides = Cube(3, 3, 5)
cube_volume = CubeVolumeCalculator
print(cube_volume.calc_cube_volume(cube_sides))
