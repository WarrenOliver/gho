#!/usr/bin/env python3

import subprocess
import re

def get_github_url():
    try:
        # Get the remote URL of the current Git repository
        remote_info = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Extract the URL using a regular expression
        match = re.search(r'origin\s+(https?://[^\s]+)', remote_info.stdout)
        
        if match:
            return match.group(1)
    except subprocess.CalledProcessError:
        return None

def open_github_in_browser():
    # Get the GitHub repository URL
    github_url = get_github_url()

    if github_url:
        # Open the GitHub URL in the default web browser
        subprocess.run(['open', github_url], check=True)
    else:
        print("Not a Git repository or unable to determine the repository URL.")

if __name__ == "__main__":
    open_github_in_browser()
#!/usr/bin/env python3

import subprocess
import re

def get_github_url():
    try:
        # Get the remote URL of the current Git repository
        remote_info = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Extract the URL using a regular expression
        match = re.search(r'origin\s+(https?://[^\s]+)', remote_info.stdout)
        
        if match:
            return match.group(1)
    except subprocess.CalledProcessError:
        return None

def open_github_in_browser():
    # Get the GitHub repository URL
    github_url = get_github_url()

    if github_url:
        # Open the GitHub URL in the default web browser
        subprocess.run(['open', github_url], check=True)
    else:
        print("Not a Git repository or unable to determine the repository URL.")

if __name__ == "__main__":
    open_github_in_browser()