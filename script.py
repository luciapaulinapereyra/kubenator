import re
import json

def replace_variables(template, variables):
    for key, value in variables.items():
        template = re.sub(fr'\${key}\b', str(value), template)
    return template

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(output_file_path, content):
    with open(output_file_path, 'w') as file:
        file.write(content)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

templates = ["00_app.yml", "01_service.yml", "02_ingress.yml"]

for template in templates:
    yaml_file_path = f'./plantillas/{template}'
    output_yaml_file_path = f'./resultados/{template}'
    yaml_template = read_file(yaml_file_path)
    variables = read_json('./variables.json')
    yaml_result = replace_variables(yaml_template, variables)
    write_file(output_yaml_file_path, yaml_result)
    print(f"El resultado ha sido guardado en {output_yaml_file_path}")

