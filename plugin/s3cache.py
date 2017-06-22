#!/usr/bin/env python
"""
Cache build artifacts on s3 for drone.io
"""
import boto3
import os


class S3Cache:
    def build(self, s3client, bucket, sources, namespace):
        for path in sources:
            print "Rebuilding cache for %s..." % path
            for root,dirs,files in os.walk(path):
                for file in files:
                    filename = os.path.join(root, file)
                    target = ''.join([namespace, '/', filename])
                    s3client.upload_file(filename, bucket, target)


    def restore(self, s3client, bucket, sources, namespace):
        for source in sources:
            s3path = ''.join([namespace, '/', source])
            objs = s3client.list_objects(Bucket=bucket, Prefix=s3path)
            
            if objs.has_key("Contents"):
                print "Restoring cache for %s..." % source
                        
                if not os.path.exists(source):
                    os.makedirs(source)

                keys = objs['Contents']
                for obj in keys:
                    target = obj['Key'].strip(namespace + '/')
                    s3client.download_file(bucket, obj['Key'], target)
            else:
                print "There is no cache for %s" % source
                return "nocache"


    # Need to handle empty buckets
    def clear(self, s3client, bucket, namespace):
        print "Found [CLEAR CACHE] in commit message, clearing cache!"
        objs = s3client.list_objects(Bucket=bucket, Prefix=namespace)['Contents']
        for obj in objs:
            filepath = obj['Key']
            s3client.delete_object(Bucket=bucket, Key=filepath)
