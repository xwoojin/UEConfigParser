# UEConfigParser

An INI parser that reads ini files regardless of duplicate keys and special characters, comments.
This parser is specially designed for Unreal Engine configuration files.  
Compatible with Python 2.7 and 3.x.

## Installation

pip install UEConfigParser

## Usage

from UEConfigParser import UnrealConfigParser

parser = UnrealConfigParser()

parser.read('example.ini')

parser.display()

parser.modify_value_by_key('SectionName', 'KeyName', 'NewValue')

parser.write('example.ini') 
