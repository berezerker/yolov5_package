FROM python:3.9 as builder
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    curl tar \
    && rm -rf /var/apt/archives \
    && rm -rf /var/lib/apt/lists
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install build
COPY . /data
COPY yolov5_hse/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt