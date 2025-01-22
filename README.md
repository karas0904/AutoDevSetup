# Project Name: AutoDevSetup

## Description
This project is a streamlined tool for creating project directories, setting up virtual environments, and initializing GitHub repositories automatically. It simplifies the development process, saving time of going to YouTube again and again.

## Features
- **User-Friendly Interface**: A simple form to input project details.
- **GitHub Integration**: Automatically creates a repository on GitHub.
- **Local Setup**: Creates a project directory on your local machine.
- **Virtual Environment Setup**: Configures a Python virtual environment with essential dependencies.
- **User Info Display**: After creating the repo, all the info needed by the user is displayed on the web.


<h2>Installation</h2>

<ol>
  <li>Clone this repository:
    <pre><code>git clone https://github.com/your_github_username/your_project_name.git</code></pre>
  </li>
  <li>Navigate to the project directory:
    <pre><code>cd your_project_name</code></pre>
  </li>
  <li>Create a virtual environment:
    <pre><code>python -m venv venv</code></pre>
  </li>
  <li>Activate the virtual environment:
    <ul>
      <li>On macOS/Linux:
        <pre><code>source venv/bin/activate</code></pre>
      </li>
    </ul>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the application:
    <pre><code>uvicorn main:app --reload</code></pre>
  </li>
  <li>Open your browser and navigate to:
    <p>URL shown in the terminal.</p>
  </li>
</ol>


<h2>File Structure</h2>

<pre>
project_name/
├── backend/
│   ├── main.py             <!-- FastAPI application logic -->
│   ├── templates/          <!-- HTML templates (e.g., index.html) -->
│       ├── index.html
│   ├── static/             <!-- Static assets (CSS, JS) -->
│       ├── styles.css
│       ├── script.js
├── venv/                   <!-- Virtual environment folder -->
├── requirements.txt        <!-- Python dependencies -->
├── README.md               <!-- Documentation -->
</pre>

<h2>API Endpoints</h2>

<ul>
  <li><strong>GET /</strong>: Serves the homepage (form for project creation).</li>
  <li><strong>POST /create-project/</strong>: Processes form submission to create the project.</li>
</ul>

<h2>Screenshots</h2>
<h3>Initialpage</h3>
<img width="1512" alt="Image" src="https://github.com/user-attachments/assets/b5af1bce-e33b-42ef-bfec-c0cbbc082b5c" />
<h3>While creaing</h3>
<img width="1512" alt="Image" src="https://github.com/user-attachments/assets/2153c000-010a-4da2-97da-5bf591dbd3e8" />
<h3>When successfully created</h3>
<img width="1512" alt="Image" src="https://github.com/user-attachments/assets/2945b838-cbd4-4a91-9e52-82eb1e8ba25d" />

<h2>Troubleshooting</h2>
<h3>GitHub Repository Creation Fails:</h3>
<p>Ensure your GitHub token is correct and has the necessary permissions.</p>

<h2>Behind the Scenes: Data Flow and Architecture</h2>
<h3>High-Level Architecture</h3>
<h4>Frontend:</h4>
<p>The frontend consists of an HTML form styled with CSS and powered by JavaScript. When the user submits the form, JavaScript sends a POST request to the backend using <code>fetch</code>.</p>

<h4>Backend:</h4>
<p>The backend is built with FastAPI, which processes the POST request. It handles the following tasks:</p>
<ul>
  <li>Validating user inputs.</li>
  <li>Creating a local project directory.</li>
  <li>Setting up a virtual environment using Python's <code>venv</code> module.</li>
  <li>Initializing a GitHub repository using the provided token via GitHub's REST API.</li>
</ul>

<h4>Frontend Flow:</h4>
<ul>
  <li>User enters details in the form (project name, GitHub token, virtual environment name) and clicks "Create Project."</li>
  <li>JavaScript sends this data as a JSON object to the <code>/create-project/</code> endpoint.</li>
</ul>

<h4>Backend Flow:</h4>
<ul>
  <li>Receives the POST request containing project details.</li>
  <li>Executes the following steps:
    <ul>
      <li><strong>Step 1:</strong> Validates the input data.</li>
      <li><strong>Step 2:</strong> Creates a directory with the project name at the specified path.</li>
      <li><strong>Step 3:</strong> Sets up a Python virtual environment in the directory.</li>
      <li><strong>Step 4:</strong> Creates a GitHub repository using the provided token and links it to the local directory.</li>
    </ul>
  </li>
</ul>

<h4>Response:</h4>
<p>Upon successful execution, the backend sends a JSON response with:</p>
<ul>
  <li>Project name</li>
  <li>GitHub repository URL</li>
  <li>Local path</li>
  <li>Virtual environment name</li>
</ul>
<p>If an error occurs, an error message is returned.</p>

<h4>Frontend Response Handling:</h4>
<p>Updates the UI with the received response or displays an error message.</p>
