
FROM python:3.12-slim

ENV MONGO_DB_USERNAME=khizer-db
ENV MONGO_DB_PWD=password123

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3030

CMD ["python", "app.py"]
