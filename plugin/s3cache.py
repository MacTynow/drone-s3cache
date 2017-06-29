#!/usr/bin/env python
"""
Cache build artifacts on s3 for drone.io
"""
import boto3
import os
import tarfile

class S3Cache:
    def build(self, s3client, bucket, sources, namespace):
        for path in sources:
            if os.path.exists(path):
                print "Rebuilding cache for %s..." % path

                tarname = namespace + ".tar.gz"
                tar = tarfile.open(tarname, "w:gz")
                tar.add(path)
                tar.close()

                target = ''.join([namespace, '/', tarname])
                s3client.upload_file(tarname, bucket, target)
            else:
                print "There is nothing to cache for %s" % path

        print "Done!"


    def restore(self, s3client, bucket, sources, namespace):
        for source in sources:
            print "Restoring cache for %s..." % source

            tarname = namespace + ".tar.gz"
            s3path = ''.join([namespace, '/', tarname])
            
            obj = s3client.list_objects(Bucket=bucket, Prefix=s3path)
            if obj.has_key("Contents"):
                s3client.download_file(bucket, obj["Contents"][0]["Key"], tarname)

                if not os.path.exists(source):
                    os.makedirs(source)

                tar = tarfile.open(tarname, "r:gz")
                tar.extractall()
                tar.close()
            else:
                print "There is no cache for %s" % source
                return "nocache"

        print "Done!"


    # Need to handle empty buckets
    def clear(self, s3client, bucket, namespace):
        print "Found [CLEAR CACHE] in commit message, clearing cache!"
        objs = s3client.list_objects(Bucket=bucket, Prefix=namespace)['Contents']
        for obj in objs:
            filepath = obj['Key']
            s3client.delete_object(Bucket=bucket, Key=filepath)
