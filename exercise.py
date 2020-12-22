from manimlib.imports import *
import os
import pyclbr

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
