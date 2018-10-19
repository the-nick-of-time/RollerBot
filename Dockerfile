FROM python:3.5-alpine

RUN pip install discord.py

ADD rollerbot.py /
ADD rolling/ /
ADD app_token /

EXPOSE 443

CMD [ "python3", "/rollerbot.py" ]
