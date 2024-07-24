import aiofiles
import asyncio
import json

# Directories for the API and move data
pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    # Read the contents of the JSON file
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()
    
    # Load it into a directory and create a list of moves.
    pokemon = json.loads(contents)
    print(pokemon['name']) 

# Run the asynchronous main function
asyncio.run(main())
