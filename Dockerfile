FROM python:2.7-alpine
ADD ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD ./app.py /code/app.py
CMD ["python", "app.py"]