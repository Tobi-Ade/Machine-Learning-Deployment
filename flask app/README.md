## <b> Runnning the Flask App</b>
<br>
- Navigate into the flask app directory by running:

```bash
  cd ".\flask app"
```

- The **requirements.txt** file contains all the dependencies needed to run the project successfully. You can install these by running:
```bash
  pip install -r requirements.txt
```

- Now that all the dependencies are installed, you can simply start the api by running:
```bash
  python app.py
```
The flask api should start running at this stage. You can send a request and get instant results, or copy the url where the api is running and paste it in your browser, where you can interact with the api.  
<br>

- The **request.py** file contains a sample request. To use this, keep the api running and open an new terminal window, navigate to the current directory, then run:
 ```bash
  python request.py
```
The request.py file can also be modified to see how the result changes. You can also create a custom request using the same format in the request.py.