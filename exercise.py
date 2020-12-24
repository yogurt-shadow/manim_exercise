from manimlib.imports import *
import os
import pyclbr
import math

class Hello_world(Scene):
    def construct(self):
        helloworld = TextMobject("Hello World!", color=RED)
        self.play(Write(helloworld))
        self.wait(1)

class Hello_Manim(Scene):
	def construct(self):
		helloworld = TextMobject("Hello World!", color=RED)
		rectangle=Rectangle(color=BLUE)
		rectangle.surround(helloworld)

		group1 = VGroup(helloworld, rectangle)
		hellomanim = TextMobject("Hello Manim", color=BLUE)
		hellomanim.scale(2.5)

		self.play(Write(helloworld))
		self.wait(1)
		self.play(FadeIn(rectangle))

		self.wait(1)
		self.play(ApplyMethod(group1.scale, 2.5)) # zoom x2.5
		self.wait(1)
		self.play(Transform(helloworld, hellomanim))
		self.wait()

'''
shapes below

Circle圆
Annulus圆环
Ellipse椭圆
Square方形
Rectangle矩形
Triangle三角形
Polygon多边形
'''
class Basic_Shapes(Scene):
	def construct(self):

		ring = Annulus(inner_radius = 0.4, outer_radius = 1, color = BLUE)
		square=Square(color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
		rect = Rectangle(height=3.2, width=1.2, color=PINK, fill_color=PINK, fill_opacity=0.5)

		line01 = Line(np.array([0, 3.6, 0]), np.array([0, 2, 0]), color=BLUE)
		line02 = Line(np.array([-1, 2, 0]), np.array([-1, -1, 0]), color=BLUE)
		line03 = Line(np.array([1, 2, 0]), np.array([1, 0.5, 0]), color=BLUE)

		ring.shift(UP * 2)
		square.shift(LEFT + DOWN * 2)
		rect.shift(RIGHT + DOWN * (3.2 / 2 - 0.5))


		self.add(line01)
		self.play(GrowFromCenter(ring))
		self.wait(0.5)
		self.play(FadeIn(line02), FadeIn(line03))
		self.wait(0.5)
		self.play(FadeInFromDown(square))
		self.play(FadeInFromDown(rect))
		self.wait()

class Shoot(Scene):
	def construct(self):
		circle01 = Circle(color=BLUE)
		circle02 = Circle(color=RED, fill_color=RED, fill_opacity = 1)
		circle02.scale(0.1)
		line01 = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), color=RED)
		line02 = Line(np.array([0, 1, 0]), np.array([0, -1, 0]), color = RED)
		aim_scope = VGroup(circle01, circle02, line01, line02)
		acquire = TextMobject("Target Acquired!", color = GREEN)
		shoot = TextMobject("Shoot Now!", color = RED)

		target_list = []
		for i in range(3):
			for j in range(5):
				target_ij = Circle(color = YELLOW, fill_color = YELLOW, fill_opacity = 0.4)
				target_ij.scale(0.4)
				target_ij.shift(np.array([-4 + j * 2, -2 + i * 2, 0]))
				self.play(FadeIn(target_ij))
				target_list.append(target_ij)

		self.wait(1)

		def shoot_ij(i, j):
			target_ij = target_list[i * 5 + j]
			circle_current = Circle(color = BLUE)
			circle_current2 = Circle(color = RED, fill_color = RED, fill_opacity = 1)
			circle_current2.scale(0.1)
			circle_current.next_to(target_ij, 0)
			circle_current2.next_to(target_ij, 0)


			self.play(ApplyMethod(aim_scope.next_to, target_ij, 0))

			acquire.next_to(target_ij, UP)
			self.play(FadeIn(acquire))
			self.wait(0.5)
			self.play(FadeOut(acquire))

			self.play(
			Transform(circle_current, target_ij),
			Transform(circle_current2, target_ij))

			shoot.next_to(target_ij, UP)
			self.play(FadeIn(shoot))
			self.wait(0.5)
			self.play(FadeOut(shoot))

			target_ij.set_color(PINK)
			target_ij.set_fill(PINK)

			self.play(
			ApplyMethod(target_ij.set_fill, PINK),
			ApplyMethod(target_ij.set_color, PINK))

			self.wait(0.5)

			ij = TextMobject("(%d, %d)" % (i, j), color = GREY)
			ij.next_to(target_ij, DOWN)
			self.play(Write(ij))
			self.wait(1)
			return 0

		self.add(aim_scope)
		self.play(aim_scope.shift, DOWN * 3 + LEFT * 6.1)
		shoot_ij(0, 1)
		shoot_ij(2, 0)
		shoot_ij(1, 3)
		shoot_ij(0, 0)
		shoot_ij(2, 4)

