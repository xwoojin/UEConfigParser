rmdir /s /q dist
update_version.py
python setup.py sdist bdist_wheel
python -m twine upload dist/*
pause