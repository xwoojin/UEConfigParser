import os

class UnrealConfigParser:
    def __init__(self):
        """Constructor"""
        self.lines = []

    def read(self, file_path: str):
        """
        Reads text file and stores lines in self.lines
        :param file_path: Path to the file to read
        """
        if not os.path.exists(file_path):
            print(f'File not found: {file_path}')
            raise FileNotFoundError
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.lines = file.readlines()
        except Exception as e:
            print(f'File read error: ', end='') # Better to handle exception on separate print statement
            print(e)
            raise

    def write(self, output_path: str, newline_option=None):
        """
        Writes output to a file with the changes made
        :param output_path: Path to the output file
        :param newline_option: Newline character to use. Options: 'None','\n', '\r\n' (default: None)
        """
        if not os.path.exists(os.path.dirname(output_path)):
            try:
                os.makedirs(os.path.dirname(output_path))
            except Exception as e:
                print(f'Directory create error: {output_path}', end='')
                print(e)
        try:
            with open(output_path, 'w', encoding='utf-8', newline=newline_option) as file:
                file.writelines(self.lines)
            print(f'File written: {output_path}')
        except Exception as e:
            print(f'File write error: ', end='')
            print(e)
            raise

    def _is_section(self, line: str, section: str) -> bool:
        """
        Checks if the line is a section
        :param line: Line to check
        :param section: Section name to compare
        """
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
            return current_section == section
        return False

    def add_key(self, section: str, key: str, value: str):
        """
        Adds a key to a section
        :param section: Section name to add the key
        :param key: Key name to add
        :param value: Value to add
        """
        in_section = False
        updated_lines = []
        section_found = False
        for index, line in enumerate(self.lines):
            stripped = line.strip()
            if self._is_section(stripped, section):
                in_section = True
                section_found = True
            if in_section and (index + 1 == len(self.lines) or self.lines[index + 1].strip().startswith('[')):
                updated_lines.append(f"{key}={value}\n")
                in_section = False
            updated_lines.append(line)
        if not section_found:
            updated_lines.append(f'\n[{section}]\n{key}={value}\n')
        self.lines = updated_lines


    def remove_key(self, section: str, key: str):
        """
        Removes a key from a section
        :param section: Section name to remove the key
        :param key: Key name to remove
        """
        in_section = False
        key_found = False
        updated_lines = []
        for line in self.lines:
            stripped = line.strip()
            if self._is_section(stripped, section):
                in_section = True
            elif stripped.startswith('[') and stripped.endswith(']'):
                in_section = False
            if in_section and '=' in stripped and not stripped.startswith((';', '#')):
                current_key, value = map(str.strip, stripped.split('=', 1))
                if current_key == key:
                    key_found = True
                    continue

            updated_lines.append(line)

        if not key_found:
            print(f'{section} - {key} : does not exists')

        self.lines = updated_lines

    def modify(self, section: str, key: str, new_value: str, spacing=False):
        """
        Modifies the value of a key in a section
        :param section: Section name to modify
        :param key: Key name to modify
        :param new_value: New value to set
        :param spacing: Add space between key and the value (default: False)
        """
        in_section = False
        key_found = False
        updated_lines = []
        for line in self.lines:
            stripped = line.strip()
            if self._is_section(stripped, section):
                in_section = True
            elif stripped.startswith('[') and stripped.endswith(']'):
                in_section = False
            if in_section and '=' in stripped and not stripped.startswith((';', '#')):
                current_key, value = map(str.strip, stripped.split('=', 1))
                if current_key == key:
                    if spacing:
                        line = f'{key} = {new_value}\n'
                    else:
                        line = f'{key}={new_value}\n'
                    key_found = True

            updated_lines.append(line)

        if in_section and not key_found:
            print(f'{section} - {key} : does not exists')

        self.lines = updated_lines

    def comment_key(self, section: str, key: str):
        """
        Disables a key by commenting it out
        :param section: Section name to modify
        :param key: Key name to disable
        """
        in_section = False
        key_found = False
        exists = False
        updated_lines = []
        for line in self.lines:
            stripped = line.strip()
            if self._is_section(stripped, section):
                in_section = True
            elif stripped.startswith('[') and stripped.endswith(']'):
                in_section = False
            if in_section and '=' in stripped and not stripped.startswith((';', '#')):
                current_key, value = map(str.strip, stripped.split('=', 1))
                if current_key == key:
                    line = f'; {line}'
                    key_found = True
            if in_section and '=' in stripped:
                current_key, value = map(str.strip, stripped.split('=', 1))
                if current_key == key:
                    exists = True

            updated_lines.append(line)

        if exists:
            if not key_found:
                print(f'{section} - {key} : is already disabled')
            else:
                print(f'{section} - {key} : commented')
        else:
            print(f'{section} - {key} : does not exist')

        self.lines = updated_lines

    def uncomment_key(self, section: str, key: str):
        """
        Enables a key by uncommenting it
        :param section: Section name to modify
        :param key: Key name to enable
        """
        in_section = False
        key_found = False
        exists = False
        updated_lines = []
        for line in self.lines:
            stripped = line.strip()
            if self._is_section(stripped, section):
                in_section = True
            elif stripped.startswith('[') and stripped.endswith(']'):
                in_section = False
            if in_section and stripped.startswith(';') and '=' in stripped:
                uncommented_line = stripped[1:].strip()
                current_key, value = map(str.strip, uncommented_line.split('=', 1))
                if current_key == key:
                    line = uncommented_line + '\n'
                    key_found = True
            if in_section and '=' in stripped:
                uncommented_line = stripped[1:].strip()
                current_key, value = map(str.strip, uncommented_line.split('=', 1))
                if current_key == key:
                    line = uncommented_line + '\n'
                    exists = True
            updated_lines.append(line)
        if exists:
            if not key_found:
                print(f'{section} - {key} : is already enabled')
            else:
                print(f'{section} - {key} : uncommented')
        else:
            print(f'{section} - {key} : does not exist')

        self.lines = updated_lines

    def display(self):
        """
        Prints the lines to the console
        """
        for line in self.lines:
            print(line, end='')
