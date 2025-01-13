from setuptools import setup, find_packages

setup(
    name='UEConfigParser',
    version='1.0.1',
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
