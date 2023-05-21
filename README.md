# py to exe

![image](https://github.com/ylp1455/.py-to-.exe/assets/115799462/6c0b00c9-ecb9-4b2a-9bac-48c220c3d72a)


## Overview
.py-to-.exe is a Python script that enables the conversion of Python (.py) files into executable (.exe) files on Windows. This repository provides the necessary files and instructions to facilitate this conversion process.

## Installation

1. **Python Installation**: Ensure that Python is installed on your system. If not, you can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone this repository to your local machine using the following command:<br>
  <code>  git clone https://github.com/ylp1455/.py-to-.exe.git </code>


3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the project directory:
  <code> cd .py-to-.exe</code>
  
  
4. **Install Dependencies**: Install the required dependencies by running the following command:
<code> pip install -r requirements.txt </code>


## Usage

To convert a Python script into an executable file, follow these steps:

1. **Place Python Script**: Move your Python script (.py) file into the project directory.

2. **Conversion Process**: Open a terminal or command prompt and navigate to the project directory.

3. **Run Conversion Script**: Execute the following command to convert the Python script into an executable:

<code> python compile.py your_script.py</code>


Replace `your_script.py` with the actual name of your Python script file.

4. **Conversion Progress**: The conversion process will begin, and you will see the progress in the terminal or command prompt.

5. **Generated Executable**: Once the conversion is complete, you can find the generated executable file (your_script.exe) in the `dist` directory within the project folder. This executable can be run on Windows machines without requiring Python to be installed.

**Note**: If your script has any dependencies, the `pyinstaller` package will attempt to include them automatically. However, in certain cases, additional steps may be necessary to handle external dependencies.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



