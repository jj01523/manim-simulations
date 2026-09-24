from manim import *

class MidpointConvergence(Scene):
    def construct(self):
        def get_midpoint(x,y):
            return (x+y)/2
        numline = NumberLine(x_range=[0,3], include_numbers=True)
        numline.scale(4)
    
        """
        for an axes, its axes.coords_to_point()
        otherwise, its numline.number_to_point()
        """
        
        pos1=0
        pos2=3
        dot1 = Dot(point = numline.number_to_point(pos1), color=YELLOW,radius=0.1)
        dot2 = Dot(point=numline.number_to_point(pos2), color=YELLOW,radius=0.1)
        self.play(Create(numline))
        self.play(AnimationGroup(GrowFromCenter(dot1),
                  GrowFromCenter(dot2)))
        for _ in range(8):
            
            dot1_stagnant = Dot(point = numline.number_to_point(pos1), color=YELLOW,radius=0.1)
            dot2_stagnant = Dot(point=numline.number_to_point(pos2), color=YELLOW,radius=0.1)
            mid_point = Dot(point=numline.number_to_point(get_midpoint(pos1,pos2)),color=GREEN)
            pos2 = get_midpoint(pos1,pos2)
            
            self.add(dot1_stagnant,dot2_stagnant)
            self.play(AnimationGroup(
            dot1.animate.move_to(mid_point),
            dot2.animate.move_to(mid_point).set_color(GREEN)
        ))
            self.play(AnimationGroup(dot2_stagnant.animate.move_to(mid_point),
                                 FadeOut(dot2), lag_ratio=0.4))
            dot1 = Dot(point = numline.number_to_point(pos1), color=YELLOW,radius=0.1)
            dot2 = Dot(point=numline.number_to_point(pos2), color=YELLOW,radius=0.1)
            self.wait(0.5)
        
        
            