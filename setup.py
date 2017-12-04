from setuptools import setup

setup(name='bendford_py',
      version='0.1.0',
      description='A library for testing data sets with Bendford\'s Law',
      url='https://github.com/milcent/benford_py',
      download_url=
        'https://github.com/milcent/benford_py/archive/v0.1.0.tar.gz',
      author='Marcel Milcent',
      author_email='marcelmilcent@gmail.com',
      license='GPLv3.0',
      packages=['bendford'],
      install_requires=[
      	'pandas',
      	'numpy',
      	'matplotlib',
      ],
      zip_safe=False)
