class Right_triangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def right_triangle_area(self):
        return int((self.side_a * self.side_b) / 2)

S = Right_triangle(8, 4)
print(S.side_a)
print(S.side_b)
print(S.right_triangle_area())




