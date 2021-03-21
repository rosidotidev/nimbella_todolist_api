import nimbella
import json
import random

def main(args):
    appkey='tdlst'
    db = nimbella.redis()
    print('log A')
    username=args.get("username","")
    if username=='':
      return {"body":{"response":{"result":"error","description":"username not valid"}}}
    searchuser=search_user(username)
    print('log B')
    if searchuser:
      return {"body":{"response":{"result":"ok","code": searchuser['code'],"username":searchuser['username']}}}
    print('log C')
    n = random.randint(0,10000000)
    code="code-"+str(n)
    key = appkey+":user:"+code
    
    value = json.dumps({
    "username": username,
    "code": code})
    print('before save')

    rsuccess=db.set(key, value)
    print('after save')
    return {"body":{"response":{"result":"ok","code":code,"username":username}}}



def search_user(username):
    appkey='tdlst'
    db = nimbella.redis()
    keys = db.keys(appkey+":user:*")
    data = db.mget(keys)
    res_user=None
    for user in data:
      d = json.loads(user.decode('utf-8'))
      print(d)
      if username==d['username']:
        res_user=d    
    return res_user
