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
    
    name="テスト１"
    key="test1"
    chartEnabled="false"
    projectLeaderCanEditProjectLeader="false" 
    subtaskingEnabled="true"
    textFormattingRule="markdown"

    result = api.project.create(name, key, chartEnabled, projectLeaderCanEditProjectLeader, subtaskingEnabled, textFormattingRule)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()