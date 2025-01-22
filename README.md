# Project Name: AutoDevSetup

## Description
This project is a streamlined tool for creating project directories, setting up virtual environments, and initializing GitHub repositories automatically. It simplifies the development process, saving time of going to YouTube again and again.

## Features
- **User-Friendly Interface**: A simple form to input project details.
- **GitHub Integration**: Automatically creates a repository on GitHub.
- **Local Setup**: Creates a project directory on your local machine.
- **Virtual Environment Setup**: Configures a Python virtual environment with essential dependencies.
- **User Info Display**: After creating the repo, all the info needed by the user is displayed on the web.


Installation
Clone this repository:
git clone https://github.com/your_github_username/your_project_name.git

Navigate to the project directory:
cd your_project_name

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
On macOS/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the application:
uvicorn main:app --reload

Open your browser and navigate to:
localhost URL showing in the terminal

File Structure
project_name/
├── backend/
│   ├── main.py             # FastAPI application logic
│   ├── templates/          # HTML templates (e.g., index.html)
        ├──index.html
│   ├── static/             # Static assets (CSS, JS)
        ├──styles.css
        ├──script.js
├── venv/                   # Virtual environment folder
├── requirements.txt        # Python dependencies
├── README.md               # Documentation


API Endpoints
GET /: Serves the homepage (form for project creation).
POST /create-project/: Processes form submission to create the project.


Troubleshooting
GitHub Repository Creation Fails:
Ensure your GitHub token is correct and has the necessary permissions.



Behind the Scenes: Data Flow and Architecture
High-Level Architecture

Frontend:
The frontend consists of an HTML form styled with CSS and powered by JavaScript.
When the user submits the form, JavaScript sends a POST request to the backend using fetch.

Backend:
The backend is built with FastAPI, which processes the POST request.
It handles the following tasks:
Validating user inputs.
Creating a local project directory.
Setting up a virtual environment using Python's venv module.
Initializing a GitHub repository using the provided token via GitHub's REST API.

Frontend:
User enters details in the form (project name, GitHub token, virtual environment name) and clicks "Create Project."
JavaScript sends this data as a JSON object to the /create-project/ endpoint.

Backend:
Receives the POST request containing project details.
Executes the following steps:
Step 1: Validates the input data.
Step 2: Creates a directory with the project name at the specified path.
Step 3: Sets up a Python virtual environment in the directory.
Step 4: Creates a GitHub repository using the provided token and links it to the local directory.

Response:
Upon successful execution, the backend sends a JSON response with:
Project name
GitHub repository URL
Local path
Virtual environment name
If an error occurs, an error message is returned.

Frontend:
Updates the UI with the received response or displays an error message.

