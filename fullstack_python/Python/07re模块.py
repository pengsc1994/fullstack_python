import re

string = 'hello worsslld'

#正常字符：字母、数字、下划线

print(re.search('w\w{2}l', string)) #匹配w开头\w正常字符{2}2次l结尾
print(re.search('w.{2}l', string))  #同上
print(re.search('w.*l', string))    #*重复之前匹配符到最后一个
string = 'hello worrsslld'
print(re.search('r*s', string))     #*匹配前面的子表达式零次或多次
print(re.search('r+s', string))     #+匹配前面的子表达式一次或多次
print(re.search('r?s', string))     #+匹配前面的子表达式一次或零次
# * == {0,} + == {1,} ? == {0,1}    元字符用大括号来写
# [ ]内 元字符代表普通字符
string = 'hello wo3rrss1l\l,d'
print(string)
print(re.search('[^a-z,^ ].*[,]', string))

print(re.search(r'\\', string))

ret = re.search(r'(?P<id>\d).*(?P<id2>\\)', string)
print(ret)
print(ret.group())
print(ret.group('id'))
print(ret.group('id2'))
