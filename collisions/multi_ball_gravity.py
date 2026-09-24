from manim import * 
import random
import numpy as np

class MultiBallGravity(Scene):
    def construct(self):
        colors = [
            "#76be1b",
            "#ffc823",
            "#ff6616",
            "#d00727",
            "#b116ad",
            "#00a2df"
        ]
        c_radius = 0.1
        box_parameter=4
        box = Square(side_length=box_parameter)
        self.add(box)
        #create circles
        circles = VGroup()
        velocities = []
        a = np.array([0,-9.8,0])
        for i in range(10):
            circle = Circle(radius=c_radius, fill_opacity=1, color=colors[i % len(colors)]).shift(np.array([random.uniform(-1,1),random.uniform(-1,1),0]))
            circles.add(circle)
            velocities.append(np.array([0,0,0]))
            self.add(circle)
            
            
        #simulation parameters
        dt = 0.05
        run_time = 10
        frames = int(run_time/dt)
        
        def collision(i):
            for i in range(len(circles)):
                x,y,_ = circles[i].get_center()
                if (x - c_radius) <= box.get_left()[0] or (x + c_radius) >= box.get_right()[0]:
                    velocities[i][0] *= -0.8
                if (y - c_radius) <= box.get_bottom()[1] or (y + c_radius) >= box.get_top()[1]:
                    velocities[i][1] *= -0.8
                    
        def circle_update(i):  #what circle each updator belongs to
            def updator(mob, dt):
                velocities[i] = velocities[i] + a * dt
                #check for collision
                collision(i)
                new_pos = circles[i].get_center() + velocities[i] * dt
                mob.move_to(new_pos)
            return updator
        
        for i, c in enumerate(circles):
            c.add_updater(circle_update(i))
        self.wait(10)
                