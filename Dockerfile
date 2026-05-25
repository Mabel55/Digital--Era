# Use the official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your project files (including your study_buddy_brain) into the container
COPY . .

# Open port 8000 for FastAPI
EXPOSE 8000

# Tell the container how to start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]