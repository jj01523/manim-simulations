from manim import * 

class BallOnPlatforms(Scene):
    def construct(self):
        ball_radius=0.3
        ball = Circle(color=WHITE, fill_opacity=1, radius=ball_radius).shift(UP * 3).shift(LEFT *5.3)
        floors_coords = []
        for i in range(5):
            floor = Line(start=LEFT, end=RIGHT).shift(DOWN*3).shift(LEFT * 3 *i)
            floor.shift(RIGHT * 5.5)
            floors_coords.append((floor.get_left(), floor.get_right()))
            self.add(floor)
        self.add(ball)
        print(floors_coords) 
        # printed value: 
        # [(array([ 2., -3.,  0.]), array([ 4., -3.,  0.])), (array([-1., -3.,  0.]), array([ 1., -3.,  0.])), (array([-4., -3.,  0.]), array([-2., -3.,  0.]))
        
        
        velocity = np.array([2,0,0])
        a = np.array([0,-9.8,0])
        time_step = 0.05
        run_time = 7
        num_steps = int(run_time/time_step)
        
        #recalculating velocity at every frame
        for _ in range(num_steps):
            velocity = velocity + a * time_step
            new_pos = ball.get_center() + velocity * time_step
            
            #if ball is on y value, check if its on x value
                #checking for x value
            x = new_pos[0]
            for start, end in floors_coords:
                if start[0] < x < end[0] and -4 < new_pos[1] < floor.get_center()[1] + ball_radius:
                    velocity[1] *= -0.8
                    new_pos[1] = floor.get_center()[1] + ball_radius
                
            
            
            
            #if floors_coords[0][0]<x<
            self.play(ball.animate.move_to(new_pos), run_time=0.05)
        