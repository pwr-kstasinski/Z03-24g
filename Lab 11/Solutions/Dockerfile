FROM python

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s CMD curl --fail http://0.0.0.0:5000/healthcheck || exit 1

EXPOSE 5000

CMD [ "python3", "serwer.py" ]

