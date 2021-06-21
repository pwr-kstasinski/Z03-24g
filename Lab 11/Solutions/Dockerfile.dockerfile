FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 CMD curl --fail 127.0.0.1:5001/healthcheck || exit 1
CMD [ "python", "DockerImage.py"]
