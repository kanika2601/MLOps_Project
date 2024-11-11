# Step 1: Specify the Base Image
FROM tensorflow/tensorflow:latest-gpu  # or use 'tensorflow/tensorflow:latest'

# Step 2: Set the Working Directory
WORKDIR /app

# Step 3: Copy Project Files
# Copy the project files (code, dependencies, etc.) into the container
COPY . /app

# Step 4: Install Dependencies
# Install required Python packages listed in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Step 5: Environment Setup (Optional)
# Set environment variables for better reproducibility (if required by your model)
ENV MODEL_NAME="gan_model"

# Step 6: Define the Entry Point or Run Command
# This command will be executed when the container starts
CMD ["python", "train.py"]
