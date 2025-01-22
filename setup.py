from setuptools import setup, find_packages

setup(
    name='srilanka',
    version='1.0.1',
    description='A comprehensive package for working with data about Sri Lanka, including provinces, districts, and cities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ishan Oshada',
    author_email='ishan.kodithuwakku.offical@gmail.com',
    url='https://github.com/ishanoshada/Srilanka',
    packages=find_packages(),
    keywords='Sri Lanka, provinces, districts, cities, data, utility',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Natural Language :: English',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/ishanoshada/Srilanka#readme',
        'Source': 'https://github.com/ishanoshada/Srilanka',
        'Tracker': 'https://github.com/ishanoshada/Srilanka/issues',
    },
)
