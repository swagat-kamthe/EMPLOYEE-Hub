# Use the official Python image from Docker Hub
FROM python:3.11.9

# Set environment variables for Python

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
# Set working directory in the container
WORKDIR /code

#RUN apt-get clean && apt-get vim -y && apt-get install default-libmyclient-dev -yy
ADD requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /code/

# Expose the port that Django runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
