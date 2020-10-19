# TODO IF YOU RUN THIS FILE IN ITS CURRENT STATE IT WILL DEADLOCK DUE TO LOCKS AND SLEEPS BELOW.


import threading
# from threading import Thread

# TODO GREAT EXAMPLE TO SHOW TWO THREADS RUNNING AT ONCE
# def func():
#     for _ in range(100):
#         print("In the thread")

# thread = threading.Thread(target=func)
# thread.start()

# for _ in range(100):
#     print('In the main program')

# from random import randint
# from time import sleep

# # TODO running three threads simultaneously
# #nondamaen or running in the foreground
# def func(s):
#     print(f"Hello, {s}!")
#     sleep_time = randint(0, 3)
#     print(f"Sleeping for {sleep_time} seconds")
#     sleep(sleep_time) # can pause and run other threads
#     print(f"Good-bye, {s}!")

# thread1 = threading.Thread(target=func, args=("Adam",)) # add daemon=True for background daemon threads
# thread2 = threading.Thread(target=func, args=("James",))
# thread1.start()
# thread2.start()

# print("all threads started.")

# TODO ALLOW DAEMON THREADS TO RUN
# sleep(4)
# print("Done With this.")

# TODO OR once daemon is added.....
# thread1.join()
# thread2.join()
# print("Done with this.")


# from time import sleep

# class ValueHolder:
#     def __init__(self):
#         self._value = 0
#         self._lock = threading.Lock()

#     def increment(self):
#         self._lock.acquire() # comment out the acquire and release to see the difference
            # This Begins Critical Section
#         v = self._value
#         v = v + 1
#         sleep(0.1)
#         self._value = v
#         self._lock.release()
            # This ends Critical Section

#     @property
#     def value(self):
#         return self._value

# vh = ValueHolder()

# thread1 = threading.Thread(target=vh.increment, daemon=True)
# thread2 = threading.Thread(target=vh.increment, daemon=True)

# thread1.start()
# thread2.start()
# print("Threads all started.")
# thread1.join()
# thread2.join()
# print(vh.value)
# print("Done with this.")


from time import sleep

lock1 = threading.Lock()
lock2 = threading.Lock()

def func1():
    with lock1:
        sleep(0.1)
        with lock2:
            print("func1")

def func2():
    with lock2: # make sure locks are in same order and not 2, 1
        sleep(0.1)
        with lock1:
            print("func2")


thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)
thread1.start()
thread2.start()
