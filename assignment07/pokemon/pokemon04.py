import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def pokemon(file):
    # Read the contents of the JSON file
    async with aiofiles.open(file, mode='r') as f:
        contents = await f.read()
    
    # Load it into a dictionary and create a list of moves
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    # Open a new file to write the list of moves into
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_move.txt', mode='w') as f:
        await f.write('\n'.join(moves))
async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')
    
    task = [pokemon(pathlist) for pathlist in pathlist]

    await asyncio.gather(*task)
        

asyncio.run(main())
