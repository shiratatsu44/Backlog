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
    users = api.project.list_users("SampleProject")
    print(json.dumps(users, indent=2))


    """
    Wiki API
    """
    # list wikis
    # https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-list/
    print("# list wikis")
    wikis = api.wiki.list("SampleProject")
    print(json.dumps(wikis[0], indent=2))

    # get attachment
    # https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-attachment/
    print("# get attachment")
    wiki = [w for w in api.wiki.list("SampleProject") if len(w["attachments"]) > 0][0]
    attachment = api.wiki.get_attachment(
        wikiId=wiki["id"],
        attachmentId=wiki["attachments"][0]["id"])
    attachment["data"] = base64.b64encode(attachment["data"]).decode()
    print(json.dumps(attachment, indent=2))


if __name__ == "__main__":
    main()