import nimbella
import json
import random

def main(args):
    appkey='tdlst'
    db = nimbella.redis()
    print('log A')
    item=args.get("content","")
    if item=='':
      return {"body":{"response":{"result":"error","description":"item not valid"}}}
    usercode=args.get("user-code","")
    if usercode=='':
      return {"body":{"response":{"result":"error","description":"user not valid"}}}
    
    print('log B')
    n = random.randint(0,10000000)
    code="code-"+str(n)
    key = appkey+":item:"+usercode+":"+code
    
    value = json.dumps({
    "item": item,
    "user-code": usercode,
    "code": code})
    print('before save')

    rsuccess=db.set(key, value)
    print('after save')
    return {"body":{"response":{"result":"ok","code":code}}}
