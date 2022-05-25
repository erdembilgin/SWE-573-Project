FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# RUN python3 -m virtualenv venv && bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt
ADD . /code/
# EXPOSE 8000
# ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]