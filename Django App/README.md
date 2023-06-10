## <b> Runnning the Django App</b>
<br>
- Navigate into the django app directory by running:

```bash
  cd ".\Django app"
```

- The **requirements.txt** file contains all the dependencies needed to run the project successfully. You can install these by running:
```bash
  pip install -r requirements.txt
```

- Navigate into the project directory by running 
```bash
  cd deployment
```
- If you check all the files in this directory you can find the **manage.py** file  whihc is needed to run the app (mlApp). Now run:

```bash
  python manage.py runserver
```

- If you have a preferred address where you wish to run the server, you can do that by adding the address after "runserver". Example:<br>
```bash
  python manage.py runserver 127.0.0.1:8080
```
This means the server will run on "127.0.0.1:8080"

Now you can copy the url where the serve is running and paste it in your browser, where you can interact with the web app.  






