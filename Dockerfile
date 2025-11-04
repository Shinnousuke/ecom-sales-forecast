# Use official Python image
FROM python:3.10-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install system dependencies (for statsmodels, numpy, matplotlib, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir streamlit pandas numpy matplotlib statsmodels scikit-learn

# Expose port for Cloud Run
EXPOSE 8080

# Set environment variable for Streamlit
ENV PORT 8080

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]