class Circles(Scene):
    def construct(self):
        i = 0.1
        while i < 3:
            circle01 = Circle(color = GREEN)
            circle01.scale(i)
            circle02 = Circle(radius = i + 0.2, color=GREEN)
            self.play(ShowCreation(circle01))
            self.add(circle01)
            self.play(Transform(circle01, circle02))
            i = i + 0.2

class LDR(Scene):
    def construct(self):
        circle01 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        circle02 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        square01 = Square(color=RED, fill_color=RED, fill_opacity=0.5)
        love = VGroup(circle01, circle02, square01)

        rect01 = Rectangle(height = 0.8, width = 4, fill_color=YELLOW, color=YELLOW, fill_opacity=0.5)
        rect02 = Rectangle(height = 0.8, width = 4, fill_color=YELLOW, color=YELLOW, fill_opacity=0.5)
        death = VGroup(rect01, rect02)

        square02 = Square(color=BLUE, fill_color = BLUE, fill_opacity = 0.5)
        square02.scale(1.6)
        c01=Circle(color=BLACK, fill_color=BLACK, fill_opacity=0.5)
        c02=Circle(color=BLACK, fill_color=BLACK, fill_opacity=0.5)
        c01.scale(0.45)
        c02.scale(0.45)
        robots = VGroup(square02, c01, c02)

        line01 = Line(np.array([-6, -2.4, 0]), np.array([6, -2.4, 0]), color=RED)
        line01.set_height(0.2)

        text01 = TextMobject("LOVE\nDEATH\n + \nROBOTS")
        text01.scale(1.8)
        text01.set_color_by_gradient(RED, ORANGE, YELLOW, GOLD, GREEN, BLUE, PURPLE)

        group_all = VGroup(love, death, robots, line01, text01)

        circle01.shift((UP + LEFT) * np.sqrt(2) / 2)
        circle02.shift((UP + RIGHT) * np.sqrt(2) / 2)
        square01.rotate(np.pi / 4)

        rect01.rotate(np.pi / 4)
        rect02.rotate(-np.pi / 4)

        c01.shift(np.array([-0.72, 0.6, 0]))
        c02.shift(np.array([0.72, 0.6, 0]))
        robots.shift(RIGHT * 4)

        text01.shift(DOWN * 2.5)

        self.play(ShowCreation(circle01), ShowCreation(circle02), ShowCreation(square01))
        self.wait(1)
        self.play(ApplyMethod(love.shift, LEFT * 4))
        self.wait(1)

        self.play(ShowCreation(rect01), ShowCreation(rect02))
        self.wait(1)

        self.play(ShowCreation(square02))
        self.play(ShowCreation(c01), ShowCreation(c02))
        self.wait(1)

        self.play(ApplyMethod(love.set_opacity, 1), ApplyMethod(death.set_opacity, 1),
        ApplyMethod(robots.set_opacity, 1))
        self.wait(1)
        self.play(ShowCreation(line01))
        self.wait(1)

        self.play(Transform(line01, text01))
        self.wait(1)
        self.play(ApplyMethod(group_all.shift, UP * 1))
        self.wait(1)

class TAA(Scene):
    def construct(self):
        quote = TextMobject("study hard on manim!")
        quote.set_color(GOLD)
        quote.to_edge(UP)
        quote2 = TextMobject("I will learn manim well", color=GREEN)
        author = TextMobject("hanger", color = PURPLE)

        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote, quote2),
        ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2*LEFT))
        self.play(ApplyMethod(author.scale, 1.6))
        author.match_color(quote2)
        '''
        self.play(FadeOut(quote), FadeOut(author))
        self.wait(2)
        '''

class moveText(Scene):
    def construct(self):
        square = Square(side_length = 5, fill_color = BLUE, fill_opacity = 0.5)
        label = TextMobject("tilt")
        label.bg = BackgroundRectangle(label, fill_opacity = 1)

        label_group = VGroup(label.bg, label)
        label_group.rotate(TAU / 6)

        label2 = TextMobject("surround", color = PINK)
        label2.bg = BackgroundRectangle(label2, color = BLUE_C, fill_color = RED_B, fill_opacity = 0.5)
        label2_group = VGroup(label2.bg, label2)
        label2_group.next_to(label_group, DOWN * 2 + RIGHT)
        label3 = TextMobject("rainbow color")
        label3.scale(1.4)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait(2)

