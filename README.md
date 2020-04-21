Noclist assignment submission

## Set up 
Install Python3.7.7 using homebrew and pyenv to manage multiple versions of python
    
    brew install pyenv
    pyenv install 3.7.7

Activate the Python 3.7.7 environment from the project home directory
    
    source env/bin/activate

Install packages and required dependencies
    
    pip install -r requirements.txt

## Running 
To run get users from project home dir
    
    cd noclist
    python main.py

## Testing
4 tests are included and are divided up into two files
    
    cd tests
    python -m  unittest users_test.py
    python -m  unittest request_wrapper_test.py

## Off boarding
Deactivate the python env when you would like to switch back to your native Python env
    
    deactivate

## Assumptions
I assume that all connection issues or error codes thrown by the flaky server will either be in requests.exceptions.RequestException or a ConnectionResetError 

