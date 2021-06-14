FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./server .

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 CMD curl -f http://localhost:5000/healthcheck || exit 1

CMD [ "python", "./server.py" ]