FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# creates new app folder inside the container and cd to it
# RUN apt install libpq-dev gcc
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock .env ./

# Install dependencies
RUN poetry install 

# Copy project files
COPY python_ask_service /app/python_ask_service

# Expose the port the app runs on
EXPOSE 4000


# Run the application
# ENTRYPOINT ["bash"]
CMD ["poetry", "run", "flask","-A","python_ask_service.backend.app", "run", "--host=0.0.0.0","--port=4000"]
