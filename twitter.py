import requests
import urlparse

new_exception(FramanTwitterException,Exception)

def tweet(public_token,secure_code,message):
    def_message=urlparse.quote(message)
    url="http://library.123go.it/post.php"
    response = requests.get(url,params={"tk":public_token, "msg":def_message, "auth_token":secure_code})
    if response.status==200:
        return True
    raise FramanTwitterException
