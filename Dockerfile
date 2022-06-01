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

COPY dist/yolov5_hse-0.1.1-py3-none-any.whl .
RUN  python3.9 -m pip install yolov5_hse-0.1.1-py3-none-any.whl
RUN python3.9 -m pip install streamlit

WORKDIR /app

COPY yolov5_stream_demo /app/

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["web_demo.py"]