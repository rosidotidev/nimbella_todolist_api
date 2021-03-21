# nimbella todolist serverless api
Nimbella API required to axpose CRUD services (using Redis as NoSql DB)
Once installed Nimbella platform you can use these commands in order to create all required actions
<br/>
cd <path_to_api_directory> <br/>

nim action create api/item-save item-save.py --web true <br/>
nim action create api/item-update item-update.py --web true <br/>
nim action create api/item-list item-list.py --web true <br/>
nim action create api/item-del item-del.py --web true <br/>
nim action create api/user-access user-access.py --web true <br/>
