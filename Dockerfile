# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . .

# Set the environment variables, if needed
# ENV VARIABLE_NAME value

# Expose the port on which the Flask app runs
EXPOSE 5001

# Start the Flask app when the container launches
CMD ["python", "app.py"]
