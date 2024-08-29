# Gunakan base image untuk Python
FROM python:3.11-slim

# Tentukan working directory di dalam container
WORKDIR /app

# Salin file requirements.txt dan install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Tentukan environment variable untuk Flask
ENV FLASK_APP=app.py

# Ekspos port 1778
EXPOSE 1778

# Perintah untuk menjalankan aplikasi Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=1778"]
