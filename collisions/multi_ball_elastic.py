from manim import * 
import random
import numpy as np
class MultiBallElastic(Scene):
    def construct(self):
        #add balls
        circle_radius = 0.1
        box_parameter = 4
        num_balls = 20
        
        colors = [
            "#76be1b",
            "#ffc823",
            "#ff6616",
            "#d00727",
            "#b116ad",
            "#00a2df"
        ]
        
        #create balls
        balls = VGroup()
        for i in range(num_balls):
            ball = Circle(radius=circle_radius, fill_opacity=1, color=colors[i%len(colors)])
            ball.shift(np.array([random.uniform(-1,1), random.uniform(-1,1), 0]))
            
            ball.velocity = np.array([random.uniform(-1,1), random.uniform(-1,1), 0])
            balls.add(ball)
        
        box = Square(side_length=box_parameter)
        self.add(box, balls)
        
        #def updator function
        def update_balls(balls_group, dt):
            #move each ball by its velocity
            for ball in balls_group:
                new_pos = ball.velocity * dt
                ball.shift(new_pos)
                
                #check for collision
                position = ball.get_center()
                #collision with left & right walls
                if abs(position[0]) > (box_parameter/2) - circle_radius:
                    ball.velocity[0] *= -1
                #collision with top & bottom walls
                if abs(position[1]) > (box_parameter/2) - circle_radius:
                    ball.velocity[1] *= -1
            
            #check for ball collision
            for i in range(len(balls)): #goes through each ball starting at ball 0
                for j in range(i+1, len(balls)):  #goes through each ball starting at ball 1
                    ball1 = balls[i] #0,1,2
                    ball2 = balls[j] #1,2,3
        
                    dist = np.linalg.norm(ball1.get_center() - ball2.get_center())
                    #if the distance is less than double the circle radius, they've collided
                    if dist <= (circle_radius*2):
                        ball1.velocity, ball2.velocity = ball2.velocity, ball1.velocity
        
        balls.add_updater(update_balls)
        
        #running animation... no need for _ in fps.
        self.wait(10)
        
        balls.clear_updaters()