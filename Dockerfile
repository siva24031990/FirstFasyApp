FROM python
COPY . /app
WORKDIR /app
RUN pip install -r Requirements.txt
CMD ["python","main.py"]
