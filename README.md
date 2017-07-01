# drone-s3cache

[![CircleCI](https://circleci.com/gh/MacTynow/drone-s3cache.svg?style=svg)](https://circleci.com/gh/MacTynow/drone-s3cache)

Cache build artifacts on s3 for drone.io


## Credits 

This plugin is inspired by and contains bits of https://github.com/Drillster/drone-volume-cache. If you don't care about storing your cache somewhere else than on your host, then use their work!

## Overview

Run the plugin directly after installing requirements:

```bash
export PLUGIN_AWS_ACCESS_KEY_ID=accesskeyid
export PLUGIN_AWS_SECRET_ACCESS_KEY=secretaccesskey
export PLUGIN_BUCKET=drone-cache
export PLUGIN_REBUILD=true
export PLUGIN_CACHE=test
export DRONE_REPO_NAME=test
export DRONE_COMMIT_MESSAGE=test
python plugin/main.py
```

## Docker

Alternatively, run the plugin directly from a built Docker image:

```bash
docker run -e PLUGIN_AWS_ACCESS_KEY_ID=accesskeyid \
  -e PLUGIN_AWS_SECRET_ACCESS_KEY=secretaccesskey \
  -e PLUGIN_BUCKET=drone-cache \
  -e PLUGIN_REBUILD=true \
  -e PLUGIN_CACHE=test \
  -e DRONE_REPO_NAME=test \
  -e DRONE_COMMIT_MESSAGE=test \
  -i mactynow/drone-s3cache
```


## License

drone-s3cache is licensed under the Apache License. A copy is included
in this repository.