class FL(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        base1 = TexMobject(
        "\\sum_{n=1}^\\infty "
        "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )

        VGroup(title, base1).arrange(DOWN)
        self.play(
        Write(title),
        FadeInFrom(base1, UP)
        )
        self.wait(2)

'''
TexMobject
TextMobject
'''


class FL2(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        base1 = TexMobject(
        "\\sum_{n=1}^\\infty "
        "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )

        VGroup(title, base1).arrange(DOWN)
        self.play(
        Write(title),
        FadeInFrom(base1, UP)
        )
        self.wait(2)


class PF(GraphScene):
    CONFIG = {
    "x_min": -10,
    "x_max": 10.3,
    "y_min": -1.5,
    "y_max": 1.5,
    "graph_origin": ORIGIN,
    "function_color": RED,
    "axis_color": GREEN,
    "x_labeled_nums": range(-10, 12, 2),
    "y_labeled_nums": range(-2, 2, 1),
    }

    def construct(self):
        self.setup_axes(animate = True)
        self.wait(2)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2, PURPLE)

        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)

        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val = -10,
        direction = UP / 2)
        two_pi = TexMobject("x = 2\\pi")

        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.wait(2)
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab),
        ShowCreation(graph_lab2), ShowCreation(two_pi))
        self.wait(2)

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)


class SP(ThreeDScene):
    def construct(self):
        r = 7
        sun = Sphere(radius = 1.6)
        planet = Sphere(radius = 0.4)
        orbit = Circle(radius = r)
        planet.shift(UP * r)
        system = VGroup(orbit, sun, planet)
        system.shift(DOWN * 2 + LEFT * 1.2)

        F_vector = Vector(np.array([0, -5, 0]), color = YELLOW)
        F_vector.next_to(planet, DOWN * 0.6)
        F_formula = TextMobject(
        '$\\vec{F}=G m_1 m_2 \\frac{(\\vec{r_1}\\vec{r_2})}{r^3}$', color = GOLD
        )
        F_formula.scale(1.5)

        F_formula.rotate_about_origin(PI / 2)
        F_formula.next_to(F_vector, LEFT * 0.4)

        self.set_camera_orientation(phi = 65*PI / 180, theta = PI / 3)

        self.play(ShowCreation(orbit))
        self.wait(1)
        self.play(FadeIn(sun), FadeInFromLarge(planet))
        self.wait(1)
        self.play(ShowCreation(F_vector))
        self.play(Write(F_formula))
        self.wait(2)

class sun_system(Scene):
    def construct(self):
        sun = Circle(radius = 0.5, color = RED, fill_color=RED, fill_opacity = 1)
        planet01 = Circle(radius = 0.2, color = BLUE, fill_color = BLUE, fill_opacity = 1)
        planet01.next_to(sun, RIGHT * 1)

        planet02 = Circle(radius = 0.2, color = GREEN, fill_color = GREEN, fill_opacity = 1)
        planet02.next_to(planet01, RIGHT)

        planet03 = Circle(radius = 0.2, color = YELLOW, fill_color = YELLOW, fill_opacity = 1)
        planet03.next_to(planet02, RIGHT)

        planet04 = Circle(radius = 0.2, color = MAROON, fill_color = MAROON, fill_opacity = 1)
        planet04.next_to(planet03, RIGHT)

        planet05 = Circle(radius = 0.2, color = PURPLE, fill_color = PURPLE, fill_opacity = 1)
        planet05.next_to(planet04, RIGHT)

        planet06 = Circle(radius = 0.2, color = GREY, fill_color = GREY, fill_opacity = 1)
        planet06.next_to(planet05, RIGHT)

        planet01.rotate_about_origin(PI *0.8)
        planet02.rotate_about_origin(TAU / 10)
        planet03.rotate_about_origin(TAU / 7)
        planet04.rotate_about_origin(TAU / 3)
        planet05.rotate_about_origin(TAU / 1.5)
        planet06.rotate_about_origin(-PI / 4)

        orbit01 = Circle(radius = 1, color = BLUE)
        orbit02 = Circle(radius = 1.6, color = GREEN)
        orbit03 = Circle(radius = 2.25, color = YELLOW)
        orbit04 = Circle(radius = 2.9, color = MAROON)
        orbit05 = Circle(radius = 3.525, color = PURPLE)
        orbit06 = Circle(radius = 4.15, color = GREY)
        orbits = VGroup(orbit01, orbit02, orbit03, orbit04, orbit05, orbit06)

        group = VGroup(sun, planet01, planet02, planet03, planet04, planet05, planet06)


        planets = VGroup(planet01, planet02, planet03, planet04, planet05, planet06)


        theta = 0.04

        speed = [3.5, 4, 2.5, 2, 1.25, 1]


        self.play(ShowCreation(orbits))
        self.play(GrowFromCenter(group))

        for i in range(70):
            index = [speed[m] * theta for m in range(6)]
            self.play(
            ApplyMethod(planet01.rotate_about_origin, index[0]),
            ApplyMethod(planet02.rotate_about_origin, index[1]),
            ApplyMethod(planet03.rotate_about_origin, index[2]),
            ApplyMethod(planet04.rotate_about_origin, index[3]),
            ApplyMethod(planet05.rotate_about_origin, index[4]),
            ApplyMethod(planet06.rotate_about_origin, index[5])
            )

