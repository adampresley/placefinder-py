from distutils.core import setup

setup(
	name = "placefinder-py",
	version = "0.1",
	description = "Yahoo! BOSS PlaceFinder Python Client",
	author = "Adam Presley",
	author_email = "adam@adampresley.com",
	url = "https://github.com/adampresley/placefinder-py",
	py_modules = [ "placefinder" ],
	requires = [ "oauth2" ],
	provides = [ "placefinder" ],
	classifiers = [
		"Environment :: Web Environment",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Operating System :: OS Independent"
	]
)
