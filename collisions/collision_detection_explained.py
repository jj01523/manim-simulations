from manim import * 


class CollisionDetectionExplained(MovingCameraScene):
    def construct(self):
        text_intro = Text("How do you know when\n"
    "two balls collide in a simulator?")
        self.play(Write(text_intro))
        self.wait(2)
        self.play(FadeOut(text_intro))
        
        self.camera.frame.save_state()
        grid = NumberPlane(background_line_style={"stroke_opacity": 0.3}).add_coordinates()
        #self.add(grid)
        tracker = ValueTracker()
        scale_tracker = ValueTracker(1)
        
        radius = 2
        radius2 = -(radius)
        threshold_rad = (radius * 2)
        origin_circ = Circle(color = ORANGE, radius=radius)
        circle2 = Circle(color= YELLOW, radius=radius)
        radius1 = DashedLine(start = np.array([0,0,0]), end=np.array([radius,0,0]), color=RED)
        radius2 = DashedLine(start = np.array([0,0,0]), end=np.array([radius2,0,0]), color=RED)
        dot_origin = Dot(color=ORANGE)
        dot2 = always_redraw(lambda: Dot(point=circle2.get_center(), color=YELLOW).scale(scale_tracker.get_value()))
        threshold = Circle(color=GRAY_D, radius = threshold_rad)
        
        
        label = Text("radius").move_to(radius1, UP).scale(0.5)
        diameter_label = Text("diameter").move_to(np.array([0,-0.3,0])).scale(0.5)
       
        def update_circle2(mob):
            mob.move_to(RIGHT*tracker.get_value())
        
        
        self.play(AnimationGroup(
            GrowFromCenter(dot_origin),
            Create(origin_circ), lag_ratio=1))
        self.play(AnimationGroup(Create(radius1),
                                 Write(label), lag_ratio=0.5))
        self.play(AnimationGroup(Create(radius2),
                                 Transform(label,diameter_label)))
        self.wait()
        
        d_line = VGroup(radius1, radius2, label)
        self.play(AnimationGroup(d_line.animate.shift(RIGHT*2), Create(threshold),
                                 lag_ratio=1))
        self.play(FadeOut(d_line))
        self.play(FadeIn(circle2,dot2))
        circle2.add_updater(update_circle2)
        
        main_line = always_redraw(lambda: DashedLine(start=origin_circ.get_center(), end=circle2.get_center(), color=RED))
        main_label = always_redraw(lambda: Tex(f"{tracker.get_value():.2f}", color=RED).move_to(main_line).shift(DOWN))
        self.play(Create(main_line))
        self.play(Write(main_label))
        self.play(AnimationGroup(tracker.animate.set_value(6.5),
                                 self.camera.frame.animate.scale(1.3)))
        self.wait()
        
        intersection_dot = Dot(point=np.array([radius, 0, 0]), color=GREEN)
        
        self.play(GrowFromCenter(intersection_dot))
        self.play(Restore(self.camera.frame), run_time=2)
        self.play(AnimationGroup(tracker.animate.set_value(4),
                            Flash(intersection_dot), run_time=3, lag_ratio=1))
        
        
        self.play(scale_tracker.animate.set_value(2))
        text_final = Text("When the yellow dot enters the threshold area,\n"
                          "the two balls collide.").shift(DOWN * 3)
        self.play(AnimationGroup(Write(text_final),
                                 scale_tracker.animate.set_value(1)))
        self.wait(3)
    #run_time=2)
        
        