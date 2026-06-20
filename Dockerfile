FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY static ./static
EXPOSE 8000
ENV AGENTCMDB_API_KEY=dev-agentcmdb-key
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
