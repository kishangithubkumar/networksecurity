## it is used define configuration of project, such as dependencies, metadata, and more.

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            
            #Read lines from the files
            lines=file.readlines()
            ##process each line
            for line in lines:
                requirement = line.strip()
                ##Igonore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirement_lst

print(get_requirement())
                    
            
            
            