from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = [
		line.strip()
		for line in f.readlines()
		if line.strip() and not line.strip().startswith("#")
	]

# get version from __version__ variable in themes/__init__.py
from themes import __version__ as version

setup(
	name="themes",
	version=version,
	description="app for themes",
	author="itsystematic",
	author_email="ahmeddesoky412@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
