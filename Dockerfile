FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask whoosh PyPDF2

CMD ["python", "app.py"]