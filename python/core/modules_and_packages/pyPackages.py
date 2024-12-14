"""
create virtual env
>>> python -m venv [your-env-name]

check installed modules and packages with version
>>> pip freeze/pip list

activate and deactivate your virtual env
>>> [your-env-name]\Scripts\activate
([your-env-name])>>> [your-env-name]\Scripts\deactivate

Install and uninstall modules and packages
>>> pip install [module-or-package-name]==x.y.z
>>> pip uninstall [module-or-package-name]==x.y.z

add moduels and packages in requirements.txt file
>>> pip freeze > requirements.txt

install all modules and packages from requirements.txt file
>>> pip install -r requirements.txt

https://pypi.org/
"""