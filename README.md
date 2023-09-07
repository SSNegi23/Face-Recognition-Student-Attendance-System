<h1 align="center"> Face Recognition Student Attendance System </h1>

# Introduction

This document provides an overview of the Face Recognition Student Attendance System built using Tkinter, MySQL, and the LBPH (Local Binary Pattern Histogram) Face Recognition algorithm. This system allows you to automate the attendance tracking process for students by recognizing their faces and generating attendance records in an Excel sheet.

# Table of Content

* [Features](#Features)
* [Requirements](#Requirements)
* [Installation](#Installation)
* [Usage](#Usage)
* [Database](#Database)
* [Face Recognition Algorithm](#Face-Recognition-Algorithm)
* [Attendance Generation](#Attendance-Generation)
* [Troubleshooting](#Troubleshooting)
* [Contributing](#Contributing)

# Features

- Student registration with details such as student ID, name, department, roll number, course, year, semester, and gender.
- Face data collection: The system captures 100 pictures of each student for training the face recognition model.
- Real-time face detection and recognition using the LBPH algorithm.
- Displaying the recognized student's name, ID, and department.
Automatic attendance generation in an Excel sheet.

# Requirements

- Python 3.x
- Tkinter library (usually included with Python)
- OpenCV library for face detection and recognition
- MySQL database for storing student information
- Xlsxwriter library for Excel sheet generation
- LBPH (Local Binary Pattern Histogram) Face Recognition algorithm

# Installation

1. Clone or download this repository to your local machine.
2. Install the required Python libraries using pip:
    * `pip install opencv-python-headless`
    * `pip install mysql-connector-python`
    * `pip install xlsxwriter`
3. Set up the MySQL database with the appropriate schema and credentials (details in the [Database](#Database) section).
4. Configure the database connection in the project code.


# Usage

1. Run the application by executing the main script, e.g., `python main.py`.
2. Register students by entering their details and capturing their face data.
3. Use the face recognition feature to take attendance.
4. Attendance records will be generated in an Excel sheet.

# Database

* The system relies on a MySQL database to store student information.
* You should create a database with the necessary tables (e.g., students) to store student details.
* Configure the database connection in the code to connect to your MySQL server.
* Ensure that the schema matches the database structure used in the code.

# Face-Recognition-Algorithm

* The system uses the LBPH (Local Binary Pattern Histogram) Face Recognition algorithm for real-time face detection and recognition.
* The LBPH algorithm is robust and capable of recognizing faces accurately.
* Ensure that OpenCV and the required libraries are installed for face recognition to work correctly.

# Attendance-Generation

* The system generates attendance records in an Excel sheet.
* Each attendance record includes the student's name, ID, department, etc.
* The Excel sheet can be further customized to suit your needs, such as adding date and time stamps.

# Troubleshooting

* If you encounter any issues or errors, please check the installation steps, database configuration, and library dependencies.
* Ensure that the LBPH Face Recognition algorithm is correctly installed and configured.

# Contributing

Contributions to this project are welcome. You can submit bug reports, feature requests, or even contribute code improvements via pull requests.