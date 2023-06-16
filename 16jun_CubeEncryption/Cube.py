class Cube:
    def __init__(self, corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8):
        self.cor1 = corner1
        self.cor2 = corner2
        self.cor3 = corner3
        self.cor4 = corner4
        self.cor5 = corner5
        self.cor6 = corner6
        self.cor7 = corner7
        self.cor8 = corner8

    def rotate_right(self):
        self.cor2, self.cor6, self.cor5, self.cor1 = self.cor1, self.cor2, self.cor6, self.cor5
        self.cor3, self.cor7, self.cor8, self.cor4 = self.cor4, self.cor3, self.cor7, self.cor8

    def rotate_left(self):
        self.cor1, self.cor5, self.cor6, self.cor2 = self.cor2, self.cor1, self.cor5, self.cor6
        self.cor4, self.cor8, self.cor7, self.cor3 = self.cor3, self.cor4, self.cor8, self.cor7

    def rotate_upward(self):
        self.cor1, self.cor5, self.cor8, self.cor4 = self.cor4, self.cor1, self.cor5, self.cor8
        self.cor2, self.cor6, self.cor7, self.cor3 = self.cor3, self.cor2, self.cor6, self.cor7

    def rotate_downward(self):
        self.cor4, self.cor1, self.cor5, self.cor8 = self.cor1, self.cor5, self.cor8, self.cor4
        self.cor3, self.cor2, self.cor6, self.cor7 = self.cor2, self.cor6, self.cor7, self.cor3

    def getting_word(self):
        return self.cor1 + self.cor2 + self.cor3 + self.cor4 \
               + self.cor5 + self.cor6 + self.cor7 + self.cor8

    def __repr__(self):
        return self.cor1 + '->' + self.cor2 + '->' + self.cor3 + '->' + self.cor4 \
               + '->' + self.cor5 + '->' + self.cor6 + '->' + self.cor7 + '->' + self.cor8
