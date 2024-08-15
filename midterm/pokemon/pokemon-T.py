import asyncio
import httpx
import time

async def get_pokemon(client, url, ability):
    start_time = time.perf_counter()
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()
    pokemons = [pokemon['pokemon']['name'] for pokemon in pokemon['pokemon']]
    print(pokemons)
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get ability={ability} {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = ['speed-boost', 'battle-armor']
        for ability in rand_list:
            url = f'https://pokeapi.co/api/v2/ability/{ability}'
            tasks.append(asyncio.create_task(get_pokemon(client, url, ability)))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(get_pokemons())
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous finish. Time taken: {end_time-start_time} seconds")