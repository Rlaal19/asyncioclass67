import time
import asyncio

my_computer_time = 0.1
opponent_computer_time = 0.5
oppenents = 24
move = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move):
        time.sleep(my_computer_time)
        print(f"{x+1} {i} my time move")
        await asyncio.sleep(opponent_computer_time)
        print(f"{x+1} {i+1} oppenent time move")
    print(f"Board - {x+1} >>>>>>>>> Finish move in {round(time.perf_counter() - board_start_time)}sec \n")
    return round(time.perf_counter() - board_start_time)

async def main():
    tasks = []
    for i in range(oppenents):
        tasks +=[game(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} sec.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"Finish in {round(time.perf_counter() - start_time)} secs.")