# coding=utf-8
import os,os.path

class OperateFile:
    def __init__(self):
        self

# http://www.pythontab.com/html/2018/pythonjichu_0131/1237.html
# ======================== read 的3种方式

# 方法1
f = open("hello.txt")
while True:
    text = f.readline()
    if text:
        print(text)
    else:
        print(len(text))
        break
f.close()

# 方法2
f = open("hello.txt")
line_list = f.readlines()
print(type(line_list))
for line in line_list:
    print line
f.close()

# 方法3
f = open("hello.txt")
s = f.read()
print type(s)
for line in s:
    print(line)


# ======================== write 的2种方式
f = open("hello.txt", 'w', 'utf-8')
f.write('您好，python')
print '写入完毕'
f.close()


f = open("hello.txt",'a++')
print(f.read())
fruits = ['appple\n','banana\n','orange\n','watermelon\n']
f.writelines(fruits)
print ('写入成功')
f.close()

# ======================== delete 文件
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("文件不存在")


# ======================== copy 文件
srcFile = open("hello.txt")
destFile = open("hello2.txt",'w')
destFile.write(srcFile.read())
destFile.close()
srcFile.close()
print("复制完成")


with open("a.txt") as src ,open("b.txt") as dest:
    dest.write(src)
print("复制成功")