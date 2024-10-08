FROM python:3-alpine AS builder

WORKDIR /app

RUN python3 -m venv ror-docker-env
ENV VIRTUAL_ENV=/app/ror-docker-env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2
FROM python:3-alpine AS runner

WORKDIR /app

COPY --from=builder /app/ror-docker-env ror-docker-env
COPY app.py app.py

ENV VIRTUAL_ENV=/app/ror-docker-env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=app/app.py

EXPOSE 8080

CMD ["gunicorn", "--bind" , ":8080", "--workers", "2", "app:app"]