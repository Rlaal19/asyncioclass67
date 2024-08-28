# example of using an asyncio queue
from random import random
import asyncio

# corotine to generate work
async def producer(queue):
    print('Producer: Running')
    # gernerate work
    for i in range(10):
        # generate value
        value = i
        # block to simulate work
        await asyncio.sleep(random())
        # add to the queue
        print(f'> Producer put {value}')
        await queue.put(value)
        print('Producer: Done')

# corotine to cosumer work
async def consumer(queue):
    print('Consumer: Running')
    # cosumer work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'> Cosumer got {item}')
        # print all done
        print('Cosumer: Done')

# entry point corotine
async def main():
    # create the share queue
    queue = asyncio.Queue()
    # run the producer and customer
    await asyncio.gather(producer(queue),consumer(queue))

# start the asyncio program
asyncio.run(main())

