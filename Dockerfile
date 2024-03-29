# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FASTAPI_APP main:app

# Run app.py when the container launches
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--reload", "main:app"]
