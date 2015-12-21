################################################################################
# Tweet with Viper
#
# Created by 123go.it
# Authors: S. Pira - F. Manetti
################################################################################

def tweet(twitter_id,public_token,auth_token,message):
        try:
            if(twitter_id)!="":
                print("TWEET: Connecting to library.123go.it ...")
                url="http://library.123go.it/post.php"
                def_message=message+" "+twitter_id.strip()
                print("Using Token: "+public_token)
                print("Sending Tweet: "+def_message)
                parameters={"tk":public_token, "msg":def_message, "auth_token":auth_token}
                response = requests.get(url,params=parameters)
            else:
                print("Invalid Twitter ID")
        except Exception as e:
            print(e)

        try:
            if(twitter_id)!="":
                if response.status==200:
                    print("Success!!")
                    print("-------------")
                    print(response.content)
                    print("-------------")
        except Exception as e:
            print("ooops, something went wrong! :(",e)
