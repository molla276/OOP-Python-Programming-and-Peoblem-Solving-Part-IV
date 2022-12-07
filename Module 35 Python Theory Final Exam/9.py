# from time import sleep, perf_counter

# def f1():
#     for i in range(5):
#         print(f"f1 - {i}")
#         sleep(2)

# def f2():
#     for i in range(5):
#         print(f"f2 - {i}")
#         sleep(2)

# def f3():
#     for i in range(5):
#         print(f"f3 - {i}")
#         sleep(2)

# def f4():
#     for i in range(5):
#         print(f"f4 - {i}")
#         sleep(2)
# f1()
# f2()
# f3()
# f4()

from threading import Thread
import time
def f1():
    for i in range(5):
        print(f"f1 - {i}")
        time.sleep(0.2)
def f2():
    for i in range(5):
        print(f"f2 - {i}")
        time.sleep(0.2)
def f3():
    for i in range(5):
        print(f"f3 - {i}")
        time.sleep(0.2)
def f4():
    for i in range(5):
        print(f"f4 - {i}")
        time.sleep(0.2)

th1 = Thread(target=f1)
th2 = Thread(target=f2)
th3 = Thread(target=f3)
th4 = Thread(target=f4)

th1.start()
th2.start()
th3.start()
th4.start()
#Run code in parallel with other 4 functions
th1.join()
th2.join()
th3.join()
th4.join()
