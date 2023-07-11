# tux.tools website
TO-DO: Merge modules into this repo as blueprint submodules
# tux.tools


Folder structure should follow this rules:
```
app
    |--- templates
            |--- static_template.html
    |--- static
            |--- static_sample.css
    |--- bin
            |--- __init__.py
            |--- bin.py
            |--- templates
                |--- bin
                      |--- template_sample.html
            |--- static
                |--- bin
                      |--- static_sample.css
    |--- geo
            |--- __init__.py
            |--- geo.py
            |--- templates
                |--- geo
                      |--- template_sample.html
            |--- static
                |--- geo
                      |--- static_sample.css
    |--- tools
            |--- __init__.py
            |--- tools.py
            |--- templates
                |--- tools
                      |--- template_sample.html
            |--- static
                |--- tools
                      |--- static_sample.css
    |--- main.py
    |--- models.py
    |--- config.py
    |--- wsgi.py
```
