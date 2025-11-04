# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Cloud Run expects
EXPOSE 8080

# Tell Streamlit to use port 8080 and listen on all network interfaces
ENV PORT 8080

# Streamlit needs this to work properly in container environments
ENV STREAMLIT_SERVER_PORT 8080
ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0
ENV STREAMLIT_SERVER_ENABLE_CORS false
ENV STREAMLIT_SERVER_HEADLESS true

# Command to run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
