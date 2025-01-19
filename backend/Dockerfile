FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install requiremnents
COPY pyproject.toml poetry.lock /
RUN pip install poetry==1.7.1
RUN poetry install --no-root

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
