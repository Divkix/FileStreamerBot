FROM ghcr.io/divideprojects/docker-python-base:latest
WORKDIR /app
COPY . .
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt \
    && pip install --disable-pip-version-check -r requirements.txt \
    && curl "https://arc.io/arc-sw.js" -o /app/WebStreamer/html/assets/static/arc-sw.js
ENTRYPOINT ["python3"]
CMD ["-m", "WebStreamer"]
