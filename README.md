# KASA Smart Plug Automation

This scripts allows you to check the plug and see how much wattage is being consumed.
If the wattage falls under a certain threashold then it will turn off the smart plug.
You can customize the which smart plug, how requently to check and what is the minimum wattage.

I use this script every day to check to see if my car charger is finished charging my
car and if so then this smart plug turns off the power to the charger. My settings are
every 5 minutes check to see if the wattage is below 2.0 watts and if it is then turn off.

## Hardware Requirement

In order for this to work you will need "Kasa Smart WiFi Plug w/Energy Monitoring by TP-Link - Reliable WiFi Connection" which you can find at [Amazon](https://www.amazon.com/dp/B0178IC5ZY?ref_=cm_sw_r_cp_ud_dp_MYFHR4A41QSY05NYNYQA). You won't need a hub just plug it in and configure it using the "Kasa" app on your phone first. Then you will need the I.P address of this device. You can get that from your router. Unfortunately the app only shows you the
mac address which you can't use.

## Software Requirement

You will need to install Python 3.8 or above. After installing 
go to this folder and run command `pip install -r requirements.txt`  
This script was tested using Python 3.10.4

## Environment Variables

This script takes the configuration input from the environment variables. It is done this way 
so it can be deployed to docker, podman or other containers easily. If you are running this
locally then just your local environment variables.

```
SMART_PLUG_IP=192.168.1.18
CHECK_EVERY=5
MINIMUM_WATTAGE=2.0
```
  
`CHECK_EVERY` is how many minutes in between to wait to check again.

