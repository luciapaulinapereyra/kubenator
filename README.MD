# Kubenator

The objective of this project is to provide a Python script that facilitates the customization of YAML templates by replacing variables with specific values. This is useful for dynamically generating configuration files based on YAML templates, allowing easy adaptation to different environments or configurations.


## Key Features

* Variable Replacement: The script allows the definition of variables and their values. It then replaces these variables in a YAML template, generating a customized configuration file.

* File Separation: The YAML template is stored in a separate file, making it easy to maintain and update without directly modifying the script.

* Result in a New File: The replacement result is saved in a new YAML file, preserving the original template and enabling the generation of multiple configurations with different sets of variables.

## Requirements

- Python 3
- Flask

1. Clone this repository:

   ```bash
   git clone https://github.com/luciapaulinapereyra/kubenator.git
   cd kubenator
2. Install dependencies
   ```bash
   pip install flask

## Usage

1. Run the Flask application:
   ```bash
   python3 script.py
2. Open your browser and go to http://127.0.0.1:5000/.
3. Fill out the form with the desired values and click "Run Script".
4. Check the results.

## Project Structure
* `app.py`: Python code for the Flask application.
* `templates/index.html`: HTML template containing the form and user interface.
* `templates/`: Folder containing YAML template files.
* `results/`:  Folder where YAML files with replaced variables will be saved.
* `variables.json`: JSON file with default variables.

## Benefits

* Configuration Automation: Enables automated generation of configuration files tailored to different contexts or environments.

* Easy Maintenance: By separating the YAML template and variable values, maintenance and updates to the configuration are simplified.


