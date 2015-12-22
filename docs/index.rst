****************
Tweet with VIPER
****************

**A simple library to tweet with your viperized board in 6 steps!**

Be advised that this library does not tweet directly from your VIPERIZED board. It sends your tweets to our website (library.123go.it) that then tweets it from there. 

Username/password will NOT be sent to the site by OAuth mechanism. Our server stores the Public/Private couple of Tokens released from twitter during the authorization procedure. You can invalidate the OAuth token for this library anytime at http://twitter.com/settings/connections.

A simple 6 steps guide to authorize our "Tweet with VIPER" APP to tweet with your account is available at http://library.123go.it/twitter/index.html.
 

===========
Description
===========

Tweet with VIPER Library is a library for VIPER to tweet on Twitter.

With this library you can automate posting on twitter from your viperized board.

Tweets are sent via a shared server, through our "Twitter with Viper" APP.

-----
Setup
-----

Import the library in your python Code with: ::

	from community.framan.twitter import twitter

Connect your VIPERIZED board to internet choosing the right driver for your board from the repositories of VIPER.

Before tweeting, you have to follow the 6 steps guide here http://library.123go.it/twitter to authorize our "Tweet with VIPER" APP. Take note of the Public Token and of the Secret Code at the end of the procedure.

----------------
Your first Tweet
----------------

Tweet using the simple tweet() function: ::

	tweet(string public_token,string secure_code,string message)

*public_token*: your token received following the 6 steps guide described above.

*secure_code*: your secure code received following the 6 steps guide described above.

*message*: the tweet message (can contain a TAG or an HASHTAG).

Go to twitter.com and enjoy your first Tweet with VIPER

The library also include an example that shows how to tweet with a Particle Photon! You can clone it in the IDE or you can copy and paste from here: ::

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



--------------
Important Info
--------------

1. This library uses the http://library.123go.it shared server as a proxy server for OAuth. We store in our database your Private Token and your Public token to tweet with our Twitter APP with your twitter account through VIPER.
2. We are not responsible for any problems or malfunctions resulting from the use of our library.
3. Please avoid sending more than 2 tweets per minute.
4. Twitter rejects repeated tweets with the same content;
5. We would be very happy to receive your feedback here.
6. This library is distributed under the GNU GPL v2 license.
7. Twitter brand and Twitter logo are property of Twitter, Inc. Viper brand and logo are properties of Viper Embedded Technologies.
8. See also the `Viper Official site <http://www.viperize.it/>`_ and the `online documentation <http://library.123go.it/twitter/docs.html>`_ of the library
