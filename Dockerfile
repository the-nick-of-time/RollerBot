FROM python:3.8-alpine

RUN apk add gcc musl-dev
RUN pip install --no-cache discord.py dndice
RUN apk del gcc musl-dev

ADD rollerbot.py /
ADD app_token /

EXPOSE 443

CMD [ "python3", "/rollerbot.py" ]
