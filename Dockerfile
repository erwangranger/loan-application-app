FROM python:latest


COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

WORKDIR /app

RUN pip install -r requirements.txt


# Expose the default httpd port 80
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]