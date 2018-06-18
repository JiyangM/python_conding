class Filter:
    def __init__(self):
        self


# filter()函数用于过滤序列, 过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

# filter()函数接收一个函数 func 和一个iterable(可以是list，字符串等)，这个函数 func 的作用是对每个元素进行判断，
# 返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，最后将返回 True 的元素放到新列表中。

list = [1, 2, 3, 4, 5, 6, 7, 8]


def is_gt_5(num):
    return num > 5


new_list = filter(is_gt_5, list)
print(new_list)

name = 'pythontab.com 2018'
# 过滤非数字字符
filter(str.isdigit, name)
# 过滤数字
filter(str.isalpha, name)
# 保留数字和小数点
filter(lambda char: char in '0123456789.', name)
