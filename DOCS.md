Write your plugin documentation here.

The following parameters are used to configuration the plugin's behavior:

* **aws_access_key_id** - The AWS key id used to push/pull from s3
* **aws_secret_access_key** - The AWS key used to push/pull from s3
* **region** - The AWS region hosting your bucket
* **bucket** - The s3 bucket name
* **restore** - Restore the cache (bool)
* **rebuild** - Rebuild the cache (bool)
* **cache** - list of directories to cache

The following is a sample drone-s3cache configuration in your 
.drone.yml file:

```yaml
notify:
  drone-s3cache:
    image: MacTynow/drone-s3cache
    aws_access_key_id: ${AWS_ACCESS_KEY_ID}
    aws_secret_access_key: ${AWS_SECRET_ACCESS_KEY}
    region: us-east-1
    bucket: drone-cache
    rebuild: true
    cache: 
      - node_volumes
      - vendor/bundle
```
