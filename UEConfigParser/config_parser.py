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

    def write(self, output_path: str, newline_option='\n'):
        """
        Writes output to a file with the changes made
        :param output_path: Path to the output file
        :param newline_option: Newline character to use. Options: 'None','\n', '\r\n' (default: '\n')
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

    def modify(self, section: str, key: str, new_value: str, spacing=False):
        """
        Modifies the value of a key in a section
        :param section: Section name to modify
        :param key: Key name to modify
        :param new_value: New value to set
        :param spacing: Add space between key and the value (default: False)
        """
        in_section = False
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
            updated_lines.append(line)
        self.lines = updated_lines
    
    def disable_key(self, section: str, key: str):
        """
        Disables a key by commenting it out
        :param section: Section name to modify
        :param key: Key name to disable
        """
        in_section = False
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
            updated_lines.append(line)
        self.lines = updated_lines

    def enable_key(self, section: str, key: str):
        """
        Enables a key by uncommenting it
        :param section: Section name to modify
        :param key: Key name to enable
        """
        in_section = False
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
            updated_lines.append(line)
        self.lines = updated_lines

    def display(self):
        """
        Prints the lines to the console
        """
        for line in self.lines:
            print(line, end='')