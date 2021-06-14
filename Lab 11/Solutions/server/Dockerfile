FROM python

WORKDIR /server

ADD ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

#ENV DB_CONNECT_STR=mysql+pymysql://serverusr:spass@mdb/usrnmess

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 CMD curl --fail http://localhost:5000/healthcheck || exit 1

CMD [ "python", "server.py" ]
#CMD [ "pip", "freeze" ]