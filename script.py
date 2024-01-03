from flask import Flask, render_template, request
import re
import json

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        variables_json = request.form['variables']
        variables = json.loads(variables_json)

        templates = ["00_app.yml", "01_service.yml", "02_ingress.yml"]
        results = []

        for template in templates:
            yaml_file_path = f'./templates/{template}'
            output_yaml_file_path = f'./results/{template}'
            yaml_template = read_file(yaml_file_path)
            yaml_result = replace_variables(yaml_template, variables)
            write_file(output_yaml_file_path, yaml_result)
            results.append(f"El resultado ha sido guardado en {output_yaml_file_path}")

        return render_template('index.html', results=results)

    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)
