from manimlib.imports import *
import math

class Polygon_and_circle(Scene):
    def construct(self):
        r = 3
        circle  = Circle(radius = r, color = YELLOW)
        self.play(ShowCreation(circle))

        theta = [math.pi / 12, 2 * math.pi / 3, 4 * math.pi / 3, - math.pi / 12, math.pi / 2 - math.pi / 15,
        math.pi + math.pi / 12, -math.pi / 3, math.pi / 3, math.pi - math.pi / 12, math.pi * 3 / 2 - math.pi / 15]
        current_x = []
        current_y = []


        def add_point(x):
            point = Circle(radius = 0.05, color = "#00ccff", fill_opacity = 1)
            point.move_to(np.array([r * math.cos(x), r *  math.sin(x), 0]))
            self.play(FadeIn(point))
            for i in range(len(current_x)):
                line = Line(np.array([r * math.cos(x), r * math.sin(x), 0]), np.array([current_x[i], current_y[i], 0]), color = "#33ff66")
                self.play(FadeIn(line))
            current_x.append(r * math.cos(x))
            current_y.append(r * math.sin(x))


        for angle in theta:
            add_point(angle)
