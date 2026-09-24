from manim import * 
import math

class TriangleAreaHeron(Scene):
    def construct(self):
        
        trackers = [
            (ValueTracker(-1.5), ValueTracker(1)),
            (ValueTracker(2), ValueTracker(2)),
            (ValueTracker(-0.5), ValueTracker(-2))
        ]
        
            
            
        """
        points = [
            np.array([-1,1,0]),
            np.array([2,1.5,0]),
            np.array([-0.5,-2,0])
        ]
        """
        
        #add the dots to the scene
        dots = VGroup()
        for i in range(len(trackers)):
            x_tracker, y_tracker = trackers[i]
            dot = always_redraw(lambda x=x_tracker, y=y_tracker: 
                Dot(point=[x.get_value(), y.get_value(), 0]))
            dots.add(dot)
            self.add(dot)
        
        #connect the dots 
        lines = VGroup()
        for i in range(len(dots)):
            line = always_redraw(lambda i=i:
                Line(start=dots[i], end=(dots[(i+1) % len(dots)])))
            lines.add(line)
            self.add(line)
            
        def find_distance(p,q):
            return math.dist(p,q)
            
        #finding the area
        def text_updator():
            coords = []
            for tracker in trackers:
                coords.append((tracker[0].get_value(), tracker[1].get_value()))
            
            a = find_distance(coords[0], coords[1])
            b = find_distance(coords[1], coords[2])
            c = find_distance(coords[2], coords[0])
            s = (a + b + c) / 2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            return area 
            
        text = always_redraw(lambda: Text(f"Area: {text_updator():.2f}").to_edge(DOWN))
        self.add(text)
        
        self.play(AnimationGroup(trackers[0][0].animate.set_value(-3),
                                 trackers[0][1].animate.set_value(3.4),
                                 trackers[1][0].animate.set_value(4),
                                 lag_ratio=0.5))
        self.wait()
        self.play(AnimationGroup(trackers[1][1].animate.set_value(0),
                                 trackers[2][0].animate.set_value(-6),
                                 trackers[2][1].animate.set_value(-3),
                                 lag_ratio=0.5))
        self.wait()
        
        
        
        