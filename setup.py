from setuptools import setup, find_packages

setup(
    name='UEConfigParser',
    version='0.0.1',
    description='ConfigParser created for read/edit/write Unreal Engine Config files',
    author='WooJin Kim',
    author_email='woojinian@gmail.com',
    url='https://github.com/xwoojin/UEConfigParser',
    install_requires=['configparser'],
    packages=find_packages(exclude=[]),
    keywords=['ueconfig', 'xwoojin', 'config', 'parser', 'unreal parser'],
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
