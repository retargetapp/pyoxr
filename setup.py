from distutils.core import setup
install_requires = [
    'requests',
]

setup(
    name='pyoxr',
    packages=['pyoxr'],  # this must be the same as the name above
    version='0.1',
    description='Python client for openexchangerates.org',
    author='RetargetApp',
    author_email='peterldowns@gmail.com',
    url='https://github.com/retargetapp/pyoxr',  # use the URL to the github repo
    download_url='https://github.com/peterldowns/mypackage/archive/0.1.tar.gz',  # I'll explain this in a second
    keywords=['openexchangerate', 'client', 'api'],  # arbitrary keywords
    classifiers=[],
    install_requires=install_requires,
)
