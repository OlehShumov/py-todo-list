# Todo List

## How it works
This project allows you to monitor the execution of your tasks, here you can create, edit and delete them, the interface also allows you to add special tags created by you to the tasks, thanks to which it will be easier to allocate execution, the interface also visually notifies about the overdue deadline


## How to install

1) Open Terminal and open folder to clone project in.

2) Clone repository into a desirable folder:

    ```
    git clone https://github.com/OlehShumov/py-todo-list.git
    ```

3) Open cloned folder in terminal

4) If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).

5) Create and activate **Virtual environment**:
   
   **Windows**
   ```
   python -m venv venv
   ```
   
   ```
   venv\Scripts\activate
   ```
   
   **MacOS**
   ```
   python3 -m venv venv
   ```
   
   ```
   source venv/bin/activate
   ```
   
6) Open cloned folder and install needed requirements using:

    ```
    pip install -r requirements.txt
    ```

7) Make migrations and migrate:

   ```
   python manage.py makemigrations
   ```
   ```
   python manage.py migrate
   ```

8) Run server:
   
   ```
   python manage.py runserver
   ```

9) Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



