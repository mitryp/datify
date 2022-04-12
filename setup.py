import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='datify',
    packages=setuptools.find_packages(),
    version='1.0.5',
    license='Apache-2.0',
    description='Module that allows extracting valid date from user input.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Dmytro Popov',
    author_email='thedmitryp@ukr.net',
    url='https://github.com/mitryp/datify',
    download_url='https://github.com/mitryp/datify/archive/refs/tags/1.0.5.tar.gz',
    keywords=['str', 'string', 'user-experience', 'user-input', 'date', 'date-strings', 'datify', 'alpha-month',
              'month', 'english', 'russian', 'ukrainian', 'natural-language', 'open-source'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
