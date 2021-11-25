FROM python:latest

RUN pip install --upgrade pip

RUN adduser  worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker . .
RUN rm -rf ./database.db

#COPY requirements.txt /app/requirements.txt
#COPY app.py /app/app.py
#COPY * /app/

#WORKDIR /app

# RUN pip install -r requirements.txt

RUN ls -al

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
