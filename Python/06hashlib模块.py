import hashlib

a = hashlib.md5()
with open('./Python/01深浅拷贝.py', 'r', encoding='utf-8') as f: 
    a.update(f.read().encode('utf-8'))
print(a.hexdigest())
