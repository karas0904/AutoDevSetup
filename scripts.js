// Theme Toggle (Dark Mode)
const themeToggle = document.getElementById("theme-toggle");
if (themeToggle) {
  themeToggle.addEventListener("change", () => {
    document.body.classList.toggle("dark-theme", themeToggle.checked);
  });
}

// Form Submission
document
  .getElementById("project-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    // Get form values
    const projectName = document.getElementById("project_name").value;
    const githubToken = document.getElementById("github_token").value;
    const envName = document.getElementById("env_name").value;

    // Validate inputs
    if (!projectName || !githubToken || !envName) {
      alert("Please fill out all fields.");
      return;
    }

    // Disable the submit button to prevent multiple submissions
    const submitButton = document.querySelector("#project-form button");
    submitButton.disabled = true;
    submitButton.textContent = "Creating Project...";

    // Prepare FormData for sending
    const formData = new URLSearchParams();
    formData.append("project_name", projectName);
    formData.append("github_token", githubToken);
    formData.append("env_name", envName);

    // Make API call to the backend
    try {
      const response = await fetch("/create-project/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded", // Set the correct Content-Type
        },
        body: formData, // Send URL-encoded form data
      });

      const data = await response.json(); // Parse JSON response

      // Handle API response
      const resultsDiv = document.getElementById("results");
      if (response.ok) {
        // Display success message and project details
        resultsDiv.innerHTML = `
        <h3>Project Created Successfully!</h3>
        <p><strong>Project Name:</strong> ${data.project_name}</p>
        <p><strong>GitHub Repository:</strong> <a href="${data.github_url}" target="_blank">${data.github_url}</a></p>
        <p><strong>Local Path:</strong> ${data.local_path}</p>
        <p><strong>Environment Name:</strong> ${data.env_name}</p>
      `;
      } else {
        // Display error message
        resultsDiv.innerHTML = `<p style="color: red;">Error: ${
          data.error || "Failed to create project"
        }</p>`;
      }
    } catch (error) {
      // Handle network or other errors
      console.error("Error:", error);
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = `<p style="color: red;">Error: ${
        error.message || "Something went wrong"
      }</p>`;
    } finally {
      // Re-enable the submit button
      submitButton.disabled = false;
      submitButton.textContent = "Create Project";
    }
  });
