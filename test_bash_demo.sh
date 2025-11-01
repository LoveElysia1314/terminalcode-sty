#!/bin/bash
# Test script: colorful terminal output demonstration
# Shows file types, colors, and symlinks with tree
mkdir -p colorful_demo && cd colorful_demo
touch normal_file.txt image.jpg archive.zip
mkdir directory_folder
echo "test" > executable_file && chmod +x executable_file
ln -s normal_file.txt symlink_file
tree
cd .. && rm -rf colorful_demo
