FROM python:3.10.4-alpine3.16

RUN python -m pip install --upgrade pip

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY outlet-automate.py outlet-automate.py

CMD [ "python", "outlet-automate.py" ]
