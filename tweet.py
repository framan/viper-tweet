################################################################################
# Tweet with Viper
#
# Created by 123go.it
# Authors: FraMan - SPira
################################################################################

def tweet(twitter_id,public_token,auth_token,message):
        try:
                if(twitter_id)!="":
                        print("TWEET: Connecting to library.123go.it ...")    
                        replaced_twitterid=twitter_id.replace("@","")
                        nospace_message=message.replace(" ","%20")
                        def_message=nospace_message+" @"+replaced_twitterid.strip()
                        print("Using Token: "+public_token)
                        print("Sending Tweet: "+def_message)
                        url="http://library.123go.it/post.php"
                        parameters={"tk":public_token, "msg":def_message, "auth_token":auth_token}
                        response = requests.get(url,params=parameters)
                else:
                        print("TWEET: Connecting to library.123go.it ...")
                        def_message=message.replace(" ","%20")
                        print("Using Token: "+public_token)
                        print("Sending Tweet: "+def_message)
                        url="http://library.123go.it/post.php"
                        parameters={"tk":public_token, "msg":def_message, "auth_token":auth_token}
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
