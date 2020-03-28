import pickle as p
#系统成员类
#学生 Student
#课程 Course
#学校 School
#班级 Class
#讲师 Teacher
conf = {
    'Student'   :'D:/#full_stack/fullstack_python/Python/09CourceSelectionSystem/conf/student.conf',
    'School'    :'D:/#full_stack/fullstack_python/Python/09CourceSelectionSystem/conf/student.conf',
    'class'     :'D:/#full_stack/fullstack_python/Python/09CourceSelectionSystem/conf/student.conf',
    'course'    :'D:/#full_stack/fullstack_python/Python/09CourceSelectionSystem/conf/student.conf',
    'teacher'   :'D:/#full_stack/fullstack_python/Python/09CourceSelectionSystem/conf/student.conf'
}


def FileToDict(_str):
    _dict = {}
    if _str not in conf:
        print('type of __class was not found.')
        return _dict
    with open(conf[_str], 'rb') as rf:
        read = rf.read()
        #print(read)
        if read != b'':
            _dict = p.loads(read)
        rf.close()
    return _dict

def DictToFile(_str, _dict):
    if _str not in conf:
        print('type of __class was not found.')
        return False
    with open(conf[_str], 'wb') as wf:
        wf.write(p.dumps(_dict))
        wf.close()
    return True

class Student:
    #姓名
    #所属学校
    #所属班级

    def __init__(self, _name):
        _dict = FileToDict('Student')
        #print(_dict)
        if _name in _dict:
            #self = _dict[_name]
            #不能直接将获取到的类赋值给当前类
            self._name = _dict[_name]._name
            self._school = _dict[_name]._school
            self._class = _dict[_name]._class
        else:
            _school = input("input your school: ")
            _class = input("input your class: ")
            self._name = _name
            self._school = School(_school)
            self._class = Class(_class)
            _dict[_name] = self
            DictToFile('Student', _dict)
    
class School:
    def __init__(self, _name):
        _dict = FileToDict('School')
        #print(_dict)
        if _name in _dict:
            self._name = _dict[_name]._name
            self._classes = _dict[_name]._classes
        else:
            self._name = _name
            self._classes = {}
            if input('is establish a new class?[yes/no]') == "yes":
                self.addClass()
            else:
                _dict[_name] = self
                DictToFile('School', _dict)
    #添加班级
    def addClass(self):
        _class = input("input class name: ")
        if _class not in self._classes:
            self._classes[_class] = Class(_class)
        _dict = FileToDict('School')
        _dict[self._name] = self
        DictToFile('School', _dict)


class Class:
    def __init__(self, _name):
        _dict = FileToDict('Class')
        #print(_dict)
        if _name in _dict:
            self._name = _dict[_name]._name
            self._course = _dict[_name]._course
        else:
            self._name = _name
            self._course = {}
            if input('is establish a new class?[yes/no]') == "yes":
                self.addCourse()
            else:
                _dict[_name] = self
                DictToFile('Class', _dict)
    #添加班级
    def addCourse(self):
        course = input("input class name: ")
        if course not in self._course:
            self._course[course] = Course(course)
        _dict = FileToDict('Class')
        _dict[self._name] = self
        DictToFile('Class', _dict)

class Course:
    def __init__(self, _name):
        #课程名
        #课程周期
        #课程价格
        #讲师
        _dict = FileToDict('Course')
        #print(_dict)
        if _name in _dict:
            self._name = _dict[_name]._name
            self._period = _dict[_name]._period
            self._price = _dict[_name]._price
            self._teacher = _dict[_name]._teacher
        else:
            self._name = _name
            self._period = int(input("input class period: "))
            self._price = int(input("input class cost: "))
            _teacher = input("input class teacher: ")
            _school = input("input teacher school: ")
            self._teacher = Teacher(_teacher)
            _dict[_name] = self
            DictToFile('Course', _dict)

class Teacher:
    def __init__(self, _name):
        _dict = FileToDict('Teacher')
        #print(_dict)
        if _name in _dict:
            self._name = _dict[_name]._name
            self._school = _dict[_name]._school
        else:
            self._name = _name
            _school = input("input teacher school: ")
            self._school = School(_school)
            _dict[_name] = self
            DictToFile('Teacher', _dict)


if __name__ == "__main__":
    s1 = Student("test1")
    print(s1._name)
    sc1 = School('school1')
    print(sc1._name, sc1._classes)
