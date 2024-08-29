#The docker file for the image pushed to docker hub for crane cloud deployment
# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port that the Django app will run on
EXPOSE 8080

# Set the entrypoint command to run the Django development server
CMD ["python", "serve.py"]

