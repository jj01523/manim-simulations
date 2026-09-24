from manim import * 
import random

class BubbleSortGrid(Scene):
    def construct(self):
        
        def main():
            colours = []
            
            start_x = -1.5
            start_y = 3
            sq_per_row = 5 # this is column
            sq_per_col = 7 # this is row 
            
            randomly_generate(colours, sq_per_row, sq_per_col)
            squares = generate_grid(colours, start_x, start_y, sq_per_col, sq_per_row)
            sort(colours, squares)
                        
        
        def randomly_generate(colours, sq_per_row, sq_per_col):
            for _ in range(sq_per_row * sq_per_col):
                colours.append(
                [
                    random.random(), #red
                    random.random(), #blue
                    random.random() #green
                ]
            )
        
        def sort(colours, squares):
            for i in range(len(colours)-1,0,-1): #descending order 
                for j in range(i): #after every iteration, 1 value is fixed
                    square_left = squares[j]
                    square_right = squares[j+1]
                    
                    
                    hsv_left = ManimColor.to_hsv(square_left.get_color())
                    hsv_right = ManimColor.to_hsv(square_right.get_color())
                    
                
                    if hsv_right[0] < hsv_left[0]:
                        self.play(AnimationGroup(
                        square_left.animate.move_to(square_right),
                        square_right.animate.move_to(square_left), run_time=0.2))

                        temp = squares[j]
                        squares[j] = squares[j+1]
                        squares[j+1] = temp
                    
                
        def generate_grid(colours, start_x, start_y, sq_per_col, sq_per_row):
            squares = VGroup()
            k=0
            for j in range(sq_per_col):
                for i in range(sq_per_row):
                        x_value = start_x + i
                        y_value = start_y - j  
                        square = Square(side_length=0.9, color = rgb_to_hex(colours[k]), fill_opacity = 1).move_to((x_value, y_value, 0))
                        self.add(square)
                        squares.add(square)
                        k +=1
            self.add(squares)
            return squares
            
        
            
        
        main()
        
        self.wait()
        
        
        