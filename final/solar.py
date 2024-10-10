import asyncio
import random
import time

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f"Solar Cell {id} hardware speed: {self.hardware_readtime}")

    async def read_vol(self):
        vol = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)
        return vol

async def read_from_solar_cell(solar_cells):
    try:
        while True:
            tasks = [solar_cell.read_vol() for solar_cell in solar_cells]
            results = await asyncio.gather(*tasks)  # รันหลาย ๆ ฟังก์ชันพร้อมกัน
            for i, vol in enumerate(results):
                print(f"{time.ctime()} Solar Cell #{solar_cells[i].id} Voltage: {vol} V")
            await asyncio.sleep(1)  # เพื่อไม่ให้ลูปทำงานเร็วเกินไป
    except KeyboardInterrupt:
        print("\nโปรแกรมหยุดทำงาน.")

async def main():
    num_cell = 5
    print(f"จำนวนแผงโซล่าเซลที่สร้าง: {num_cell}")
    solar_cells = [SolarCell(i + 1) for i in range(num_cell)]
    
    await read_from_solar_cell(solar_cells)  # ต้อง await เนื่องจากเป็น async function

if __name__ == "__main__":
    asyncio.run(main())
