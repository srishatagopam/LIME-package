from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Measurements',
    url='https://https://github.com/srishatagopam/LIME-package',
    author='Wei Ran',
    author_email='aeinrw@gmail.com',
    packages=['LIME-package'],
    install_requires=[numpy],
    version='0.1',
    license='MIT',
    description='Wrapper for LIME python implementation.',
)
