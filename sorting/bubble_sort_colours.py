from manim import * 
import random
import colorsys

class BubbleSortColours(Scene):
    def construct(self):
        colours_length = 10
        colours = []
        
        def sort(colours):
            for i in range(len(colours)-1,0,-1): #descending order 
                for j in range(i): #after every iteration, 1 value is fixed
                    square_left = squares[j]
                    square_right = squares[j+1]
                    
                    
                    hsv_left = ManimColor.to_hsv(square_left.get_color())
                    hsv_right = ManimColor.to_hsv(square_right.get_color())
                    
                
                    if hsv_right[0] < hsv_left[0]:
                        self.play(AnimationGroup(
                        square_left.animate.move_to(square_right),
                        square_right.animate.move_to(square_left)))

                        temp = squares[j]
                        squares[j] = squares[j+1]
                        squares[j+1] = temp
                
        
        for i in range(colours_length):
            colours.append(
                [
                    random.random(),
                    random.random(),
                    random.random()
                ]
            )
            
        squares = VGroup()
        for i, colour in enumerate(colours):
            square = Square(side_length=0.5, fill_opacity=1, color=rgb_to_hex(colour)).shift(LEFT * 4.5)
            square.shift(RIGHT * (i))
            self.play(Create(square),run_time=0.2)
            squares.add(square) 
            
        sort(colours)
        
       
        
        #colours.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
        self.wait()
        
        
        