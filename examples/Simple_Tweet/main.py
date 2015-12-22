################################################################################
# Tweet with Viper
#
# Created by library.123go.it
# Authors: FraMan - SPira
################################################################################


# import streams 
import streams

# import the wifi interface
from wireless import wifi

from community.framan.twitter import twitter

# load the Photon wifi driver
# change the following import to use another network driver
from bcm43362 import bcm43362 as wifi_driver

streams.serial()

# init the wifi driver!
wifi_driver.auto_init()

# use the wifi interface to link to the Access Point
# change network name, security and password as needed
print("Establishing Link...")
try:
    # FOR THIS EXAMPLE TO WORK, "Network-Name" AND "Wifi-Password" MUST BE SET
    # TO MATCH YOUR ACTUAL NETWORK CONFIGURATION
    wifi.link("Network-Name",wifi.WIFI_WPA2,"Network-Pass")
except Exception as e:
    print("ooops, something wrong while linking :(", e)
    while True:
        sleep(1000)

# FOR THIS EXAMPLE TO WORK YOU NEED TO FOLLOW THE STEPS AT:
# ------> http://library.123go.it/twitter/   <-------
# and get your public token and your secret code!

public_token = "...here goes your public token..."
secret_code = "...here goes your secret code..."
tweet = "How cool is tweeting with a @particle Photon and @VIPER_IoT? :P"

try:
    twitter.tweet(public_token,secret_code,tweet)
except FramanTwitterException as e:
    print(e)

