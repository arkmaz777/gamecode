# Project description:
The project is a simple slot game with three reels. With each spin, random symbols are drawn on 
the three reels. Each reel contains elements similar to a deck of cards. 
The project should allow for the launch of a simple website where users can enter their 
nickname and have the ability to spin/play by clicking a button. The result will be displayed 
to the player as a win, along with the state of the reels they spun. 
All games should be saved and displayed on the same page as "recent results". 
The last 10 results of all players should be shown.

Wins: A player wins only if the same symbols appear in a specific position on the reels. 
For example, [K, K, K] wins. Only one line is considered. The prize amount is determined 
by the position of the figure in the deck. J=1, Q=2, K=3, A=4 
The results do not need to be summed. Only the most recent result is displayed, along with the 
win (if any) and the reel states.

# Start the containers

   ```bash
   docker-compose up --build
   ```

And you should see the app at the adress:
http://localhost:8002/


# Creating a Superuser (which has acces to admin panel)

To create a superuser in your Django application, follow these steps:

1. Open a terminal and execute the following command to access the `web` service container:

   ```bash
   docker-compose exec web /bin/bash
   ```

2. Run commands described below and execute suggested commands
  ```bash
  python manage.py createsuperuser
  ```

Since now you have access to admin panel:
http://localhost:8002/admin


# Testing the logic of winning alghoritm

   In order to run test you have to go to the web container and run testing command as below:
   ```bash
   docker-compose exec web /bin/bash
   python manage.py test slot
   ```


# Changing styles

   When you are not able to see spcial css styles, please run the command:
   ```bash
   python manage.py collectstatic
   ```