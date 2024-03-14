class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


if __name__ == '__main__':
    s1 = Square(50)
    print("Square =", s1.get_perimetr())
