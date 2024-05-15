#!/bin/bash

# Update and initialize git submodules
echo "Initializing and updating submodules..."
git submodule update --init --recursive

# Install system dependencies if needed

sudo apt-get update && sudo apt-get install -y ffmpeg

echo "Setup completed successfully."