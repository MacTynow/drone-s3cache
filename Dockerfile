# Cache build artifacts on s3 for drone.io
#
#     docker build --rm=true -t MacTynow/drone-s3cache .

FROM alpine:3.6
MAINTAINER MacTynow <charles.martinot@gmail.com>

RUN apk -U add python py2-pip
RUN mkdir -p /opt/drone
COPY requirements.txt /opt/drone/
WORKDIR /opt/drone
RUN pip install -r requirements.txt
COPY plugin/ /opt/drone/plugin/

CMD ["python", "/opt/drone/plugin/main.py"]
