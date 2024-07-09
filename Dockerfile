# deriving the python image
FROM python:3.8-slim

# creat a working director in Docker
WORKDIR /app

# copies all the source code into docker
COPY . /app

# install the libraries we need to execute the code
# OR Run pip install -r requirements.txt
RUN pip install pandas boto3

# tell docker to run the code
CMD ["python","main.py"]