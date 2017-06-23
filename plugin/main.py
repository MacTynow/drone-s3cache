#!/usr/bin/env python

import drone
import boto3
import os
from s3cache import S3Cache


def main():
    """
    The main entrypoint for the plugin.
    """
    data = os.environ
    bucket = data["PLUGIN_BUCKET"]
    cache = data["PLUGIN_CACHE"].split(',')
    repo_name = data["DRONE_REPO_NAME"]
    commit_message = data["DRONE_COMMIT_MESSAGE"]

    if "[NO CACHE]" in commit_message:
        print "Found [NO CACHE] in commit message, skipping cache restore and rebuild!"
        return

    s3client = boto3.client("s3",
                aws_access_key_id=os.environ["PLUGIN_AWS_ACCESS_KEY_ID"],
                aws_secret_access_key=os.environ["PLUGIN_AWS_SECRET_ACCESS_KEY"])
    s3res = boto3.resource("s3",)
    s3cache = S3Cache()

    if data.has_key("PLUGIN_RESTORE") and data["PLUGIN_RESTORE"]:
        if "[CLEAR CACHE]" in commit_message:
            s3cache.clear(s3client, bucket, repo_name)
            return
        else:
            s3cache.restore(s3client, bucket, cache, repo_name)
    elif data.has_key("PLUGIN_REBUILD") and data["PLUGIN_REBUILD"]:
        s3cache.build(s3client, bucket, cache, repo_name)
    else:
        print "No restore or rebuild flag specified, plugin won't do anything!"


if __name__ == "__main__":
    main()
