#3DGames template
#Import PyGame and Py3D
import pygame
from Py3D import *

#Import other required modules


#Runs game normally
def main():
    #Sets up the game object
    game=Game(fov=75,ticks_per_second=40,max_fps=120,use_wait=True,
                         update_callback=None,frame_callback=None,time_source=None,
                         min_brightness=10,min_colour=white, debug=False,
                          caption="Py3D Game", light_distance=3.5)

    #Create classes for Objects and Sub-Objects that extend ObjectBase and
    #SubObjectBase respectively
    class Monkey(ObjectBase):
        def update(self):
            if pygame.key.get_pressed()[K_q]:
                self.rotate_z=-4
            if pygame.key.get_pressed()[K_w]:
                self.rotate_y=4
            if pygame.key.get_pressed()[K_e]:
                self.rotate_z=4
            if pygame.key.get_pressed()[K_a]:
                self.rotate_x=4
            if pygame.key.get_pressed()[K_s]:
                self.rotate_y=-4
            if pygame.key.get_pressed()[K_d]:
                self.rotate_x=-4
            if pygame.key.get_pressed()[K_i]:
                self.y=-1
            if pygame.key.get_pressed()[K_k]:
                self.y=1
            if pygame.key.get_pressed()[K_j]:
                self.x=-1
            if pygame.key.get_pressed()[K_l]:
                self.x=1
            if pygame.key.get_pressed()[K_u]:
                self.z=-1
            if pygame.key.get_pressed()[K_m]:
                self.z=1

    #Create instances of the objects and add the models
    monkey=Monkey()
    monkey_mesh=SubObjectBase()
    monkey.add_subobject(monkey_mesh)
    monkey_mesh.add_mesh("monkey.obj")

    #Add your objects to the game
    objects={}
    objects["monkey"]=monkey
    game.objects=objects

    #Create lights(x,y,z,brightness(%),colour)
    game.add_light(x=2,y=0,z=0,brightness=100,colour=white)

    #Define what should happen each tick
    class TickHandler(object):

        #Defines what should happen before objects update
        def pre_update(self,game):
            pass

        #Defines what should happen after objects update
        def post_update(self,game):
            pass

    #Allows use of a custom GUI
    class GUI(object):

        #What should happen every update
        def update(self,game):
            pass

        #Draws the GUI
        def draw(self,game):
            pass

    #Do not change
    game.tick_handler=TickHandler()
    game.gui=GUI()

    #Start the game loop
    game.loop()

#Runs the game
main()

#Be IDLE friendly
pygame.quit()
