# Storefront-Django
E-commerce App - Django

--- Using Demo SMTP server ---
To setup smtp4dev run this in terminal:
docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev


--- Using Redis for Message Broker + Cache ---
To setup Redis run this in terminal:
docker run -d -p 6379:6379 redis

--- IMPORTANT ----
I am using a WSL(Windows Subsystem for Linux) for running this django project.

1. Install Ubuntu

    wsl --install
    wsl --install -d ubuntu

2. Install Extension in VSCode for Remote Connection

   - Extension Name: Remote - WSL
   - Open Command Palette and type: Remote-WSL:Reopen Folder in WSL
   This will re-open the project folder.
   Open a terminal window on VSCode. You'll see the command prompt changed to Linux.

3. Update the Package List

    sudo apt update && sudo apt upgrade

4. Upgrade Python to latest version

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo install python 3.9
    sudo rm /usr/bin/python3 -- if any problems occur.
    sudo ln -s python3.9 /usr/bin/python3
    python3 --version

5. Install pip and pipenv

    sudo apt install python3-pip pipenv
    pip --version
    pipenv -- version

6. Install MySQL

    sudo apt install python3.9-dev
    sudo apt install libmysqlclient-dev

    pip install mysqlclient

    sudo install mysql-server
    mysql --version
    sudo service mysql start

7. Configure MySQL

    sudo mysql -u root -p

        CREATE DATABASE storefront;
        ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
        type quit to exit

    In settings.py set everything

8. Start the Project

    pipenv install
    pipenv shell 
    python manage.py migrate
    --Optionally seed the database
        python manage.py seed_db    
    python manage.py runserver

Next time onwards remember to run pipenv shell every time open a new terminal

