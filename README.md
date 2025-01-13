# UEConfigParser

An textfile reader that acts as INI parser that reads/modifies/writes ini files regardless of duplicate keys and special characters, comments.
This parser is specially designed for Unreal Engine configuration files.
Compatible with Python 2.7 and 3.x.

## Installation

pip install UEConfigParser

## Usage

from UEConfigParser import UnrealConfigParser

parser = UnrealConfigParser()  
parser.read('example.ini')  
parser.display()  

parser.modify('/Script/HardwareTargeting.HardwareTargetingSettings', 'AppliedTargetedHardwareClass', 'Mobile')  
parser.disable_key('DevOptions.Shaders', 'NeedsShaderStableKeys')  
parser.enable_key('ConsoleVariables', 'Slate.EnableGlobalInvalidation')  

newline_option = '\n'  # option: None, '\n' (LF), '\r\n' (CRLF)  
parser.write('example.ini', newline_option=newline_option)  

parser.display()  
