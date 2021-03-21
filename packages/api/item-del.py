import nimbella
import json
import random

def main(args):
    appkey='tdlst'
    print('log A')
    
    usercode=args.get("user-code","")
    if usercode=='':
      return {"body":{"response":{"result":"error","description":"user not valid"}}}

    code=args.get("code","")
    if code=='':
      return {"body":{"response":{"result":"error","description":"item code not valid"}}}

    db = nimbella.redis()
    key = appkey+":item:"+usercode+":"+code
    db.delete(key)
  
    return {"body":{"response":{"result":"ok","code":code}}}





