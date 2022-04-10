FROM python:3.7-alpine
WORKDIR /MentiMeter-Slide-Scraper
RUN pip install requests
EXPOSE 5000
COPY . .
CMD ["python3", "main.py"]