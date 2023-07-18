#!/usr/bin/python3
""" Write The Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ It's A Function Width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ It's A Function Width """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ It's A Function Height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ It's A Function Height """

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ It's A Function X """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ It's A Function X """

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ It's A Function Y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ It's A Function Y """

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ AREA """
        return (self.__width * self.__height)

    def display(self):
        """ Display """

        rectangle = ""
        print_symbol = "#"

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """ _STR_ """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update The Public Method """

        if len(args) == 0:

            for key, val in kwargs.items():
                self.__setattr__(key, val)

            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    def to_dictionary(self):
        """ To Dictionary """

        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
