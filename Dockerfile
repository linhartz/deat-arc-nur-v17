
FROM python:3.11-slim

# nastavení pracovního adresáře
WORKDIR /app

# zkopíruj vše do kontejneru
COPY . /app

# aktualizace a instalace uvicorn + fastapi + dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir fastapi uvicorn[standard] pydantic

# Railway používá port 8000 implicitně
EXPOSE 8000

# start FastAPI serveru
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
