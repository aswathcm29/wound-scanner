# Use an official Python runtime as a parent image
FROM python:latest

# Setup the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 (Flask's default port)
EXPOSE 5000

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]