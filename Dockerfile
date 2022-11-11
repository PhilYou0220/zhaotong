FROM python:3.9-slim-buster
WORKDIR /usr/local/zhaotong
COPY  . /usr/local/zhaotong
COPY requirements.txt requirements.txt
RUN pip3  install --trusted-host mirrors.aliyun.com --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple  -r requirements.txt
CMD ["python", "single_api_runall.py"]
