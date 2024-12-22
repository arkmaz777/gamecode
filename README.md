# Creating a Superuser

To create a superuser in your Django application, follow these steps:

1. Open a terminal and execute the following command to access the `web` service container:

   ```bash
   docker-compose exec web /bin/bash

2. Run commands described below and execute suggested commands
  ```bash
  python manage.py createsuperuser


# Testing the logic of winning alghoritm

   In order to run test you have to go to the web container and run testing command as below:
   ```
   docker-compose exec web /bin/bash
   python manage.py test slot

