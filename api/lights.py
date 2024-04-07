import asyncio

from pywizlight import wizlight, PilotBuilder, discovery

async def getAllLights(network):
    bulbs = await discovery.discover_lights(broadcast_space=network)
    bulbList = []
    x = 0
    for bulb in bulbs:
        x += 1
        listMember = BulbListMember(bulb.ip,x)
        bulbList.append(listMember)
    return bulbList

def getAllLightsTest(network):
    bulbList = []
    for x in range(6):
        listMember = BulbListMember(f"192.168.254.{x}",x)
        bulbList.append(listMember)
    return bulbList


async def setLightColor(ip, red, green, blue):
    light = wizlight(ip)
    await light.turn_on(PilotBuilder(rgb = (red, green, blue)))


async def main():
    bulbs = await getAllLights("192.168.254.255")
    for bulb in bulbs:
        print(bulb.__dict__)

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
class BulbListMember:
    def __init__(self, ip, listNumber):
        self.ip = ip
        self.listNumber = listNumber
