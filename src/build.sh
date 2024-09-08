#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Please install pip and rerun the script."
    exit 1
fi

# Install necessary dependencies
pip install -r requirements.txt

# Define paths
ICON_PATH="F:/Projects/Minsky/src/UI/icons/MinskyLogobig.ico"
MAIN_SCRIPT="F:/Projects/Minsky/src/main.py"
DATA_PATHS="F:/Projects/Minsky/src/Settings/data;data/"
STYLES_PATH="F:/Projects/Minsky/src/UI/styles;styles/"
ICONS_PATH="F:/Projects/Minsky/src/UI/icons;icons/"

# Run PyInstaller
pyinstaller --noconfirm --onedir --windowed --icon "$ICON_PATH" --name "Minsky" \
--add-data "$DATA_PATHS" --add-data "$STYLES_PATH" --add-data "$ICONS_PATH" \
"$MAIN_SCRIPT" --hidden-import=Settings.datapaths

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "MinskyBuild completed successfully."
    
    # Rename the dist directory
    if [ -d "dist" ]; then
        mv dist MinskyBuild
        echo "The 'dist' directory has been renamed to 'MinskyBuild'."
    else
        echo "The 'dist' directory was not found."
    fi
    
    # Remove the build directory
    if [ -d "build" ]; then
        rm -rf build
        echo "The 'build' directory has been deleted."
    else
        echo "The 'build' directory was not found."
    fi
else
    echo "MinskyBuild failed."
    exit 1
fi
