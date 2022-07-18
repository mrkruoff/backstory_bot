FROM python:3.9

WORKDIR /bot_build

ADD ./util/* ./util
ADD bot.py .

COPY requirements.txt /bot_build

RUN pip install -r requirements.txt

CMD ["python3", "./bot.py"]