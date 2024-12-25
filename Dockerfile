# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Flask API
EXPOSE 5000

# Define the entrypoint for the container
CMD ["python", "src/app.py"]