
# Program: Git and GitHub Workflow Automation

import subprocess


# Function to execute Git commands
def run_git_command(command):

    try:

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )

        print(result.stdout or "Command executed successfully.")

    except subprocess.CalledProcessError as error:

        print("Git command failed:")
        print(error.stderr)


# 1. Initialize Git repository
print("\n===== INITIALIZE REPOSITORY =====")

run_git_command(["git", "init"])


# 2. Check repository status
print("\n===== GIT STATUS =====")

run_git_command(["git", "status"])


# 3. Add files to staging area
print("\n===== STAGE FILES =====")

run_git_command(["git", "add", "."])


# 4. Commit changes
print("\n===== COMMIT CHANGES =====")

run_git_command([
    "git",
    "commit",
    "-m",
    "Initial Python project commit"
])


# 5. Create a feature branch
print("\n===== CREATE FEATURE BRANCH =====")

run_git_command([
    "git",
    "branch",
    "feature/python-practice"
])


# 6. Switch to feature branch
print("\n===== SWITCH BRANCH =====")

run_git_command([
    "git",
    "switch",
    "feature/python-practice"
])


# 7. Display available branches
print("\n===== AVAILABLE BRANCHES =====")

run_git_command(["git", "branch"])


# 8. Display commit history
print("\n===== COMMIT HISTORY =====")

run_git_command(["git", "log", "--oneline"])


# 9. Display remote repositories
print("\n===== REMOTE REPOSITORIES =====")

run_git_command(["git", "remote", "-v"])


print("\nGit workflow demonstration completed.")
