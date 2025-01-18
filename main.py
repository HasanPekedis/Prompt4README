import os

prompt = """
You are an expert technical writer skilled in creating professional README files for software projects. Write a comprehensive README file for the following project:

Project Details:

Project Name: [Your Project Name]
Description: [Provide a brief description of what the project does and its purpose.]
Features: [List the key features or functionalities of the project.]
Technologies Used: [Mention the technologies, frameworks, and tools used in the project.]
Installation Instructions: [Provide step-by-step instructions for setting up and running the project.]
Usage: [Include examples or details on how to use the project.]
Contributing: [Explain how others can contribute to the project.]
License: [Specify the license for the project, if any.]
Contact Information: [Provide your contact details for any questions or feedback.]
Requirements:

Use clear and concise language that is easy to understand.
Include headings and subheadings for organization.
Format the README using Markdown syntax (e.g., #, ##, ### for headers, and lists for steps or features).
Add placeholders where necessary (e.g., <placeholder> or [Your Text Here]).
Provide a sample table of contents if the README is lengthy.
Include code snippets or examples where appropriate, especially in the usage section.

"""

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

    # Markup languages
    ".html",  # HTML
    ".htm",  # HTML
    ".xml",  # XML
    ".xhtml",  # XHTML
    #".md",  # Markdown

    # Stylesheet languages
    ".css",  # CSS
    ".scss",  # SASS
    ".less",  # LESS

    # Scripting languages
    ".sh",  # Shell script
    ".bat",  # Batch file
    ".ps1",  # PowerShell
    ".lua",  # Lua

    # Configuration and data formats
    ".json",  # JSON
    ".yaml",  # YAML
    ".yml",  # YAML
    ".ini",  # INI
    ".toml",  # TOML
    ".cfg",  # Config
    ".env",  # Environment variables

    # Query languages
    ".sql",  # SQL
    ".graphql",  # GraphQL

    # Assembly languages
    ".asm",  # Assembly
    ".s",  # Assembly

    # Miscellaneous
    ".txt",  # Plain text
    ".log",  # Log files
    ".csv",  # CSV
    ".tsv",  # TSV
    ".tex",  # LaTeX
    ".bib",  # BibTeX
]

# List to store the matching files
matching_files = []

code_propmts = []

# Function to explore files recursively
def explore_files(directory):
    project_name = os.path.basename(directory)  # Get the name of the project folder (e.g., MyProject)

    for root, _, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()  # Get the file extension
            if file_extension in language_file_types:  # Check if it matches the predefined types
                matching_files.append(os.path.join(root, file))  # Store the full file path


def create_code_prompt_part(matching_files):
    for file_path in matching_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                print(f"--- Content of {file_path} ---")
                print(f.read())  # Read and print the content of the file
                print("\n")
        except Exception as e:
            print(f"Could not read file {file_path}: {e}")

        code_prompt = f""" There is file in {file_path} and it contains the following code:"""

        code_propmts.append(code_prompt)

        





# Explore the current directory
current_directory = os.getcwd()
explore_files(current_directory)

create_code_prompt_part(matching_files)

print(current_directory)

print(matching_files)

print(code_propmts)