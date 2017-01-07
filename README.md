# Flask Quickstart
(Python webdevelopment framework)
## Installation
### virtualenv
Use virtualenv for *development* to ensure your project does not break existing Python libraries installed.

**For Mac OS X or Linux**

`$ sudo pip install virtualenv`

**For Ubuntu/Debian (using OS package manager)**

`$ sudo apt-get install python-virtualenv`

**For Windows**

Use Python's *easy_install*. 
Check it out [here](http://flask.pocoo.org/docs/0.12/installation/#windows-easy-install).

#### Setup your project

`$ mkdir whatever`<br>
`$ cd whatever`<br>
`$ virtualenv venv`
>New python executable in venv/bin/python<br>
>Installing setuptools, pip.............done.

### Using virtualenv 

**For OS X and Linux**

`$ . venv/bin/activate`

**For Windows**

`$ venv\Scripts\activate`

Notice that the *prompt* changes to show active environment.

To go back to Python system installed:

`$ deactivate`

### Get flask into virtualenv

`$ pip install Flask`

It's not recommended but this will also work:

`$ sudo pip install Flask`




