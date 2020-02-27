import json,time
loginStatus = False
loginInfo = {}

#注册
def join():
    usrPasswd = {}
    with open("用户密码.json", "r") as fd:
        usrPasswd = json.loads(fd.read())
        fd.close()
    print("----------join----------")
    usrName = input("usrName: ")
    passWd = input("passWd: ")
    if usrName in usrPasswd:
        print("usrName already exists!")
        return False
    usrPasswd[usrName] = passWd
    with open("用户密码.json", "w") as fd:
        fd.write(json.dumps(usrPasswd))
        fd.close()
    return True

#登录
def login():
    global loginStatus
    global loginInfo
    if loginStatus == True:
        return True
    usrPasswd = {}
    with open("用户密码.json", "r") as fd:
        usrPasswd = json.loads(fd.read())
        fd.close()
    print("----------longin----------")
    usrName = input("usrName: ")
    passWd = input("passWd: ")
    if usrPasswd.get(usrName) != passWd:
        print("usrName or passwd error!")
        return False
    print("login successful!")
    loginStatus = True
    loginInfo['usrName'] = usrName
    loginInfo['passWd'] = passWd
    return True

#登出
def logout():
    global loginStatus
    global loginInfo
    loginStatus = False
    loginInfo = {}
    return True

def init():
    menu = """
    ------------------
    1.login
    2.join
    3.logout
    4.exit
    ------------------
    """
    choice = 1
    while choice in range(1, 5) :
        print(menu)
        choice = int(input("have a choice:"))
        if choice == 1:
            return login()
        if choice == 2:
            join()
        if choice == 3:
            logout()
        if choice == 4:
            exit()

def main(func):
    def _main():
        func()
        return func
    init()
    return _main

@main
def test1():
    if loginInfo == {}:
        print("have to login first!")
        return -1
    print("welcome user %s"%loginInfo["usrName"])
    print("in test1")
    return 1

test1()



