# example of using an asyncio queue
from random import random
import asyncio
import time

# corotine to generate work
async def producer(queue):
    print('Producer: Running')
    start = time.time()
    # gernerate work
    for i in range(10):
        # generate value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f'> Producer {value} sleep {sleeptime}')
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f'> Producer put {value}')
        await queue.put(value)
    # send all done signal
    await queue.put(None)
    print('Producer: Done')
    end = time.time()
    producer_time = end - start
    print(f'Producer time => {producer_time}')

# corotine to cosumer work
async def consumer(queue):
    print('Consumer: Running')
    start = time.time()
    # cosumer work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Cosumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop signal
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # print all done
    print('Consumer: Done')
    end = time.time()
    consumer_time = end - start
    print(f'Consumer time => {consumer_time}')

# entry point corotine
async def main():
    start= time.time()
    # create the share queue
    queue = asyncio.Queue()
    # run the producer and customer
    await asyncio.gather(producer(queue),consumer(queue))
    print(f"\n\n Time finish in =>", {time.time()-start}, "seconds.")

# start the asyncio
asyncio.run(main()) 