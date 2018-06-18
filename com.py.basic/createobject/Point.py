import sys
import types


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# python 创建对象的9种方式

point1 = Point(1, 2)
point2 = eval("{}({},{})".format("Point", 1, 2))  # eval 计算指定表达式的值
point3 = globals()["Point"](1, 2)
point4 = locals()["Point"](1, 2)
point5 = getattr(sys.modules[__name__], "Point")(1, 2)
point6 = point1.__class__(1, 2)
point7 = type('Point', (Point,), {})(1, 2)
point8 = types.new_class('Point', (Point,), {})(1, 2)
