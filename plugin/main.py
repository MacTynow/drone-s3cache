#!/usr/bin/env python

import drone
import boto3
from s3cache import S3Cache


def main():
    """
    The main entrypoint for the plugin.
    """
    # Retrives plugin input from stdin/argv, parses the JSON, returns a dict.
    payload = drone.plugin.get_input()
    # vargs are where the values passed in the YaML reside.
    vargs = payload["vargs"]
    data = payload["build"]
    repo = payload["repo"]
    
    if "[NO CACHE]" in data["message"]:
        print "Found [NO CACHE] in commit message, skipping cache restore and rebuild!"
        return

    s3client = boto3.client("s3")
    s3cache = S3Cache()

    if vargs.has_key("restore") and vargs["restore"]:
        if "[CLEAR CACHE]" in data["message"]:
            s3cache.clear(s3client, vargs["bucket"], repo["name"])
            return
        else:
            s3cache.restore(s3client, vargs["bucket"], vargs["cache"], repo["name"])
    elif vargs.has_key("rebuild") and vargs["rebuild"]:
        s3cache.build(s3client, vargs["bucket"], vargs["cache"], repo["name"])
    else:
        print "No restore or rebuild flag specified, plugin won't do anything!"


if __name__ == "__main__":
    main()
