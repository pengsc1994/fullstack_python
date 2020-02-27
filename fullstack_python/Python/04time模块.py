import time as t

while True:
    print("\r", t.strftime("%Y-%m-%d %A %H:%M:%S", t.localtime()), end="", flush=True)
    t.sleep(1)