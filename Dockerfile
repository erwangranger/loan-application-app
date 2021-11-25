FROM python:latest


#COPY requirements.txt /app/requirements.txt
#COPY app.py /app/app.py
COPY * /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]