FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN sudo apt-get install -y supervisor
RUN sudo apt-get install -y nginx
RUN sudo apt-get install python3 virtualenv
RUN python3 -m virtualenv venv && bash -c "source venv/bin/activate"
RUN venv/bin/pip3 install -r requirements.txt
# RUN pip install -r requirements.txt
# COPY . /code/
COPY gunicorn.conf /etc/supervisor/conf.d/ 
COPY django.conf /etc/nginx/sites-available/ 
ADD . /code/