# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install required tools (Apache Benchmark, hping3, Siege, etc.)
RUN apt update && apt install -y \
    apache2-utils hping3 slowhttptest siege wrk \
    tcpdump nmap curl net-tools iputils-ping \
    && apt clean

# Install Flask for web interface
RUN pip install flask

# Set up the Flask app (we'll write this in the next step)
COPY app.py /CBR-PTS-TLS/app.py

# Expose port for the web server (default port 5000 for Flask)
EXPOSE 5000

# Run the Flask web app
CMD ["python", "/CBR-PTS-TLS/app.py"]
