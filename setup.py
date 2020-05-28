import setuptools

with open('README.md', 'r') as fh:
	desc = fh.read()

setuptools.setup(
	name = 'freggersbot',
	version = '1.0.14',
	author = 'Jan K',
	author_email = 'contact@jandev.net',
	license = 'MIT',
	keywords = 'freggers bot',
	description = 'A bot for freggers.de',
	long_description = desc,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/Jan000/Python-Freggers-Bot',
	packages = setuptools.find_packages(),
	classifiers = [
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop'
	],
	python_requires = '>=3.7'
)