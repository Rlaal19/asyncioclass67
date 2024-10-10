import time
import asyncio

data1 = [5, 2, 3, 1, 4]
data2 = [50, 30, 10, 20, 40]
data3 = [500, 300, 100, 200, 400]


async def process_data(data, delay):
    print(f"At t = {time.time() - start:.2f} รอ {delay} วินาทีก่อนประมวลผลข้อมูลชุดนี้...")
    await asyncio.sleep(delay)

    sorted_data = sorted(data)
    print(f"At t = {time.time() - start:.2f} ข้อมูลที่เรียบเรียง {sorted_data}")
    return sorted_data

async def main():
    # ใช้ asyncio.gather เพื่อรัน task พร้อมกัน
    results = await asyncio.gather(
        process_data(data1, 2),
        process_data(data2, 3),
        process_data(data3, 1)
    )
    p = 0
    # แสดงผลลัพธ์จากทุก task หลังจากที่ gather รอให้ task ทั้งหมดเสร็จสิ้น
    for i in results:
        p += 1
        print(f"At t = {time.time() - start:.2f} ผลลัพธ์จาก data{p}: {i}")
    

start = time.time()
asyncio.run(main())
