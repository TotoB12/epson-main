import epson_projector as epson
from epson_projector.const import (PWR_OFF)

import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)


async def run(websession):    
    projector = epson.Projector(
        host='',
        websession=websession)
    data = await projector.send_command(PWR_OFF)
    print(data)

asyncio.get_event_loop().run_until_complete(main()) 
