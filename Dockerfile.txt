# Use a slim version of the Python 3.11 image (smaller footprint)
FROM python:3.11-slim

# Install LibreOffice and unoconv
RUN apt-get update && \
    apt-get install -y libreoffice libreoffice-writer unoconv && \
    apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY . .

# Expose the port your Flask app runs on (optional, default Flask port is 5000)
EXPOSE 5000

# Specify the command to run your application
CMD ["python", "app.py"]
