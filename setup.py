from setuptools import setup, find_packages

setup(
    name='autodep',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    description='Automatic dependency handling for Python scripts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Doogich',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/autodep',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
