from setuptools import setup, find_packages

setup(
    name='my-python-project',
    version='0.1.0',
    description='A sample Python project for Snyk scanning',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my-python-project',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        'requests==2.25.1',
        'numpy==1.21.0',
        'pandas==1.3.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
