# coding:utf8
import time
import threading

N = 0


def change_it(n):
    global N
    N = N + n


def run_thread(n):
    for i in range(100000):
        change_it(n)


if __name__ == "__main__":
    t1 = threading.Thread(target=run_thread, args=(1,))
    t2 = threading.Thread(target=run_thread, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(N)
