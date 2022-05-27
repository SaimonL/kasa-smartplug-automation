# KASA Smart Plug Automation

This scripts allows you to check the smart plug and see how much wattage is being consumed.
If the wattage falls under a certain threashold then it will turn off the smart plug.
You can customize the which smart plug, how requently to check and what is the minimum wattage.

I use this script every day to check to see if my car charger is finished charging my
car. Then this script turns off the power to the charger using the smart plug. 

My settings are as follows:
* Every 5 minutes check.
* Is the wattage below 2.0 watts?
* If so then turn off the smart plug.


## Requirements

### Hardware Requirement

In order for this to work you will need "Kasa Smart WiFi Plug w/Energy Monitoring by TP-Link - Reliable WiFi Connection" which you can find at [Amazon](https://www.amazon.com/dp/B0178IC5ZY?ref_=cm_sw_r_cp_ud_dp_MYFHR4A41QSY05NYNYQA). You won't need a hub just plug it in and configure it using the "Kasa" app on your phone first. Then you will need the I.P address of this device. You can get that from your router. Unfortunately the app only shows you the mac address which you can't use. This script works since this smart plug supports "Energy Monitoring" feature which is vitial.

### Software Requirement

You will need to install Python 3.8 or above. After installing 
go to this folder and run command `pip install -r requirements.txt`  
This script was tested using Python 3.10.4

## Running the script

### Environment Variables

This script takes the configuration input from the environment variables. It is done this way 
so it can be deployed to docker, podman or other containers easily. If you are running this
locally then just set your local environment variables.

Example
```
SMART_PLUG_IP=192.168.1.18
CHECK_EVERY=5
MINIMUM_WATTAGE=2.0
```

Replace the values on the right side of the "=" sign with your own.
  
`CHECK_EVERY` is how many minutes in between to wait to check again.

### Linux / MacOS

Again make sure that you have Python 3.8 or above installed and you ran `pip install -r requirements.txt`.

Type in the following:

```bash
export SMART_PLUG_IP=ip address of your device
export CHECK_EVERY=how many minutes to wait in-between checks
export MINIMUM_WATTAGE=minimum wattage before turning off the device

python outlet-automate.py
```

### Errors

If you get an error such as

```
kasa.exceptions.SmartDeviceException: Unable to connect to the device: <ip of your device>:
```

This means this script could not connect to your device because either you physically unplugged the device, or you typed the IP address wrong in the environment variable "SMART_PLUG_IP" or the smart plug is in different network.
