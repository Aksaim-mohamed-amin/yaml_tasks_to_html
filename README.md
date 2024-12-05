# Task Renderer - GitHub Actions Example

This repository demonstrates how to use GitHub Actions to automate the process of rendering tasks from a YAML file into an HTML page. Every time the YAML file is updated, 
a GitHub Action is triggered that runs a Python script inside a Docker container to convert the task data into a styled HTML file.

## How It Works

1. **YAML File:** The tasks are defined in a `tasks.yaml` file in the repository. Each task includes a description and any other relevant data.
2. **Python Script:** A Python script (`render_tasks.py`) reads the YAML file and generates an HTML page that displays the tasks.
3. **GitHub Actions:** Whenever the `tasks.yaml` file is changed, a GitHub Action is triggered. This action builds a Docker container, runs the Python script inside the container, and outputs the rendered HTML file.
4. **GitHub Pages:** The HTML output can be deployed to GitHub Pages to view the tasks.
