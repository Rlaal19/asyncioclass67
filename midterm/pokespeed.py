import asyncio
import httpx
import time

async def get_pokemon_ability(client, url):
    print(f"{time.ctime()} - get {url}")
    res = await client.get(url)
    data = res.json()
    # Extract Pokémon with the given ability
    pokemons = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return pokemons

async def get_pokemons_speed_boost():
    list_ab = ['speed-boost', 'battle-armor']
    for i in list_ab:
        url = f'https://pokeapi.co/api/v2/ability/{i}'
        async with httpx.AsyncClient() as client:
            # Fetch Pokémon with "battle-armor" ability
            pokemons = await get_pokemon_ability(client, url)
            return pokemons

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons_speed_boost()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons with 'speed-boost'. Time taken: {end_time - start_time} seconds")
    print("\n".join(pokemons))

if __name__ == '__main__':
    asyncio.run(index())