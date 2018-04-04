FROM python:3

RUN pip install discord.py

ADD rollerbot.py /
ADD rolling/ /
ADD app_token /

EXPOSE 443

CMD [ "python3", "/rollerbot.py" ]
