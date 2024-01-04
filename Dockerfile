FROM python:3.9

ADD api/core/FastApiService.py .

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/
CMD ["python", "./main.py"]
