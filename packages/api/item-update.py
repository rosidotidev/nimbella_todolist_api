import nimbella
import json

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

    code=args.get("code","")
    if code=='':
      return {"body":{"response":{"result":"error","description":"item code not valid"}}}
    
    print('log B')
    key = appkey+":item:"+usercode+":"+code
    to_update=search_item(key)
    print(to_update)
    if to_update==None:
      return {"body":{"response":{"result":"error","description":"item not present"}}}

    value = json.dumps({
    "item": item,
    "user-code": usercode,
    "code": code})
    print('before save')

    rsuccess=db.set(key, value)
    print('after save')
    return {"body":{"response":{"result":"ok","code":code}}}

def search_item(key):
  db = nimbella.redis()  
  value = db.get(key)  
  return value 
