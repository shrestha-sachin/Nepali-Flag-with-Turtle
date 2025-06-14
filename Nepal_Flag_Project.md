# Nepali Flag with Turtle Graphics

This project demonstrates how to draw the national flag of Nepal using Python's Turtle graphics module. The Nepali flag is unique as it's the only non-quadrilateral national flag in the world.

![Nepali Flag](flag.png)

## Overview

The program creates a detailed representation of Nepal's flag with:
- A blue outer border
- A red inner area
- A white crescent moon in the top portion
- A white sun/star symbol in the bottom portion

## Features

- Accurate geometric representation of Nepal's flag
- Proper coloring (blue border, red field, white celestial symbols)
- Custom drawing of the unique crescent moon and sun symbols
- Adjustable window size

## Requirements

- Python 3.x
- Turtle graphics module (included in standard Python library)

## Usage

Run the script with Python:

```bash
python nepali_flag.py
```

The flag will be drawn in a new window. Click anywhere in the window to close it when finished.

## How It Works

The code creates four separate turtle objects:
1. `out_border`: Draws and fills the blue outer border
2. `ins_border`: Creates the red inner area of the flag
3. `moon`: Draws the white crescent moon in the top section
4. `sun`: Draws the white sun/star in the bottom section

Each element is carefully positioned and drawn using mathematical calculations to ensure proper proportions.

## Code Structure

- Flag border creation with precise angles
- Mathematical approach to drawing complex shapes
- Proper use of fill methods for coloring
- Efficient use of turtle graphics commands

## Author

Created by @Sachin-Shrestha