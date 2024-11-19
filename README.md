# Tableau Workbook Extractor

![](https://github.com/SimonJahan/Tableau-Workbook-Extractor/blob/main/how_to.gif)

## Description

**Tableau Workbook Extractor** is a Python script designed to extract `.twb` files and all packaged contents from a `.twbx` (Tableau Workbook) file, read the base64-encoded images within the `.twb`, and decode them into a local directory. This script is especially useful for Tableau users who want to access and manage internal resources such as shape images.

## Features

- Automatically extracts the `.twb` file contained in a `.twbx` file.
- Decodes base64-encoded images and saves them to the local filesystem.
- Simple user interface via a file selection dialog (Tkinter).

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.7 or higher
- The following libraries:

  - `tkinter`: Integrated in Python, but may need installation depending on your environment.
  - `xml.etree.ElementTree`: Built-in to Python.
  - `base64`: Built-in to Python.
  - `zipfile`: Built-in to Python.

### Installing Dependencies

If Tkinter is not already installed, you can install it using your package manager:

#### On Ubuntu / Debian:
```bash
sudo apt-get install python3-tk
```

#### On MacOS with Homebrew:
```bash
brew install python-tk
```

#### On Windows:
Tkinter is usually included with standard Python installations. If it's missing, you can install it with the following steps:

1. Ensure that you have Python installed with the correct version (Python 3.7 or higher).
2. Open the command prompt and run:
   ```bash
   python -m pip install tk
   ```

If Tkinter is still not available after installation, you may need to repair or reinstall Python with the "tcl/tk and IDLE" option checked during the installation process.

### Explanation of Changes:

- **On Windows**: Since Tkinter is usually bundled with Python on Windows, I provided instructions to install it via `pip` in case it's missing. Additionally, I added a note about ensuring Tkinter is installed during Python's installation process.

## Installation

1. Clone this GitHub repository to your local machine:
   ```bash
   git clone https://github.com/your-username/TableauWorkbookExtractor.git
   cd TableauWorkbookExtractor
   ```

2. Make sure all required dependencies are installed.

## Usage

1. Run the main `extractor.py` script by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. A file selection dialog will appear, allowing you to choose a `.twbx` (Tableau Workbook) file.

3. The script extracts the `.twb` file, reads base64-encoded images, and stores them in a `Shape` subfolder within the extraction directory.

4. The decoded image files will be available in this directory, organized according to their internal structure.

## Project Structure

```
TableauWorkbookExtractor/
│
├── main.py            # Main script
├── README.md          # Documentation
├── LICENSE            # Licensing file
├── requirements.txt   # (Optional) List of dependencies for pip installation
├── utils/             # Utilities folder
    └── utils.py       # Utilities script
```

## Example Output

- After execution, if your `.twbx` file contains base64-encoded images, they will be extracted into a directory reflecting the structure defined in the `.twb` file.
- The output directory will look something like:

  ```
  output_directory/
  ├── workbook_name/
      ├── workbook_file.twb
      ├── Data/
      ├── Image/
      ├── Shape/
          ├── folder1/
              ├── image1.png
              └── image2.png
          ├── folder2/
              └── image3.png
  ```

## Customization

The script is designed to extract and decode images, but it can be modified to include additional features such as:

- Extracting other types of embedded files from a `.twbx`.
- Modifying the output directory structure.

## Authors

- [Simon JAHAN](https://github.com/SimonJahan)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

### Explanation of the sections:

1. **Description**: A brief explanation of what the script does.
2. **Features**: A quick list of the script's main capabilities.
3. **Prerequisites**: Information about the required libraries and the minimum Python version.
4. **Installation**: Instructions on how to clone the repository and install dependencies.
5. **Usage**: How to run the script and what to expect from it.
6. **Project Structure**: An overview of how the files are organized in the repository.
7. **Example Output**: A sample directory structure after the script is run.
8. **Customization**: Suggestions for extending the script's functionality.
9. **Contributions**: Encouraging contributions and pull requests.
10. **Authors** and **License**: Credits and licensing information.
