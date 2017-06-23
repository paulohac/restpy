FROM python:3.5
 RUN apt-get -y update
 RUN apt-get -y install netcat

 ENV PYTHONPATH /code 
 
 RUN mkdir /code
 
 WORKDIR /code
 
 ADD requirements.txt /code/
 ADD wait.sh /code/
 ADD prezi/ /code/
 ADD db/ /code/  
 ADD yoyo.ini /code/
 
 RUN chmod +x wait.sh
 RUN pip install -r requirements.txt
  
 CMD ./wait.sh && python prezi/app.py
