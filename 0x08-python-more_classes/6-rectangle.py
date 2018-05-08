class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        self.number_of_instances = number_of_instances

    def __str__(self):
        string = ""
        if self.__height is 0 and self.__width is 0:
            return string
        for col in range(self.__height):
            for row in range(self.__width):
                string += "#"
            if col < self.__height - 1:
                string += "\n"

        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    def number_of_instances(self):
        self.number_of_instances = 0


    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return self.__width * 2 + self.__height * 2
