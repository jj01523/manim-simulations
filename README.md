# Manim Simulations

Animations I built while teaching myself [Manim](https://www.manim.community/). Mostly physics simulations, sorting algorithms and geometry.


Made with Manim Community v0.19.1.

## Previews

**Bubble sort by colour**: 10 random colours generated which get sorted by hue.

![Bubble sort sorting random colours into a spectrum](assets/bubble_sort_colours.gif)

**Collision detection** - two balls in a box. The grey circle is the threshold for working out when they touch, and the red dot tracks the other ball.

![Two balls colliding in a box with the detection threshold drawn on](assets/two_ball_collision.gif)

**Binary stars** - two stars orbiting each other under their own gravity. The force between them is worked out again every frame from how far apart they are.

![Two stars orbiting each other, one blue and one gold](assets/two_body_gravity.gif)

**Triangle area** - the area is recalculated with Heron's formula as the triangle changes shape.

![A triangle deforming with its area recalculated live](assets/triangle_area_heron.gif)

## Files

**collisions/**
- `collision_detection_explained.py` - how you actually detect a collision, building up from the radius to a threshold circle
- `two_ball_collision.py` - two balls in a box, zooming in on the first collision
- `multi_ball_elastic.py` - 20 balls, wall bounces and ball to ball collisions
- `multi_ball_gravity.py` - 10 balls falling, losing speed on each wall bounce

**physics/**
- `two_body_gravity.py` - two bodies pulling on each other
- `orbit_camera_follow.py` - orbits with traced paths and a camera that follows a planet
- `bouncing_ball.py` - a ball dropping and losing 20% of its speed each bounce
- `ball_on_platforms.py` - a ball bouncing across separate platforms

**sorting/**
- `bubble_sort_colours.py` - bubble sort on random colours, compared by hue
- `bubble_sort_grid.py` - the same sort on a grid

**geometry/**
- `triangle_area_heron.py` - live area using Heron's formula
- `midpoint_convergence.py` - repeatedly taking midpoints on a number line

**combinatorics/**
- `table_permutations.py` - seating arrangements around a round table, showing why there are (n-1)! of them

## Running it

```bash
pip install -r requirements.txt
```

You also need FFmpeg installed, plus LaTeX for the scenes with equations in them.

To render a scene, give Manim the file and the class name:

```bash
manim -ql collisions/multi_ball_elastic.py MultiBallElastic
```

`-ql` is a quick low quality preview, `-qh` renders it at 1080p.
