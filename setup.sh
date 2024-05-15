#!/bin/bash

echo "Starting submodule update..."
git submodule update --init --recursive

if [ $? -ne 0 ]; then
    echo "Failed to update submodules"
    exit 1
fi

echo "Submodule update completed"