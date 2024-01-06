# REQUEST and HTTPX LIBRARIES

> It is recommended to use a virtual environment.

Install the dependencies by running the following command:

```pip install -r requirements.txt```

Start the **Uvicorn** server using the server's CLI tool:

```uvicorn webserver.main:app --reload```

or through Python by running:

```python webserver/main.py```

_Notice, however, that the second option won't restart the application when changes to the project are saved_

You can now run the Python scripts independently with the server _running_. 
 