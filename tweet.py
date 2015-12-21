################################################################################
# Tweet with Viper
#
# Created by library.123go.it
# Authors: FraMan - SPira
################################################################################

def tweet(public_token,secure_code,message):
        try:
                print("TWEET: Connecting to library.123go.it ...")
                def_message=message.replace(" ","%20")
                print("Using Token: "+public_token)
                print("Sending Tweet: "+def_message)
                url="http://library.123go.it/post.php"
                parameters={"tk":public_token, "msg":def_message, "auth_token":secure_code}
                response = requests.get(url,params=parameters)
        except Exception as e:
                print(e)

        try:
            if response.status==200:
                print("Success!!")
                print("-------------")
                print(response.content)
                print("-------------")
        except Exception as e:
                print("ooops, something went wrong! :(",e)
