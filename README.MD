# Kubenator

The objective of this project is to provide a Python script that facilitates the customization of YAML templates by replacing variables with specific values. This is useful for dynamically generating configuration files based on YAML templates, allowing easy adaptation to different environments or configurations.


## Key Features

* Variable Replacement: The script allows the definition of variables and their values. It then replaces these variables in a YAML template, generating a customized configuration file.

* File Separation: The YAML template is stored in a separate file, making it easy to maintain and update without directly modifying the script.

* Result in a New File: The replacement result is saved in a new YAML file, preserving the original template and enabling the generation of multiple configurations with different sets of variables.

## Usage

 
 * Define Variables: Modify the variables dictionary in the script with the desired variable names and values for replacement.

* Locate the Template: Place your YAML template in a separate file in the same directory as the script. Adjust the input_yaml_file_path variable with the correct path to the template file.

* Specify Output File: Define the output_yaml_file_path variable with the path where you want to save the result.

* Run the Script: Execute the script in Python. The result will be saved in the specified file, and a message will be displayed indicating the location of the new file.

## Benefits

* Configuration Automation: Enables automated generation of configuration files tailored to different contexts or environments.

* Easy Maintenance: By separating the YAML template and variable values, maintenance and updates to the configuration are simplified.


