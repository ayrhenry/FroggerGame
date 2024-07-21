import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Creating instances
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Sets player movement functions to keys
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

#Setting up game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()

    #Detect car collisions
    for car in car_manager.cars:

        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect finish line
    if player.ycor() > 260:
        player.goto_start_pos()
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()