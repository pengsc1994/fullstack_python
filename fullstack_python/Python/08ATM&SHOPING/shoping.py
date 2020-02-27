import user, ATM
user.init("d:/#full_stack/fullstack_python/Python/08ATM&SHOPING/shoping_user.json")

def join():
    return user.join({'shoping_bus':[],'atm_card':0})

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

@login
def add_pay_card():
    cardNum = int(input("input your atm card num"))
    if cardNum <= 0:
        print('card number is invalid!')
        return False
    
@login
def show_shoping_bus():
    for i in user.loginInfo[user.userName]['shoping_bus']:
        print(i)
@login
def add_shoping_bus(goods):
    info = user.loginInfo
    if info[user.userName]['shoping_bus'] == []:
        info[user.userName]['shoping_bus'] += goods
    else:
        index = 0
        newAdd = goods
        for i in goods:
            for j in info[user.userName]['shoping_bus']:
                if i['name'] == j['name']:
                    j['num'] += 1
                    del newAdd[index]
            index += 1
        print(newAdd)
        if newAdd != []:
            info[user.userName]['shoping_bus'] += newAdd
    user.modifyInfo(info)
@login
def pay_shoping_bus():
    cost_money = 0
    info = user.loginInfo
    if info[user.userName]['shoping_bus'] == []:
        print('your shopnig bus is null.')
        return False
    for i in info[user.userName]['shoping_bus']:
        cost_money += i['price'] * i['num']
    if ATM.use_money(cost_money):
        info[user.userName]['shoping_bus'] = []
    user.modifyInfo(info)

if __name__ == '__main__':
    goods = [{'name':'test3', 'price':100, 'num':1},{'name':'test2', 'price':111, 'num':1}]
    add_shoping_bus(goods)
    show_shoping_bus()
    pay_shoping_bus()
