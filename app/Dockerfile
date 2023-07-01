# 
FROM python:3.9

# 
WORKDIR /code

# copied separately to use cache
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src /code/src

# 
CMD ["python", "/code/src/main.py"]