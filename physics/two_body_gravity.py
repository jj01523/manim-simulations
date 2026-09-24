from manim import *
import math

class TwoBodyGravity(Scene):
    def construct(self):

        def create_glow(obj, rad=1, col=BLUE_B):
            glow_group = VGroup()
            for i in range(60):
                new_circle = Circle(
                    radius=rad * (1.002 ** (i ** 2)) / 200,
                    stroke_opacity=0,
                    fill_color=col,
                    fill_opacity=0.2 - i / 300
                ).move_to(obj)
                glow_group.add(new_circle)
            return glow_group

        c_radius = 4
        mass = 5

        circle1 = Circle(
            color=WHITE,
            fill_opacity=1,
            radius=c_radius
        ).to_edge(LEFT).set_color(BLUE_B)

        c1 = create_glow(circle1)

        circle2 = Circle(
            color=WHITE,
            fill_opacity=1,
            radius=c_radius
        ).to_edge(RIGHT).set_color(BLUE_B)

        c2 = create_glow(circle2)

        self.add(c1, c2)

        time_step = 0.02
        run_time = 10
        num_steps = int(run_time / time_step)

        def attract(c1, c2, mass):
            center1 = c1.get_center()
            center2 = c2.get_center()
            delta = center2 - center1
            center_distance = math.dist(center1, center2)
            direction = delta / center_distance
            G = 30
            magnitude = G * ((mass * 2) / center_distance)
            return magnitude * direction

        velocity1 = np.array([0, -1, 0])
        velocity2 = np.array([0, 1, 0])

        for _ in range(num_steps):
            force = attract(c1, c2, mass)
            a = force / mass
            velocity1 = velocity1 + a * time_step
            velocity2 = velocity2 - a * time_step
            new_pos1 = c1.get_center() + velocity1 * time_step
            new_pos2 = c2.get_center() + velocity2 * time_step

            self.play(c1.animate.move_to(new_pos1), run_time=0.01)
            self.play(c2.animate.move_to(new_pos2), run_time=0.01)
            
