import time
from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
game_is_on=True
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager=Car_Manager()
scoreboard=Scoreboard()
while game_is_on:
    time.sleep(.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
#dectetction colison with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
#succesful completetion
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()