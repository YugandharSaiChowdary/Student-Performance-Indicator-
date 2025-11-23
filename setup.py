from setuptools import setup, find_packages


setup (
    name='ml_project',
    version='0.1',
    author='sai',
    author_email='yugandharsai2801@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)