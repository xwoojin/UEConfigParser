from setuptools import setup, find_packages

long_description = ''

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='ueconfigparser',
    version='1.1.9',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    description='ConfigParser (in text) created for read/edit/write Unreal Engine Config files',
    author='WooJin Kim',
    author_email='woojinian@gmail.com',
    url='https://github.com/xwoojin/UEConfigParser',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['ueconfig', 'xwoojin', 'config', 'parser', 'config parser', 'configparser', 'unreal engine', 'unreal config', 'unreal parser'],
    python_requires=">=2.7, <4",
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
