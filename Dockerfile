# Use a slim Python image for a smaller footprint
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy only requirements file and application code
COPY requirements.txt ./
RUN pip install -r requirements.txt  # Install dependencies from requirements.txt

# Copy your application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Set entrypoint to run python
ENTRYPOINT ["python"]

# Use CMD to specify the application script
CMD ["app.py"]
