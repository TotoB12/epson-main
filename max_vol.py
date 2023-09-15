import epson_projector as epson
from epson_projector.const import (EPSON_KEY_COMMANDS, CMODE_LIST, VOL_DOWN, VOL_UP)
import time
import asyncio
import aiohttp

print(EPSON_KEY_COMMANDS.keys())

async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)

# host = input('Enter IP Address: ')
host = "172.16.16.194"

async def run(websession):  
    up = True
    while True:
        for _ in range(20):
            projector = epson.Projector(
                host=host,
                websession=websession)
            data = await projector.send_command(VOL_UP if up else VOL_DOWN)
            #dict_keys(['PWR ON', 'PWR OFF', 'HDMILINK', 'PWR', 'SOURCE', 'CMODE', 'VOLUME', 'CMODE_AUTO', 'CMODE_CINEMA', 'CMODE_NATURAL', 'CMODE_BRIGHT', 'CMODE_DYNAMIC', 'CMODE_3DDYNAMIC', 'CMODE_3DCINEMA', 'CMODE_3DTHX', 'CMODE_BWCINEMA', 'CMODE_ARGB', 'CMODE_DCINEMA', 'CMODE_THX', 'CMODE_GAME', 'CMODE_STAGE', 'CMODE_AUTOCOLOR', 'CMODE_XV', 'CMODE_THEATRE', 'CMODE_THEATREBLACK', 'CMODE_THEATREBLACK2', 'VOL_UP', 'VOL_DOWN', 'MUTE', 'HDMI1', 'HDMI2', 'PC', 'VIDEO', 'USB', 'LAN', 'WFD', 'PLAY', 'PAUSE', 'STOP', 'BACK', 'FAST', 'IMGPROC_FINE', 'IMGPROC_FAST', 'LUMINANCE_ECO', 'LUMINANCE_NORMAL', 'MEMORY_1', 'MEMORY_2', 'MEMORY_3', 'MEMORY_4', 'MEMORY_5', 'MEMORY_6', 'MEMORY_7', 'MEMORY_8', 'MEMORY_9', 'MEMORY_10'])
            # data = await projector.send_command('CMODE_CINEMA')
            print(data)
            time.sleep(0.5)
        up = not up

asyncio.get_event_loop().run_until_complete(main()) 

# 172.16.16.194