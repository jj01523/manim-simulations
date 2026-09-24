from manim import * 

class BouncingBall(Scene):
    def construct(self):
        ball_radius=0.3
        ball = Circle(color=WHITE, fill_opacity=1, radius=ball_radius).shift(UP * 3)
        floor = Line().shift(DOWN*3)
        self.add(floor,ball)
        
        velocity = np.array([0,0,0])
        a = np.array([0,-9.8,0])
        time_step = 0.05
        run_time = 7
        num_steps = int(run_time/time_step)
        
        for _ in range(num_steps):
            velocity = velocity + a * time_step
            new_pos = ball.get_center() + velocity * time_step
            if new_pos[1] < floor.get_center()[1] + ball_radius:
                velocity[1] *= -0.8
                new_pos[1] = floor.get_center()[1] + ball_radius
                
            self.play(ball.animate.move_to(new_pos), run_time=0.05)
        