#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import setuptools

with open('README.md', 'r') as fh:
	desc = fh.read()

setuptools.setup(
	name = 'freggersbot',
	version = '1.0.42',
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
	install_requires=[
    	'requests',
		'py3amf'
    ],
	python_requires = '>=3.7'
)