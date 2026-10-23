# Not meant to be built: requirements.txt pins litellm 1.107.0, which PyPI has removed.
FROM python:3.12.0-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
