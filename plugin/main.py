#!/usr/bin/env python
"""
Cache build artifacts on s3 for drone.io
"""
import drone
import requests


def main():
    """
    The main entrypoint for the plugin.
    """
    # Retrives plugin input from stdin/argv, parses the JSON, returns a dict.
    payload = drone.plugin.get_input()
    # vargs are where the values passed in the YaML reside.
    vargs = payload["vargs"]

    # Formulate the POST request.
    data = payload["build"]
    response = requests.post(vargs["url"], data=data)
    response.raise_for_status()


if __name__ == "__main__":
    main()
