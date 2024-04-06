import asyncio

from pywizlight import wizlight, PilotBuilder, discovery

async def getAllLights(network):
    """Sample code to work with bulbs."""
    # Discover all bulbs in the network via broadcast datagram (UDP)
    # function takes the discovery object and returns a list of wizlight objects.
    bulbs = await discovery.discover_lights(broadcast_space=network)
    bulbList = []
    for bulb in bulbs:
        bulbList.append(bulb.ip)

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