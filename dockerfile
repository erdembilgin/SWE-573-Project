FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m virtualenv venv && bash -c "source venv/bin/activate"
RUN venv/bin/pip3 install -r requirements.txt
# RUN pip install -r requirements.txt
# COPY . /code/
ADD . /code/