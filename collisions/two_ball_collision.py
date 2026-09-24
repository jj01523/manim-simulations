from manim import * 
import numpy as np

class TwoBallCollision(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        #add balls
        circle_radius=0.5
        box_parameter = 6
        ball1 = Circle(radius=circle_radius, color=ORANGE, fill_opacity=1).shift(np.array([-2,0,0]))
        ball2 = Circle(radius= circle_radius, color=YELLOW, fill_opacity=1).shift(np.array([2,0,0]))
        dot = Dot(color=RED).move_to(ball2)
        threshold = Circle(radius=2*circle_radius, color=GRAY_D).move_to(ball1)
        #add box 
        box = Square(side_length=box_parameter)
        self.add(box)
        """velocities: 
        the [x,y,0] means we are moving 
        x m/s in the x direction and
        y m/s in the y direction
        """
        v1 = np.array([2,1,0])
        v2 = np.array([-1,2,0])
        
        
        time_step = 0.05 #how much simulation time passes in each iteration
        # i.e., calculating the new position every 0.05 second
        
        #how many iterations of the loop there will be. 
        #i.e., how many frames are in the animation
        # so, it will be 200 x 0.05 = 10 seconds long
        num_steps = 200
        
        self.add(ball1, ball2)
        zoomed_in = False
        for _ in range(num_steps):
            new_pos1 = ball1.get_center() + v1 * time_step
            new_pos2 = ball2.get_center() + v2 * time_step
            
            for i in range(2):
                if abs(new_pos1[i]) > (box_parameter/2) - circle_radius:
                    v1[i] *= -1
                if abs(new_pos2[i]) > (box_parameter/2) - circle_radius:
                    v2[i] *= -1
                    
            #check if the distance between their centers is 
            #less than or equal to the sum of their radii
            
            
            will_collide = np.linalg.norm(new_pos1 - new_pos2) <= (circle_radius*2)
            
            if will_collide and not zoomed_in:
                v1, v2 = v2, v1
                self.play(
                    ball1.animate.move_to(new_pos1),
                    ball2.animate.move_to(new_pos2),
                    threshold.animate.move_to(new_pos1),
                    dot.animate.move_to(new_pos2),
                    run_time=0.05
                )
                explanation = Text("Red dot has entered threshold area.").move_to(ball1).shift(DOWN)
                
                self.play(self.camera.frame.animate.scale(0.8).move_to((ball1.get_center() + ball2.get_center())/2))
                self.play(FadeIn(explanation, shift=UP))
                self.wait(2)
                self.play(AnimationGroup(
                    Restore(self.camera.frame),
                    FadeOut(explanation, shift=DOWN),run_time=2))
                zoomed_in=True
                
            elif will_collide:
                v1, v2 = v2, v1
                self.play(
                    ball1.animate.move_to(new_pos1),
                    ball2.animate.move_to(new_pos2),
                    threshold.animate.move_to(new_pos1),
                    dot.animate.move_to(new_pos2),
                    run_time=0.05
                )
            
            else:
                self.play(ball1.animate.move_to(new_pos1),
                      ball2.animate.move_to(new_pos2),
                      threshold.animate.move_to(new_pos1),
                      dot.animate.move_to(new_pos2),
                      run_time=0.05)
            
        
        