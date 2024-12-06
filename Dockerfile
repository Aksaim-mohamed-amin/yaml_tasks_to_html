FROM python:3.13-slim

WORKDIR /app
COPY . /app
RUN pip install PyYAML Jinja2

CMD ["python", "generate_html.py"]
