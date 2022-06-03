#!/usr/bin/python3
"""
Module for Square class
"""


class Square():
    """Square class definition"""
    width = 0
    height = 0


    def __init__(self, *args, **kwargs):
        """Constructor method for Square instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['width', 'height']:
                    setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimiter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
