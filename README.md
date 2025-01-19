# UnrealConfigParser Utility

This project provides a Python-based utility for handling configuration files in Unreal Engine workflows or other INI-style configurations. It offers a range of features to read, write, and modify configuration files programmatically.

## Features

- **Read and Write Configuration Files**: Seamlessly read and write configuration data.
- **Section and Key Management**: Add, remove, and modify keys in specific sections.
- **Value Matching and Replacement**: Modify values based on substrings or specific criteria.
- **Comment/Uncomment Keys**: Enable or disable keys in configuration files.

## Installation

<code>pip install ueconfigparser</code>

Ensure you have Python 2.7 or later installed.

## Usage

Here are some examples of how to use the utility.

### Example 1: Reading Configuration Files

```python
from ueconfigparser import UnrealConfigParser

# Initialize the parser
parser = UnrealConfigParser()

# Read a configuration file
parser.read('config.ini')

# Display contents
parser.display()
```

### Example 2: Writing to Configuration Files

```python
from ueconfigparser import UnrealConfigParser

# Initialize the parser
parser = UnrealConfigParser()

# Read and modify the configuration file
parser.read('config.ini')
parser.add_key('General', 'NewKey', 'NewValue')

# Write changes to a new file
parser.write('updated_config.ini')
```

### Example 3: Modifying a Key Value

```python
from ueconfigparser import UnrealConfigParser

# Initialize the parser
parser = UnrealConfigParser()

# Read the configuration file
parser.read('config.ini')

# set a key's value
parser.set('General', 'ExistingKey', 'UpdatedValue')

# Save the changes
parser.write('updated_config.ini')
```

### Example 4: Commenting and Uncommenting Keys

```python
from ueconfigparser import UnrealConfigParser

# Initialize the parser
parser = UnrealConfigParser()

# Read the configuration file
parser.read('config.ini')

# Comment a key
parser.comment_key('General', 'KeyToDisable')

# Uncomment a key
parser.uncomment_key('General', 'KeyToEnable')

# Save the changes
parser.write('updated_config.ini')
```

### Example 5: Replace Substring in a Section

```python
from ueconfigparser import UnrealConfigParser

# Initialize the parser
parser = UnrealConfigParser()

# Read the configuration file
parser.read('config.ini')

# Replace a substring in a section
parser.replace_substring_in_section('General', 'OldSubstring', 'NewSubstring')

# Save the changes
parser.write('updated_config.ini')
```

## API Reference

### `UnrealConfigParser`

#### Methods:

- **`read(file_path: str)`**
  - Reads a configuration file.
  - **Parameters**: `file_path` - Path to the file to read.

- **`write(output_path: str, newline_option=None)`**
  - Writes the modified configuration to a file.
  - **Parameters**:
    - `output_path` - Path to save the file.
    - `newline_option` - Newline character to use (default: `None`).

- **`add_key(section: str, key: str, value: str)`**
  - Adds a new key-value pair to a section.

- **`remove_key(section: str, key: str)`**
  - Removes a key from a section.

- **`set(section: str, key: str, new_value: str, spacing=False)`**
  - Modifies the value of a key in a section.

- **`comment_key(section: str, key: str)`**
  - Disables a key by commenting it out.

- **`uncomment_key(section: str, key: str)`**
  - Enables a key by uncommenting it.

- **`set_value_by_string_serach_in_section(section: str, match_substring: str, new_value: str)`**
  - Updates any key's value in a section if it matches a substring.

- **`set_value_by_string_search_in_value(section: str, key: str, match_substring: str, new_value: str)`**
  - Updates a key's value if it matches a specific substring.

- **`replace_value_by_string_search_in_value(section: str, key: str, match_substring: str, new_substring: str)`**
  - Replaces a substring in the value of a specific key.

- **`replace_value_by_string_search_in_section(section: str, match_substring: str, new_substring: str)`**
  - Replaces substrings in the values of all keys within a section.

- **`comment_key_by_string_search_in_value(section: str, key: str, match_substring: str)`**
  - Comments out a key if its value matches a specific substring.

- **`uncomment_key_by_string_search_in_value(section: str, key: str, match_substring: str)`**
  - Uncomments a key if its value matches a specific substring.

- **`comment_key_by_string_search_in_section(section: str, match_substring: str)`**
  - Comments out keys in a section if their values match a substring.

- **`uncomment_key_by_section_search(section: str, match_substring: str)`**
  - Uncomments keys in a section if their values match a substring.

- **`display()`**
  - Prints the current configuration to the console.

## Author

This project was created by WooJin Kim.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Please submit issues or pull requests to improve functionality or documentation.
