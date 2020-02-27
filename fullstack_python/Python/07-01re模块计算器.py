import re

#删除空格
def del_blank(_str):
    _str = _str.replace(' ','')
    _str = _str.replace('+-','-')
    _str = _str.replace('--','+')
    _str = _str.replace('*+','*')
    print(_str)
    return _str

#加减乘除
def do(string):
    while re.search(r'[\+,\-,\*,/]', string) != None:
        string = del_blank(string)
        num = 0
        _ret = re.search(r'(?P<sybmol1>[\-]*)(?P<num1>\d+\.*\d*)(?P<doWhat>[\*,/])(?P<sybmol2>[\-]*)(?P<num2>\d+\.*\d*)', string)
        if _ret != None:
            doWhat = _ret.group('doWhat')
            if doWhat == '*':
                num = float(_ret.group('num1')) * float(_ret.group('num2'))
            if doWhat == '/':
                num = float(_ret.group('num1')) / float(_ret.group('num2'))
            if _ret.group('sybmol1') != _ret.group('sybmol2'):
                num = 0 - num
            string = string[:_ret.span()[0]] + str(num) + string[_ret.span()[1]:]
            continue
        _ret = re.search(r'(?P<sybmol1>[\-]*)(?P<num1>\d+\.*\d*)(?P<doWhat>[\+,\-])(?P<num2>\d*\.*\d*)', string)
        if _ret == None:
            break
        doWhat = _ret.group('doWhat')
        if _ret.group('sybmol1') == '':
            if doWhat == '+':
                num = float(_ret.group('num1')) + float(_ret.group('num2'))
            if doWhat == '-':
                num = float(_ret.group('num1')) - float(_ret.group('num2'))
        else:
            if doWhat == '+':
                num = float(_ret.group('num2')) - float(_ret.group('num1'))
            if doWhat == '-':
                num = 0 - (float(_ret.group('num1')) + float(_ret.group('num2')))
        string = string[:_ret.span()[0]] + str(num) + string[_ret.span()[1]:]
        _ret = re.search(r'(?P<num1>\d*\.*\d*)(?P<doWhat>[\+,\-])(?P<num2>\d*\.*\d*)', string)
    return string

#优先计算最内部括号
def do_bracket(string):
    while re.search(r'\(.*\)', string) != None:
        _ret = re.search(r'\((?P<inner>[^\(\)]*)\)', string)
        string = string[:_ret.span()[0]] + str(do(_ret.group('inner'))) + string[_ret.span()[1]:]
        print(string)
    return string

def main(string):
    return do(do_bracket(string))



string = '1 + 2 + 3 + 4 + 5 + ( (21 - 12) * -3 + 12) * 5 + -1*(2+4 + 2)'
print(string)
print(main(string))


