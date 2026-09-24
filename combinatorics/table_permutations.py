from manim import *
import itertools

class TablePermutations(Scene):
    def construct(self):
        c_radius = 0.3
        table = Circle(color=WHITE)
        
        colours = [RED, YELLOW, GREEN, BLUE]
        positions = [
            np.array([0, 2, 0]),  
            np.array([2, 0, 0]),  
            np.array([0, -2, 0]), 
            np.array([-2, 0, 0])  
        ]
        self.add(table)
        
        shifts = [UP, RIGHT,DOWN,LEFT]
        circles = VGroup()
        for i, color in enumerate(colours):
            circle = Circle(
                radius=c_radius, 
                fill_color=color,
                fill_opacity=1,
                color=color
            ).move_to(positions[i])
            circles.add(circle)
            self.play(FadeIn(circle, shift=shifts[i]), run_time=0.5)
        self.wait()
        
        count = 1
        text = always_redraw(lambda: Text(f"Number of Arrangements: {count}").shift(DOWN * 3))
        self.play(Write(text))
        
        fixed_color = 0  # Fix RED at position 0 (top)
        moving_color = [1, 2, 3]
        perms = list(itertools.permutations(moving_color))
        for perm in perms:
            full_perm = [fixed_color] + list(perm)
            print(full_perm)
            # Create animations to move circles to new positions
            animations = []
            
            for i in range(len(colours)):
                target_pos = positions[full_perm[i]]
                animations.append(circles[i].animate.move_to(target_pos))
            
            self.play(AnimationGroup(*animations), run_time=1)
            count += 1
            self.wait(0.5)
        #self.play(AnimationGroup(circles[0].animate.move_to(circles[1]), circles[1].animate.move_to(circles[0])))
        #count+=1  
            
        
        #self.play(Rotate(circles, angle=1/4 * TAU, about_point=ORIGIN), run_time=2)
        #self.play(Rotate(circles, angle=1/4 * TAU, about_point=ORIGIN), run_time=2)
        self.wait()
        
        