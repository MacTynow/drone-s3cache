import boto3
import random
import string
import os
from moto import mock_s3
from plugin.s3cache import S3Cache


@mock_s3
class TestS3cache():
    client = boto3.client("s3", region_name="us-east-1")
    resource = boto3.resource("s3")
    s3cache = S3Cache()
    test_string = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64))


    def setup(self):
        self.client.create_bucket(Bucket="mybucket") 


    def test_s3cache_restore_empty_cache(self):
        response = self.s3cache.restore(self.client, "mybucket", ["tests/test_data"], "reponame")

        assert response == "nocache"


    def test_s3cache_build_cache(self):
        if not os.path.exists("tests/test_data/"):
            os.makedirs("tests/test_data/")

        with open("tests/test_data/test.txt", "w+") as f:
            f.write(self.test_string)

        self.s3cache.build(self.client, "mybucket", ["tests/test_data"], "reponame")
        response = self.resource.Object("mybucket", "reponame/tests/test_data/test.txt")

        assert self.test_string in response.get()["Body"].read().decode("utf-8")


    def test_s3cache_restore_cache(self):
        # Remove the file before checking the restore function
        os.remove("tests/test_data/test.txt")

        self.s3cache.restore(self.client, "mybucket", ["tests/test_data"], "reponame")
        test_file = open("tests/test_data/test.txt")

        assert self.test_string in test_file.read()


    def test_s3cache_clear_cache(self):
        self.s3cache.clear(self.client, "mybucket", "reponame")

        response = self.client.list_objects(Bucket="mybucket")

        assert response.has_key("Contents") == False
