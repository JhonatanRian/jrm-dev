# Usando debian:bookworm-slim como base (versão leve do Debian)
FROM debian:bookworm-slim
LABEL maintainer="<@JRM_DEV>"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libpq-dev \
    libmagic-dev \
    uwsgi-core \
    gettext \
    uwsgi-plugin-python3 \
    git \
    ca-certificates \
#    postgresql-client \
#    nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the application code.
COPY . .

RUN uv sync --group prd --locked

RUN uv run python manage.py collectstatic --no-input
RUN uv run python manage.py compilemessages

COPY docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
