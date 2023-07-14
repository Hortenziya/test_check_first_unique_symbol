FROM python:3.9

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY templates templates
COPY main.py .

EXPOSE 6001
CMD ["python", "main.py"]
