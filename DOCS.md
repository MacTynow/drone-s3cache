Write your plugin documentation here.

The following parameters are used to configuration the plugin's behavior:

* **url** - The URL to POST the webhook to.

The following is a sample drone-s3cache configuration in your 
.drone.yml file:

```yaml
notify:
  drone-s3cache:
    image: MacTynow/drone-s3cache
    url: http://mockbin.org/
```
