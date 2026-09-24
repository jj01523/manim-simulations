from manim import *
import numpy as np

class OrbitCameraFollow(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state() #save the original state of camera
        tracker = ValueTracker(1)
        sun = Circle(radius=0.3, color=YELLOW_D, fill_opacity=1)
        
        orbit_radius = 2.5
        orbit2_radius_x = 3
        #because we use tracker.get_value() that will always be changing, we need 
        #to use always_redraw(lambda:)
        planet = always_redraw(lambda: Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to([
            orbit_radius * np.cos(PI/2 * tracker.get_value()),
             orbit_radius * np.sin(PI/2 * tracker.get_value()), 0
        ]))
        planet2 = always_redraw(lambda: Circle(radius=0.125, color=BLUE, fill_opacity=1).move_to([
            orbit2_radius_x * np.cos(PI/2 * tracker.get_value()),
             orbit_radius * np.sin(PI/2 * tracker.get_value()), 0
        ]))
        trace = TracedPath(planet.get_center, stroke_color=GREEN_E)
        trace2 = TracedPath(planet2.get_center, stroke_color=DARK_BLUE)
    
        self.add(planet, trace, planet2, trace2)
        self.add(sun)
        
        def update_camera(mob):
            t= tracker.get_value()
            if 0 <= t < 4:
                pass
            elif 4 <= t <= 8:
                mob.scale_to_fit_width(max(14.2222 + (t-4) * (3 - 14.2222),3))
                mob.move_to(planet.get_center())
            elif 8 < t <= 12:
                mob.scale_to_fit_width(min(3 + (t-8) * (14.2222 - 3),14.2222))
                mob.move_to(planet.get_center())
                
                
        self.camera.frame.add_updater(update_camera)
        self.add(self.camera.frame)
        self.play(
            tracker.animate.set_value(12),
             rate_func=linear,run_time=10)
        #self.play(self.camera.frame.animate.set(width=planet.width * 8).move_to(planet))
                
        self.wait()
        
        