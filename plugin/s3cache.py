#!/usr/bin/env python
"""
Cache build artifacts on s3 for drone.io
"""
import boto3
import os


class S3Cache:
    # TODO: make sure it can namespace different project
    def build(self, s3client, bucket, sources):
        for path in sources:
            print "Rebuilding cache for %s..." % path
            for root,dirs,files in os.walk(path):
                for file in files:
                    filename = os.path.join(root, file)
                    s3client.upload_file(filename, bucket, filename)

    # TODO: make sure it can namespace different project
    def restore(self, s3client, bucket, sources, dest):
        for source in sources:
            print "Restoring cache for %s..." % dest
            
            dirname =  ''.join([dest[sources.index(source)], '/', source])
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            objs = s3client.list_objects(Bucket=bucket, Prefix=source)['Contents']
            for obj in objs:
                filepath = obj['Key']
                target = ''.join([dest[sources.index(source)], '/', filepath])
                s3client.download_file(bucket, filepath, target)

    def clear(self, s3client, bucket, namespace):
        print "Found [CLEAR CACHE] in commit message, clearing cache!"
        objs = s3client.list_objects(Bucket=bucket, Prefix=namespace)['Contents']
        for obj in objs:
            filepath = obj['Key']
            s3client.delete_object(Bucket=bucket, Key=filepath)
