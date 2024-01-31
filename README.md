# End-to-End-DataScience-Project-with-MLFlow

## Create a Repository in github and clone it into local workspace

### Create a template.py file -> We need lots of files and folders, instead of creating manually we create a script, so whenever we run this anywhere we gethn the folder structure.

- from pathlib import Path #this will directly convert to windows path like forward slashes to backward slashes
- Information level logging, it will save time stamp and error message
- we will create one folder called src, that will create mlproject and all folder structure in that
- we need this for CI/CD deployment using github action, to commit code empty folder can be pushed so gitkeep is required
- all constructor files are needed inside the mlproject folder
- here all configuration of project is stored
- creating for loop to create files, PATH is used to convert the file location into windows operatable format
