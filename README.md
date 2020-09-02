


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Simple script which gathers a few informations (Windows version, host name, IP adress) and saves into the .xlsx file (Excel format).

## Technologies
- Python (of course),
- pandas,
- openpyxl.

## Setup
1. <a href="https://www.python.org/downloads/">Install Python</a> on your operating system.
2. Install dependencies(in virtual environment or globally):
    - download *"requirements.txt"* file;
    - cd to download folder;
    - use following command:
    ```
    pip install -r requirements.txt
    ```
2. Edit the *"audit.bat"* file with any text editor.
3. Now you have two options:

    - instead of "path\to\your\python.exe" phrase write the path 
      to your virtual environment with installed dependencies;

    - using your PATH environment variable, just replace above 
      phrase with "python" word, but you have to install all dependencies globally;
5. Save and run the "audit.bat" script!
