import os
import requests
import subprocess
import sys
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="backend/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-project/")
async def create_project(
    project_name: str = Form(...),
    github_token: str = Form(...),
    env_name: str = Form(...),
):
    print(f"Received project_name: {project_name}, github_token: {github_token}, env_name: {env_name}")

    # Step 1: Create the project folder on the desktop
    desktop_path = os.path.expanduser("~/Desktop")
    project_path = os.path.join(desktop_path, project_name)

    if not os.path.exists(project_path):
        os.makedirs(project_path)

    # Step 2: Create the GitHub repository
    github_api_url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {github_token}"
    }
    data = {
        "name": project_name,
        "description": f"Repository for {project_name} project",
        "private": False
    }

    # Fetch GitHub username dynamically
    user_info_url = "https://api.github.com/user"
    user_response = requests.get(user_info_url, headers=headers)
    if user_response.status_code != 200:
        return JSONResponse(
            status_code=400,
            content={"error": f"Failed to fetch GitHub user info: {user_response.json().get('message', 'Unknown error')}"}
        )
    github_username = user_response.json()["login"]

    # Create GitHub repository
    response = requests.post(github_api_url, headers=headers, json=data)
    if response.status_code != 201:
        return JSONResponse(
            status_code=400,
            content={"error": f"Failed to create GitHub repository: {response.json().get('message', 'Unknown error')}"}
        )

    github_url = f"https://github.com/{github_username}/{project_name}"

    # Step 3: Set up the virtual environment
    def create_virtualenv(project_path, env_name):
        venv_path = os.path.join(project_path, env_name)
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
        pip_path = os.path.join(venv_path, "bin", "pip") if sys.platform != "win32" else os.path.join(venv_path, "Scripts", "pip")
        subprocess.run([pip_path, "install", "--upgrade", "pip"])
        subprocess.run([pip_path, "install", "fastapi"])
        return venv_path

    try:
        venv_path = create_virtualenv(project_path, env_name)
    except subprocess.CalledProcessError as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to create virtual environment: {str(e)}"}
        )

    # Step 4: Initialize Git repository and push to GitHub
    try:
        # Initialize Git repository
        subprocess.run(["git", "init"], cwd=project_path, check=True)

        # Add all files to the staging area
        subprocess.run(["git", "add", "."], cwd=project_path, check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_path, check=True)

        # Add the remote repository
        subprocess.run(["git", "remote", "add", "origin", github_url], cwd=project_path, check=True)

        # Rename the default branch to 'main'
        subprocess.run(["git", "branch", "-M", "main"], cwd=project_path, check=True)

        # Pull remote changes (if any) and rebase
        try:
            subprocess.run(["git", "pull", "origin", "main", "--rebase"], cwd=project_path, check=True)
        except subprocess.CalledProcessError:
            # If the remote repository is empty, this will fail. Ignore the error.
            pass

        # Push to GitHub
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=project_path, check=True)
    except subprocess.CalledProcessError as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to push to GitHub: {str(e)}"}
        )

    # Return a JSON response with the project details
    return JSONResponse(content={
        "project_name": project_name,
        "github_url": github_url,
        "local_path": project_path,
        "env_name": env_name,
    })