# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies (the altair pinning is enforced by requirements.txt)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port on which Streamlit runs
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
