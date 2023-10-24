# DOCKING SYSTEM BACKEND

this is a backend for a docking system build with simple flask server to provide information to frontend throught socket connection.

### Requeriments

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## How to run

1. Clone this repository.
2. go inside the directory.
3. run the following line.
   
```bash
  $ pip install -r requirements.txt
```

4. after that use the following line to put the system up.

```bash
  $ flask run
```

5. now you can see if the system e available putting in your browser's address bar.

```bash
  127.0.0.1:8000
```

## Personalizing some configs

you can change the number of berths available and the port that application will be available.

to do this changes you have to use the ```.flaskenv```.

### Changing the application's port

1. open the .flaskenv file in your text editor.
2. look for the line with:
   
```python
FLASK_RUN_PORT = 8000
```
3. change the value after the =
4. change it's value to desired value

**OBS:** depending from your O.S the port 8000 can be not available getting some problem to start the application, so you can change the value for another, here a brief list of suggested ports:

 * 3000
 * 3001
 * 5000
 * 8001

### Changing the quantity of berths

1. open the .flaskenv file in your text editor.
2. look for the line with:

```python
BERTHS = [1, 2, 3]
```

3. the quantity of berths is set by the quantity of elements in this list, each element of this list works like an id for the berths.
4. add more berths by adding more elements to this list with integer values.