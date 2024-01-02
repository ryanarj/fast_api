FROM python:3.9

ADD main.py .

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/
CMD ["python", "./main.py"]
