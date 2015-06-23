FROM python:2.7

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt
 
# set working directory to /app/
WORKDIR /app/
 
# install python dependencies
RUN pip install -r requirements.txt
 
# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

USER myuser
