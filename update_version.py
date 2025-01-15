import re

def increment_version(file_path: str):
    """
    Increment the version in the given setup.py file by 0.0.1.

    :param file_path: Path to the setup.py file
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Match the version using a regex
        version_pattern = r"version=['\"](\d+)\.(\d+)\.(\d+)['\"]"
        match = re.search(version_pattern, content)

        if not match:
            print("Version not found in the setup.py file.")
            return

        # Extract the current version and increment the patch number
        major, minor, patch = map(int, match.groups())
        patch += 1
        new_version = f"{major}.{minor}.{patch}"

        # Replace the old version with the new one
        updated_content = re.sub(version_pattern, f"version='{new_version}'", content)

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Version updated to {new_version}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Path to your setup.py file
setup_file_path = 'setup.py'

# Increment the version
increment_version(setup_file_path)