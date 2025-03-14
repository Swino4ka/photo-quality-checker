# Photo Quality Checker

A Python application that analyzes a folder of photos and selects the best ones based on criteria such as open eyes, correct exposure (not overexposed), and overall good image quality. The program outputs the filenames classified as "good," "average," or "bad" in the command line.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Overview

This project uses OpenCV and pre-trained Haar cascade classifiers to detect faces and eyes in images, and simple histogram analysis to assess the exposure. The application reads images from a specified folder, processes each image, and then outputs the file names along with their ratings based on:
- Face and eye detection (ensuring two eyes are visible)
- Average brightness within a predefined acceptable range

## Features

- **Face and Eye Detection:** Uses Haar cascades (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) to determine if a face and both eyes are present.
- **Exposure Analysis:** Computes the average brightness of the image to evaluate exposure.
- **Rating System:** Classifies images as "good", "average", or "bad" based on detection results.
- **Command Line Output:** Prints out the filenames grouped by rating.
- **Modular Code:** Separated functions for image analysis in a `utils.py` file.


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/photo-quality-checker.git
   cd photo-quality-checker
   ```
2. **Install Dependencies:**

It is recommended to use a virtual environment. Then install the required packages:
pip install -r requirements.txt

## Usage Instructions

### 1. Prepare Your Images

Place the images you want to analyze into the `images/` folder. The program will process all image files with the following extensions:
- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`

Note: There are already test images prepared in the "images folder", delete them before running the aplication.

### 2. Run the Application

Open a terminal in the project's root directory and execute the main script by running:

```bash
python main.py
```

### 3. Output

The program processes each image and prints the following information to the command line:

- **Filename** along with its quality rating: `good`, `average`, or `bad`.
- **Average brightness** of the image (used to assess exposure).
- **Number of detected faces** (if any).

For example, the output might look like this:

```
photo1.jpg: good (average brightness: 120.5, detected faces: 1)
photo2.jpg: bad (average brightness: 60.2, detected faces: 0)
photo3.png: average (average brightness: 180.3, detected faces: 1)
```

### 4. Next Steps

- **Review the Results:** Manually review the filenames listed under each category to decide which images to keep.
- **Enhancements:** In future versions, you might add functionality to automatically move files into separate folders (e.g., `good/`, `average/`, `bad/`) or generate a detailed report.

Happy coding!



