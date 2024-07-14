from setuptools import setup, find_packages

setup(
    name='driver-customer-mapping',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'h3',
        'folium',
        'geopy',
        'requests',
        'polyline',
    ],
    entry_points={
        'console_scripts': [
            'run-mapping=scripts.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to map driver and customer locations using H3, folium, and OSRM API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/driver-customer-mapping',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
