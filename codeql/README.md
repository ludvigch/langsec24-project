# CodeQL queries to look for prototype pollution patterns
**Prerequisites:** Visual Studio Code(VSCode)

## Setup CodeQL in VSCode
    1. Install the CodeQL extension

## Run queries on a target project
    1. Open VSCode in this directory of the repository
    2. Switch to the CodeQL tab
    3. In the Databases section, select the Github icon "Download Database from GitHub" and enter the target project url
       for example: https://github.com/dgilland/pydash
    4. In the Queries section, select recursive.ql or setattr.ql and click the "Run local query" button

## Packages analysed in the project
| Package | URL |
| ------- | --- |
| Eve | https://github.com/pyeve/eve |
| Flask | https://github.com/pallets/flask |
| FlaskBB | https://github.com/flaskbb/flaskbb |
| Jinja | https://github.com/pallets/jinja |
| Marshmallow | https://github.com/marshmallow-code/marshmallow |
| Pydash | https://github.com/dgilland/pydash |
| Pyjwt | https://github.com/jpadilla/pyjwt |
| Pyquery | https://github.com/gawel/pyquery |
| Pyramid | https://github.com/Pylons/pyramid |
| Toolz | https://github.com/pytoolz/toolz |

**Accessed 27/5-2024**
