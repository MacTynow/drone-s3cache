# drone-s3cache


Cache build artifacts on s3 for drone.io


## Credits 

This plugin is inspired by and contains bits of https://github.com/Drillster/drone-volume-cache. If you don't care about storing your cache somewhere else than on your host, then use their work!

## Overview

Run the plugin directly after installing requirements:

```bash
python plugin/main.py <<EOF
{
  "repo" : {
    "owner": "foo",
    "name": "bar",
    "full_name": "foo/bar"
  },
  "system": {
    "link_url": "http://drone.mycompany.com"
  },
  "build" : {
    "number": 22,
    "status": "success",
    "started_at": 1421029603,
    "finished_at": 1421029813,
    "commit": "9f2849d5",
    "branch": "master",
    "message": "Update the Readme",
    "author": "johnsmith",
    "author_email": "john.smith@gmail.com"
  },
  "vargs": {
    "region": "us-east-1",
    "bucket": "mybucket",
    "rebuild": "true",
    "cache": ["node_volumes", "vendor/bundle"]
  }
}
EOF
```

## Docker

Alternatively, run the plugin directly from a built Docker image:

```bash
docker run -i MacTynow/drone-s3cache <<EOF
{
  "repo" : {
    "owner": "foo",
    "name": "bar",
    "full_name": "foo/bar"
  },
  "system": {
    "link_url": "http://drone.mycompany.com"
  },
  "build" : {
    "number": 22,
    "status": "success",
    "started_at": 1421029603,
    "finished_at": 1421029813,
    "commit": "9f2849d5",
    "branch": "master",
    "message": "Update the Readme",
    "author": "johnsmith",
    "author_email": "john.smith@gmail.com"
  },
  "vargs": {
    "region": "us-east-1",
    "bucket": "mybucket",
    "rebuild": "true",
    "cache": ["node_volumes", "vendor/bundle"]
  }
}
EOF
```


## License

drone-s3cache is licensed under the Apache License. A copy is included
in this repository.
