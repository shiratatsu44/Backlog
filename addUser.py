import base64
import json
from backlog.util import load_conf
from backlog.base import BacklogAPI

def main():
    """
    Load conf.yml
    """
    conf = load_conf("conf.yml")["backlog"]
    api = BacklogAPI(conf["space"], conf["api_key"])

    """
    Project API
    """
    # list project users
    # https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-list/
    print("# list project users")
    
    userId="shiratatsu"
    passowrd="shiratatsu"
    name="shiratatsu"
    mailAddress="shiratatsu.com@gmail.com" 
    roleType=1

    result = api.user.add(userId, passowrd, name, mailAddress, roleType)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()