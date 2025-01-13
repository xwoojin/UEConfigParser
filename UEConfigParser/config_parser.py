from collections import defaultdict

class UnrealConfigParser:
    def __init__(self):
        self.lines = []
        self.data = defaultdict(lambda: defaultdict(list))

    def read(self, file_path):
        current_section = None
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.lines = file.readlines()
                for line in self.lines:
                    stripped = line.strip()
                    if not stripped or stripped.startswith((';', '#')):
                        continue
                    if stripped.startswith('[') and stripped.endswith(']'):
                        current_section = stripped[1:-1].strip()
                    elif '=' in stripped and current_section:
                        key, value = map(str.strip, stripped.split('=', 1))
                        self.data[current_section][key].append(value)
        except Exception as e:
            print('File read error: ', end='') # Better to print error message on separater print statement incase something goes wrong with exception
            print(e)
            raise

    def search_and_replace(self, search_phrase, replace_phrase):
        for section, keys in self.data.items():
            for key, values in list(keys.items()):
                if search_phrase in key:
                    new_key = key.replace(search_phrase, replace_phrase)
                    self.data[section][new_key] = self.data[section].pop(key)
                for i, value in enumerate(values):
                    if search_phrase in value:
                        self.data[section][key][i] = value.replace(search_phrase, replace_phrase)

    def modify_value_by_key(self, section, key, new_value):
        if section in self.data:
            if key in self.data[section]:
                self.data[section][key] = [new_value]

    def write(self, file_path, newline_option=None):
        try:
            with open(file_path, 'w', encoding='utf-8', newline=newline_option) as file:
                current_section = None
                written_keys = defaultdict(set)
                for line in self.lines:
                    stripped = line.rstrip('\n')
                    if stripped.startswith('['):
                        current_section = stripped[1:-1]
                        file.write(line)
                    elif '=' in stripped and not stripped.startswith((';', '#')):
                        if current_section:
                            key, _ = map(str.strip, stripped.split('=', 1))
                            if key in self.data[current_section] and key not in written_keys[current_section]:
                                values = self.data[current_section][key]
                                for value in values:
                                    file.write(f"{key}={value}\n")
                                written_keys[current_section].add(key)
                    else:
                        file.write(line)

                for section, keys in self.data.items():
                    if section != current_section:
                        file.write(f"\n[{section}]\n")
                    for key, values in keys.items():
                        if key not in written_keys[section]:
                            for value in values:
                                file.write(f"{key}={value}\n")
                print(f'File write: {file_path}')
        except Exception as e:
            print('File write error: ', end='')
            print(e)
            raise
    def display(self):
        for section, keys in self.data.items():
            print(f'[{section}]')
            for key, values in keys.items():
                for value in values:
                    print(f'{key}={value}')
            print()