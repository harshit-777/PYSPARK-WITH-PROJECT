


import tweepy
from tweepy import OAuthHandler , Stream 
from tweepy.streaming import StreamListener 
import socket 
import json 


consumer_key = '#############'
consumer_secret = '##################'
access_key = '#######################'
access_secret = '#######################'





class TweetListener(StreamListener):
    
    def __init__(self,csocket):
        self.client_socket = csocket
        
    def on_data(self,data):
        
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True 
        except BaseException as e :
            print('Error',e)
            return True 
        
    def on_error(selff,status):
        print(status)
        return True 


def sendData(c_socket):
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    
    twitter_stream = Stream(auth,TweetListener(c_socket))
    twitter_stream.filter(track=['guitar'])




if __name__=="__main__":
    s = socket.socket()
    host = '127.0.0.1'
    port = 9999
    s.bind((host,port))
    
    print('Listening on port 9999')
    s.listen(5)
    c,addr = s.accept()
    
    sendData(c)







