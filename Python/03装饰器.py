import time as t

def getTime(function):
    def inner(*num,**nums):
        t1 = t.time()
        function(*num, **nums)
        t2 = t.time()
        print("%s use time: %fs"%(function.__name__, t2 - t1))
        return function
    return inner #返回函数名带()调用时会执行两次入参函数

@getTime
def test1():
    print("in test1.")
    return 'xxxxx' + 'zzzzzzzz'

@getTime
def test2():
    print("in test2.")
    return 'xxxxx' + 'zzzzzzzz'

@getTime
def add(*num,**nums):
    sum = 0
    for i in num:
        sum += i
    print(sum)
    return sum

#getTiem(test1)
#getTiem(test2)
'''
a = test1()
b = test2()
c = add(1,2,3,4,5,6,7,8,9,10)
print(a, b, c)
'''
#不接收返回值会再次执行返回函数
test1()
test2()
add(1,2,3,4,5,6,7,8,9,10)
