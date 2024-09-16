# ![favicon-32x32](https://github.com/user-attachments/assets/a5049736-ded2-4590-b5c0-f5183cb945ed) Python Batch Image Tools

A repository containing useful Python scripts for performing batch image processing tasks. These scripts allow you to efficiently convert, rename, and apply watermarks to images in bulk, streamlining workflows that involve large numbers of images.

---

## Overview

This repository provides three batch image utility scripts:

1. **convert_images.py**: A tool for converting image formats (e.g., JPEG to PNG) in bulk.
2. **rename_images.py**: A script to rename images based on a numerical sequence.
3. **watermark_images.py**: Adds a watermark to multiple images at once.

Each of these tools is designed specifically for batch operations, allowing users to process multiple images simultaneously with minimal manual effort.

---

## Usage

To use these batch image tools, follow these steps:

1. Clone the repository.
2. Install the required dependencies using the instructions below.
3. Run the scripts based on your requirements. Each script will prompt you for specific options, such as image format, renaming pattern, or watermark details.

---

## Batch Image Utilities

### 1. `convert_images.py`

This script is designed to convert a large number of images from one format to another in a single operation. Supported formats include PNG, JPEG, BMP, TIFF, and more.

**How to use:**

- Run the script, and it will prompt you for the source directory, the output format, and the destination folder.
- Example: Convert all PNG files in a folder to JPEG.

**Features:**

- Automatically creates the target folder if it doesn't exist.
- Handles a variety of popular formats: `jpg`, `jpeg`, `png`, `gif`, `bmp`, `webp`.
- Provides detailed error messages for files that fail to convert.

### 2. `rename_images.py`

Use this utility to rename a batch of images in a numerical pattern. It is useful for organizing large numbers of images with numbered names.

**How to use:**

- After running the script, you’ll be asked for the source directory and your preferred renaming pattern (e.g., `image_001.jpg`, `photo_2024.jpg`).
- Example: Rename all images to follow a sequential pattern like `1`.png, `2`.png, etc.

**Features:**

- Renames all files sequentially in a folder.
- Skips directories and files that cannot be renamed.
- Displays renamed files and their new names as they are processed.

### 3. `watermark_images.py`

This script allows you to apply a watermark to multiple images at once, saving you time when branding or protecting images.

**How to use:**

- You will be prompted for the watermark image, its position (e.g., top-right, bottom-left), and the opacity level.
- Example: Apply a logo watermark to all images in a directory at the bottom-right corner with 50% opacity.

**Features:**

- Resizes watermark images to a specified dimension if needed.
- Supports positioning the watermark in various corners of the image (top-left, top-right, bottom-left, bottom-right).
- Handles transparent images (like PNG) efficiently.

---

## Dependencies

Before running the scripts, ensure all necessary Python libraries are installed. Use the following command to install dependencies:

```bash
pip install -r requirements.txt
