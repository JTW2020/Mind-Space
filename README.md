# Mind-Space
Modern Software Development Project for team Mind Space

# Setting up the Server folder
To set up the server, you have to go to the server folder from the terminal and 
then use the following commands:

**Before using any of these commands to work on the server, make sure your current directory is Mind-Space/server**

**These commands should be run in sequence during the first time you load the project.**
```
python3 -m venv venv                        # This line creates the virtual environment
. venv/bin/activate                         # This will activate virtual environment
python3 -m pip install -r requirements.txt  # This will install all the modules
```

Every time you run the program make sure you are using the virtual environment and
that the modules are up to date by just using the following commands:

**Windows Terminal**
```
venv\Scripts\activate                       # This will activate virtual environment
python3 -m pip install -r requirements.txt  # This will install all the modules
```

**Bash**
```
. venv/bin/activate                         # This will activate virtual environment
python3 -m pip install -r requirements.txt  # This will install all the modules
```

# Starting the Server

**Windows Terminal**
```
set FLASK_APP=app
flask run
* Running on http://127.0.0.1:5000
```

**Bash**
```
export FLASK_APP=app
flask run
* Running on http://127.0.0.1:5000
```

# Potential Future use of Docker
With Docker, we can automate the setup of the environment for the application which
will enable us to spend more time programming and less time setting up.
