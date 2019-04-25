from setuptools import setup

long_description=""" This library is a language checker for English with:

--Contextual Spell Checking
--Advanced Style Checking
--Intelligent Grammar Checking

and built for Python 3.7. 
It uses artificial intelligence and natural language processing technology to find your writing errors
and offer smart suggestions. The technology was developed by After the Deadline http://www.afterthedeadline.com/ 
and is available under the GNU General Public License. 
After the Deadline is available on WordPress.com as well as in libraries, plugins, add-ons, and 
extensions for a variety of platforms. See the Download or Developers page for more information on 
extensions and libraries. 
"""
	
setup(
	name='mystracher',
	version='0.1',
	description='A structure / Grammar checker for English - a Python wrapper 3.7 for ATD (After The Dateline)',
	long_description=long_description,
	url='https://github.com/Shahabks/mystracher',
	author='Shahab Sabahi',
	author_email='mysoltechnologyai@gmail.com',
	license='MIT',
	classifiers=[
	'Intended Audience :: Education',
	'Topic :: Utilities',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3.7',
	],
	keywords='praat speech signal processing phonetics',
	install_requires=[
	],
	packages=['mystracher'],
      zip_safe=False)
