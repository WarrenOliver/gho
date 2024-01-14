#!/bin/bash

# Set the script path
SCRIPT_PATH="/home/warren-oliver/code/gho/gho.py"
NEW_SCRIPT_NAME="gho"

# Create a bin directory in the user's home directory if it doesn't exist
mkdir -p "$HOME/bin"

# Move the script to the bin directory
mv "$SCRIPT_PATH" "$HOME/bin/$NEW_SCRIPT_NAME.py"

# Make the script executable
chmod +x "$HOME/bin/$NEW_SCRIPT_NAME.py"

# Create a symbolic link without the extension
ln -s "$HOME/bin/$NEW_SCRIPT_NAME.py" "$HOME/bin/$NEW_SCRIPT_NAME"

# Add the bin directory to the PATH in the user's shell profile
echo 'export PATH="$PATH:$HOME/bin"' >> "$HOME/.bashrc"

# Notify the user
echo "The script has been installed as a global CLI application."
echo "Please restart your terminal or run 'source ~/.bashrc' to apply the changes."
echo "You can now use the command '$NEW_SCRIPT_NAME' to run your script."