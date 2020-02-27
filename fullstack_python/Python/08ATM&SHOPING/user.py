import json,time
loginStatus = False
loginInfo = {}
userName = ''
confFile = ''

#选择用户文件
def init(file):
    global confFile
    if file == '':
        return False
    confFile = file
    return True

#注册
def join(usrInfo = {}):
    print(usrInfo)
    usrPasswd = {}
    with open(confFile, "r") as fd:
        usrPasswd = json.loads(fd.read())
        fd.close()
    print("----------join----------")
    usrName = input("usrName: ")
    passWd = input("passWd: ")
    if usrName in usrPasswd:
        print("usrName already exists!")
        return False
    usrInfo['passwd'] = passWd
    usrPasswd[usrName] = usrInfo
    with open(confFile, "w") as fd:
        fd.write(json.dumps(usrPasswd))
        fd.close()
    return True

#登录
def login():
    global loginStatus
    global loginInfo
    global userName
    if loginStatus == True:
        return True
    usrInfo = {}
    with open(confFile, "r") as fd:
        usrInfo = json.loads(fd.read())
        fd.close()
    print("----------longin----------")
    usrName = input("usrName: ")
    passWd = input("passWd: ")
    if usrName not in usrInfo:
        print('user %s is not join us!'%usrName)
        return False
    if usrInfo[usrName]['passwd'] != passWd:
        print("usrName or passwd error!")
        return False
    print("login successful!")
    loginStatus = True
    userName = usrName
    loginInfo[usrName] = usrInfo[usrName]
    return True

#登出
def logout():
    global loginStatus
    global loginInfo
    loginStatus = False
    loginInfo = {}
    return True

#修改用户info
def modifyInfo(info):
    global loginInfo
    loginInfo = info
    usrInfo = {}
    with open(confFile, "r") as fd:
        usrInfo = json.loads(fd.read())
        fd.close()
    usrInfo[userName] = loginInfo[userName]
    with open(confFile, "w") as fd:
        fd.write(json.dumps(usrInfo))
        fd.close()
    return True

