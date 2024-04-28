# Use a more recent Python version
FROM python:3.12  

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies in one step
COPY requirements.txt .  
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8080 for the Flask app
EXPOSE 8080

# Use a simplified CMD to run the Flask app
CMD ["python", "app.py"]
