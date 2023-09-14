import epson_projector as epson
from epson_projector.const import (VOL_UP, VOL_DOWN, PWR_OFF, PWR_ON)
import time
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)

# host = input('Enter IP Address: ')
host = "172.16.16.145"

async def run(websession):  
    up = True
    while True:
        for _ in range(20):
            projector = epson.Projector(
                host=host,
                websession=websession)
            data = await projector.send_command(VOL_UP if up else VOL_DOWN)
            print(data)
            time.sleep(0.5)
        up = not up

asyncio.get_event_loop().run_until_complete(main()) 

# 172.16.16.145