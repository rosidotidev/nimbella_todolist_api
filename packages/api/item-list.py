import nimbella
import json
import random

def main(args):
    appkey='tdlst'
    db = nimbella.redis()
    print('log A')
    
    usercode=args.get("user-code","")
    if usercode=='':
      return {"body":{"response":{"result":"error","description":"user not valid"}}}
    items=search_items(usercode)
   
    print(items)
    return {"body":{"response":{"result":"ok","user-code":usercode,"items":[json.loads(i.decode('utf-8')) for i in items]}}}
    #return {"body":{"response":{"result":"ok","user-cod":usercode}}}



def search_items(user_code):
    appkey='tdlst'
    db = nimbella.redis()
    keys = db.keys(appkey+":item:"+user_code+":*")
    data = db.mget(keys)
    return data



