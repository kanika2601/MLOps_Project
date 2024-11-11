# Step 1: Choose the base image
FROM tensorflow/tensorflow:latest-gpu  # Use tensorflow/tensorflow:latest for CPU only

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your project files into the container
COPY . /app

# Step 4: Install required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt  # Make sure you have a requirements.txt file in your project

# Step 5: Define the command to run your GAN model
CMD ["python", "train.py"]  # Replace train.py with your main script name if different
