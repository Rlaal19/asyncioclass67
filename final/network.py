import time
import asyncio
import math

data = [[2,3],[3,7],[6,9],[4,6],[3,5],[5,3],[7,4],[8,2],[6,1],[1,2]]
data = sorted(data)

# ฟังก์ชันสำหรับคำนวณระยะทางแบบ async
async def calculate_distance(x1, y1, point):
    x2, y2 = point
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"คำนวณระยะทางจาก ({x1}, {y1}) ไปยัง ({x2}, {y2}): {distance}")
    await asyncio.sleep(0)  # ใช้ sleep(0) เพื่อรองรับ async
    return distance

# ฟังก์ชันหลักสำหรับคำนวณระยะทางทั้งหมด
async def main():
    # ระบุพิกัดตำแหน่งอ้างอิง
    x1, y1 = 0, 0
    
    # สร้าง tasks สำหรับคำนวณระยะทาง
    tasks = [calculate_distance(x1, y1, point) for point in data]
    
    # รอให้ทุก tasks ทำงานเสร็จและเก็บผลลัพธ์
    result = await asyncio.gather(*tasks)
    
    # แสดงผลลัพธ์ทั้งหมด
    print("\nผลลัพธ์ของระยะทางทั้งหมด:", result)

# เรียกใช้ฟังก์ชันหลัก
asyncio.run(main())

