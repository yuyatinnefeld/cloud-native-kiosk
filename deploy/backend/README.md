# Backend Service

## Setup Mkdocs Environment
```bash
# install mkdocs and project relevant python packages
pip install -r requirements_dev.txt

# create mkdocs files
mkdocs new .

# edit mkdocs file
vi ./mkdocs.yml

# edit docs/index.md
vi docs/index.md

# create a python script which generates the markdown files and nav automatically
# source: https://github.com/oprypin/mkdocs-gen-files
touch docs/gen_mkdocs_pages.py
```
