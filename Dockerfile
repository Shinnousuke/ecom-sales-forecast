# ==============================================
# 📦 Streamlit Sales Forecasting App - Dockerfile
# Works perfectly with Google Cloud Run (GCP)
# ==============================================

# 1️⃣ Base Image
FROM python:3.10-slim

# 2️⃣ Environment Settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# 3️⃣ Set Working Directory
WORKDIR /app

# 4️⃣ Copy all files into the container
COPY . /app

# 5️⃣ Install required system dependencies (for numpy, statsmodels, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    liblapack-dev \
    libblas-dev \
    && rm -rf /var/lib/apt/lists/*

# 6️⃣ Install Python dependencies
RUN pip install --no-cache-dir \
    streamlit \
    pandas \
    numpy \
    matplotlib \
    statsmodels \
    scikit-learn

# 7️⃣ Expose the port that Cloud Run uses
EXPOSE 8080

# 8️⃣ Command to run your Streamlit app
# (Replace app.py if your main file has a different name)
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]
