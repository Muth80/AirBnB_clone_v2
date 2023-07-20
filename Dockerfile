FROM ubuntu:20.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Set up the working directory inside the container
WORKDIR /app

# Copy the required files to the container
COPY web_flask/ web_flask/

# Install Flask and other required packages
RUN pip3 install Flask

# Expose port 5000 for the Flask application
EXPOSE 5000

# Start the Flask application
CMD ["python3", "-m", "web_flask.__init__"]
