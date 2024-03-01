#!/bin/bash

# Set the source and destination paths
source_path="research/data"
destination_path="$HOME/Dropbox/0_RUG_23_24/back_up"

# Check if the destination directory exists, if not create it
if [ ! -d "$destination_path" ]; then
    mkdir -p "$destination_path"
fi

# Copy the source directory to the destination directory, overwriting if needed
cp -r -f "$source_path" "$destination_path"

echo "Data backup completed!"