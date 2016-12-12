FROM python:2

COPY requirements.txt .

RUN apt-get update && apt-get install libpcap-dev -y
# python-dev libxml2-dev libxslt-dev
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
