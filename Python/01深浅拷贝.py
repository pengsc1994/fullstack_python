_list = [[1,2,3],4,5,6,"wwwwwww", "testwww"]


#浅拷贝
_list2 = _list.copy()
_list2[0][2] = -1
_list2[1] = -123
print("%d  %d"%(id(_list[0]), id(_list2[0])))
#_list[0] 存的是列表的地址指针，浅拷贝只复制指针(可变类型公用指针)
print(_list2)
print(_list)

#直接赋值
#只是将新变量指向旧变量的地址
_list = [[1,2,3],4,5,6,"wwwwwww", "testwww"]
_list3 = _list
_list3[0][2] = -3
_list3[1] = -123
print("%d  %d"%(id(_list), id(_list3)))
print(_list3)
print(_list)

print("%d  %d %d "%(id(_list[0]), id(_list2[0]), id(_list3[0])))

#深拷贝
import copy
_list = [[1,2,3],4,5,6,"wwwwwww", "testwww"]
deep_list = copy.deepcopy(_list)
deep_list[0][2] = -1
deep_list[1] = -123
print("%d  %d"%(id(_list[0]), id(deep_list[0])))
print(deep_list)
print(_list)

