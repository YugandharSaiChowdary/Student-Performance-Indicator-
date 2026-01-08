from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
    
setup (
    name='ml_project',
    version='0.1',
    author='sai',
    author_email='yugandharsai2801@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)