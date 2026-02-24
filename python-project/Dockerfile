FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]

# Here we are writing COPY command in 2 layers (5th and 9th line) because
# it is a good practice to separate the installation of dependencies from the application code.
# if we write COPY . . in one layer, it will invalidate the cache for all layers
# whenever we change any file in the application code, even if the dependencies remain the same.
# This will lead to longer build times.