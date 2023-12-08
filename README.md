#     Simple Todo Application









## Getting Started


1-First of all clone this repo
--
        git clone https://github.com/AyushTmg/Todo_List_Project.git

2-Setup a virtual enviroment
--
        python -m venv venv

3-Install all dependencies from the requirements.txt in a virtual enviroment
--
        pip install -r requirements.txt


4-Update the DATABASES settings in settings.py  in this case postgres is used 
--
        DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME':"database name",
                'USER': 'your_database_user',
                'PASSWORD': "database password",
                'HOST': 'localhost',
                'PORT': '5432',
        }
        }


5-Migrate the changes to your database
--
        python manage.py migrate\
        python manage.py runserver

6-Run Application
--
        python manage.py runserver


## Usage


- View Tasks: Visit the homepage to view all tasks .

![image](https://github.com/AyushTmg/Todo_List_Project/assets/119398357/477d44fc-7883-4d33-87e5-3e9280a89c0f)

- View Task Details: Click on a task to view its details.

![image](https://github.com/AyushTmg/Todo_List_Project/assets/119398357/f0f4753f-1362-43e4-ae9c-f3a42be13b14)

- Add Task: Click on "New Task" to add a new task.

![image](https://github.com/AyushTmg/Todo_List_Project/assets/119398357/8c88a440-a5ff-42cb-aa7c-3ef06b367ea5)

- Update Task: Click on "Edit" next to a task to update its details.

![image](https://github.com/AyushTmg/Todo_List_Project/assets/119398357/0ae84a88-a6f5-4065-85c6-62e5b0b31a55)

- Delete Task: Click on "Delete" next to a task to remove it.

![image](https://github.com/AyushTmg/Todo_List_Project/assets/119398357/8b6f4cd2-afba-42c9-85bb-a4a2eafefd9a)
