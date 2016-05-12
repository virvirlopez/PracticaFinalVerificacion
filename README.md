# Config

Create a new environment to run the tests:
```
pip install virtualenv
rm -rf venv/
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Run the tests
Unit Tests
```
venv/bin/pytest tests 
```
or
```
venv/bin/nosetests 
```

BDD Tests
```
lettuce
```

# Pylint
```
venv/bin/pylint casino
```

# Coverage
```
env/bin/nosetests --with-coverage
```