class sun_system_3d(ThreeDScene):
    def construct(self):
        sun = Sphere(radius = 0.5, checkerboard_colors=[RED_D, RED_E], fill_opacity = 1)
        planet01 = Sphere(radius = 0.2, checkerboard_colors=[BLUE_D, BLUE_E], fill_color = BLUE, fill_opacity = 1)
        planet01.next_to(sun, RIGHT * 1)
        planet02 = Sphere(radius = 0.2, checkerboard_colors=[GREEN_D, GREEN_E], fill_opacity = 1)
        planet02.next_to(planet01, RIGHT * 1)
        planet03 = Sphere(radius = 0.2, checkerboard_colors=[YELLOW_D, YELLOW_E], fill_opacity = 1)
        planet03.next_to(planet02, RIGHT)
        planet04 = Sphere(radius = 0.2, checkerboard_colors=[MAROON_D, MAROON_E], fill_opacity = 1)
        planet04.next_to(planet03, RIGHT)
        planet05 = Sphere(radius = 0.2, checkerboard_colors=[PURPLE_D, PURPLE_E], fill_opacity = 1)
        planet05.next_to(planet04, RIGHT)
        planet06 = Sphere(radius = 0.2, checkerboard_colors=[LIGHT_GRAY, GRAY], fill_opacity = 1)
        planet06.next_to(planet05, RIGHT)

        planet01.rotate_about_origin(PI *0.8)
        planet02.rotate_about_origin(TAU / 10)
        planet03.rotate_about_origin(TAU / 7)
        planet04.rotate_about_origin(TAU / 3)
        planet05.rotate_about_origin(TAU / 1.5)
        planet06.rotate_about_origin(-PI / 4)


        orbit01 = Circle(radius = 1, color = BLUE)
        orbit02 = Circle(radius = 1.6, color = GREEN)
        orbit03 = Circle(radius = 2.25, color = YELLOW)
        orbit04 = Circle(radius = 2.9, color = MAROON)
        orbit05 = Circle(radius = 3.525, color = PURPLE)
        orbit06 = Circle(radius = 4.15, color = GREY)
        orbits = VGroup(orbit01, orbit02, orbit03, orbit04, orbit05, orbit06)

        group = VGroup(sun, planet01, planet02, planet03, planet04, planet05, planet06)


        planets = VGroup(planet01, planet02, planet03, planet04, planet05, planet06)


        theta = 0.04

        speed = [3.5, 4, 2.5, 2, 1.25, 1]

        self.set_camera_orientation(phi = 65 * PI / 180, theta = PI / 3)
        self.play(ShowCreation(orbits))
        self.play(GrowFromCenter(group))

        for i in range(70):
            index = [speed[m] * theta for m in range(6)]
            self.play(
            ApplyMethod(planet01.rotate_about_origin, index[0]),
            ApplyMethod(planet02.rotate_about_origin, index[1]),
            ApplyMethod(planet03.rotate_about_origin, index[2]),
            ApplyMethod(planet04.rotate_about_origin, index[3]),
            ApplyMethod(planet05.rotate_about_origin, index[4]),
            ApplyMethod(planet06.rotate_about_origin, index[5])
            )

class test_sphere(ThreeDScene):
    def construct(self):
        sun = Sphere(radius = 0.5, checkerboard_colors=[RED_D, RED_E], fill_opacity = 1)

        self.set_camera_orientation(phi=65 * PI / 180, theta=PI / 3)
        self.play(Write(sun))
