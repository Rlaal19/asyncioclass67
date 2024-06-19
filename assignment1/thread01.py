# running a function in another thread
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thead = Thread(target=task)
# run the thread
thead.start()
# wait for the thread to finish
print(f'{ctime()} waiting for the thread...')
thead.join()