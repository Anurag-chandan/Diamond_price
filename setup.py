#tO RUN SETUP.PY -->python setup.py install

from setuptools import find_packages,setup
#For versioning we use setup
from typing import List



def get_requirements(file_path)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #readline will read all lines only once.
        requirements=[req.replace('\n'," ") for req in requirements]
        #Above we use list comprehension to remove character while reading requirements.txt

        

        return requirements




setup(
    name = "Diamondpricepredictions",
    version = '0.0.1',
    author='anurag',
    author_email = 'anurag25chandan@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    #Either we create a list of installer or give a file path to requirement.txt
    packages = find_packages()
)
