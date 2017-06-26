FROM python:3
 RUN apt-get -y update
 RUN apt-get -y install netcat

 ENV PYTHONPATH /code

 RUN mkdir /code

 WORKDIR /code

 ADD requirements.txt /code/
 ADD wait.sh /code/
 ADD prezi/ /code/prezi
 ADD db/ /code/db
 ADD yoyo.ini /code/

 RUN chmod +x wait.sh
 RUN pip install -r requirements.txt

 CMD ./wait.sh && python prezi/app.py
