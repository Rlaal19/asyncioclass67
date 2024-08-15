import asyncio
import httpx
import time

async def get_pokemon_ability(client, ability_url):
    print(f"{time.ctime()} - get {ability_url}")
    resp = await client.get(ability_url)
    data = resp.json()
    # Extract Pokémon with the given ability
    pokemons = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return pokemons

async def get_pokemons_battle_armor():
    ability_url = 'https://pokeapi.co/api/v2/ability/battle-armor'
    async with httpx.AsyncClient() as client:
        # Fetch Pokémon with "battle-armor" ability
        pokemons = await get_pokemon_ability(client, ability_url)
        return pokemons

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons_battle_armor()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons with 'battle-armor'. Time taken: {end_time - start_time} seconds")
    print("Pokémon with 'battle-armor':")
    print("\n".join(pokemons))

if __name__ == '__main__':
    asyncio.run(index())