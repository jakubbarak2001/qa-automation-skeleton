# Start with the official Playwright image (Python tag), updated to v1.54.0 to match dependencies.
FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

# Set the working directory
WORKDIR /app

# Copy requirement files first to leverage Docker's build cache
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt

# Install Python dependencies (Pytest, Allure-Pytest, linters, formatters)
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

# Install Node.js, npm, and Java (JRE) for Allure CLI report generation
RUN apt-get update && \
    apt-get install -y nodejs npm openjdk-17-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the Allure command-line tool globally using npm
RUN npm install -g allure-commandline

# Copy the rest of the application code
COPY . .
