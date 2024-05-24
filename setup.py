import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description= f.read()

setuptools.setup(
name='cnnClassifier',
version='0.0.0',
author='shubi2',
author_email='22mmca015hy@manuu.edu.in',
description='A small python package for cnn app',
long_description=long_description,
long_description_content='text/markdown',
url='https://github.com/shubi2/chicken-disease-classification.git',
projects_urls={
        'Bug Tracker':'https://github.com/shubi2/chicken-disease-classification.git/issues'
},
package_dir={'':'src'},
packages=setuptools.find_packages(where='src')
)