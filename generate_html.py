import yaml
from jinja2 import Template

# Load tasks from the YAML file
with open('tasks.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Simple HTML template
template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>To-Do Tasks</title>
</head>
<body>
    <h1>Task List</h1>
    <ul>
        {% for task in tasks %}
        <li>{{ task.title }} - status: {{ task.status }}</li>
        {% endfor %}
    </ul>
</body>
</html>
""")

# Render and save to index.html
html_output = template.render(tasks=data['tasks'])
with open("index.html", "w") as output_file:
    output_file.write(html_output)
