import user1 as user
import json
user.init("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/ATM_user.json")

def join():
    #is_normal  账户冻结状态True正常False冻结
    #limit      额度
    #balance    余额
    return user.join({'is_normal':True, 'limit': 20000 , 'balance': 0})

def login(func):
    def _login(*info):
        ret = user.login()
        if ret == False:
            if input('is join a new user? y/n') in ['y','Y']:
                if join() == True:
                    _login(*info)
                return False
            else:
                _login(*info)
        func(*info)
        return True
    return _login

@login
def logout():
    return user.logout()


#加减冻结
#冻结  
def freeze_user(user, flag):
    #user   用户名
    #flag   Flase 冻结 True 解冻
    users = {}
    with open("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/ATM_user.json", "r") as fd:
        users = json.loads(fd.read())
        fd.close()
    if user not in users:
        print('do not have %s.'%user)
        return False
    users[user]['is_normal'] = flag
    with open("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/ATM_user.json", "w") as fd:
        fd.write(json.dumps(users))
        fd.close()
    return True

#是否被冻结
def is_normal(user):
    users = {}
    with open("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/ATM_user.json", "r") as fd:
        users = json.loads(fd.read())
        fd.close()
    if user not in users:
        print('do not have %s.'%user)
        return False
    return users[user]['is_normal']

#转账
def transfer(user1, user2, amount):
    #user   用户名
    #flag   Flase 冻结 True 解冻
    users = {}
    with open("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/ATM_user.json", "r") as fd:
        users = json.loads(fd.read())
        fd.close()
    if user1 not in users:
        print('do not have %s.'%user1)
        return False
    if user2 not in users:
        print('do not have %s.'%user2)
        return False
    if users[user1]['is_normal'] == False:
        print('user %s was freezed.', user1)
        return False
    if users[user2]['is_normal'] == False:
        print('user %s was freezed.', user2)
        return False
    users[user1]['balance'] -= amount
    users[user2]['balance'] += amount
    with open("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/ATM_user.json", "w") as fd:
        fd.write(json.dumps(users))
        fd.close()
    return True

#加     存钱
@login
def save_money(amount):
    if is_normal(user.userName) == False:
        print('user %s was freezed.', user.userName)
        return False
    info = user.loginInfo
    info[user.userName]['balance'] += amount
    return user.modifyInfo(info)
#减     取钱
@login
def get_money(amount):
    if is_normal(user.userName) == False:
        print('user %s was freezed.', user.userName)
        return False
    info = user.loginInfo
    info[user.userName]['balance'] -= amount
    if info[user.userName]['balance'] < 0:
        if input('is use credit limit？ y/n') in ['y', 'Y']:
            #从额度提现5%手续费
            info[user.userName]['limit'] += info[user.userName]['balance'] * 0.05
            if info[user.userName]['limit'] < 0:
                print('your spend is ouver limit.')
                return False
            info[user.userName]['balance'] = 0
        else:
            print('your balance is less than your spend.')
            return False
    return user.modifyInfo(info)

#减     花钱
@login
def use_money(amount):
    if is_normal(user.userName) == False:
        print('user %s was freezed.', user.userName)
        return False
    info = user.loginInfo
    print(info)
    if input('is use credit limit？ y/n') in ['y', 'Y']:
        #从额度提现5%手续费
        info[user.userName]['limit'] -= amount
        if info[user.userName]['limit'] < 0:
            print('your spend is ouver limit.')
            return False
    else:
        info[user.userName]['balance'] -= amount
        if info[user.userName]['balance'] < 0:
            print('your spend is ouver balance.')
            return False
    return user.modifyInfo(info)

def show_me():
    print(user.loginInfo)

if __name__ =='__main__':
    use_money(5)