import os
import time
import asyncio

from kasa import SmartPlug

ip = os.environ.get('SMART_PLUG_IP', 'missing')
check_every_seconds = int(os.environ.get('CHECK_EVERY', '1'))
minimum_wattage = float(os.environ.get('MINIMUM_WATTAGE', '2.0'))
check_every_seconds *= 60

if ip == 'missing':
  print('Missing IP address')
  exit(0)

print("Booting up smart plug automate\n")
print(f"Smart Plug I.P: {ip}")
print(f"Smart Plug check every {check_every_seconds} seconds")
print(f"Smart Plug minimum watt: {minimum_wattage}")


"""Check to see if the outlet needs to be turned off"""
async def check() -> None:
  sp = SmartPlug(ip)
  await sp.update()

  print()
  print(f"Checking: {sp.alias}")  # Print out the device labeled by the user

  if sp.is_on:
    watt_consumption = sp.emeter_realtime.power

    if watt_consumption > minimum_wattage:
      print(f"Still charging at {watt_consumption} watts")

    else:
      print('Finished charging.')
      print('Turning off the outlet.')
      await sp.turn_off()

  else:
    print('The device is off')

  print()  


if __name__ == "__main__":
  while(True):
    asyncio.run(check())
    time.sleep(check_every_seconds)
    