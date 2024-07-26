#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Select option 1 for python3 using update-alternatives
echo "Selecting option 1 for python3 using update-alternatives..."
echo 1 | update-alternatives --config python3

# Check if the command was successful
if [ $? -eq 0 ]; then
  echo "Python3 alternative successfully updated."
else
  echo "Failed to update python3 alternative."
  exit 1
fi
