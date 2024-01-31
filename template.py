import os
from pathlib import Path #this will directly convert to windows path like forward slashes to backward slashes 
import logging


# Information level logging, it will save time stamp and error message
logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(message)s:')

#we will create one folder called src, that will create mlproject and all folder structure in that
project_name = "mlProject"

list_of_files = [

    #we need this for CI/CD deployment using github action, to commit code empty folder can be pushed so gitkeep is required
    ".github/workflows/.gitkeep",

    # all constructor files are needed inside the mlproject folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",

    #here all configuration of project is stored
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",

    #
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"

]

# creating for loop to create files, PATH is used to convert the file location into windows operatable format
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
