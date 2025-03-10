import os
import argparse

parser = argparse.ArgumentParser(description="Optional arguments.")
parser.add_argument("--path", type=str, help="Path of the project.")
args = parser.parse_args()


prompt = ""

code_prompts = []

language_file_types = [
    # Programming languages
    ".py",  # Python
    ".java",  # Java
    ".c",  # C
    ".cpp",  # C++
    ".cs",  # C#
    ".rb",  # Ruby
    ".go",  # Go
    ".rs",  # Rust
    ".swift",  # Swift
    ".kt",  # Kotlin
    ".php",  # PHP
    ".pl",  # Perl
    ".r",  # R
    ".m",  # MATLAB or Objective-C
    ".jl",  # Julia
    ".dart",  # Dart
    ".ts",  # TypeScript
    ".js",  # JavaScript
    ".txt",  # text

]

# Function to explore files recursively
def explore_files(directory):
    # List to store the matching files
    matching_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()  # Get the file extension
            if file_extension in language_file_types:  # Check if it matches the predefined types
                matching_files.append(os.path.join(root, file))  # Store the full file path

    return matching_files

def create_code_prompt_part(matching_files):
    for file_path in matching_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:

                code_prompt = f"""###There is file in {file_path} and it contains the following code:
                    {f.read()}
                \n"""

                code_prompts.append(code_prompt)
        except Exception as e:
            print(f"Could not read file {file_path}: {e}")


def update_prompt():
    global prompt
    prompt = f"""You are an expert technical writer skilled in creating professional README files for software projects. Write a comprehensive README file for the following project:

Project Details:

Project Name: [Your Project Name]
Description: [Provide a brief description of what the project does and its purpose.]
Table of Contents: [A list of sections in the README, making it easier to navigate.]
Features: [List the key features or functionalities of the project.]
Technologies Used: [Mention the technologies, frameworks, and tools used in the project.]
Installation Instructions: [Provide step-by-step instructions for setting up and running the project.][Make sure you understand how project runs]
Configuration: [optional][Information on any configuration settings, environment variables, or setup steps that need to be done before running the project.]
Usage: [Include examples or details on how to use the project.]

You will use this code parts to create the code prompt part of the README file:

{''.join(code_prompts)}
Requirements:
The project name should match the folder name of the project.
Use given code and understand project details.
Use clear and concise language that is easy to understand.
Include headings and subheadings for organization.
Format the README using Markdown syntax (e.g., #, ##, ### for headers, and lists for steps or features).
Add placeholders where necessary (e.g., <placeholder> or [Your Text Here]).
"""
    
if __name__ == "__main__":
        
    if args.path:
        current_directory = args.path
    else:
        current_directory = os.getcwd()

    project_name = current_directory.split("/")[-1]


    matching_files = explore_files(current_directory)

    create_code_prompt_part(matching_files)

    update_prompt()
    
    # Open the file in write mode
    with open(f"prompt_{project_name}.txt", "w", encoding="utf-8") as file:
        file.write(prompt)  # Write the string to the file


