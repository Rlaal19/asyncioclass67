import asyncio

async def fibonacci(n):
    await asyncio.sleep(1)
    a,b =0,1
    if n <= 1:
        return n
    else:
        for i in range (1,n):
            c= a+b
            a = b
            b = c
        return b
    
async def main():
    n= 10
    coro = [asyncio.create_task(fibonacci(i)) for i in range(n)]
    # results = await asyncio.gather(*coro)
    # print(results)
    done, pending = await asyncio.wait(coro)
    
    # ดึงผลลัพธ์จาก tasks ที่เสร็จสิ้นแล้ว
    results = [task.result() for task in done]
    print(results)

asyncio.run(main())