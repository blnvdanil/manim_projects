from manimlib.imports import *
import os
import numpy as np

class Slide1(ThreeDScene):

    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }

        self.set_camera_orientation(phi=60*DEGREES, theta=60*DEGREES, distance=8)

        axes = ThreeDAxes(**axis_config)

        #self.add(axes)

        a = Dot(Y_AXIS*-2).scale(0.5)

        b = Dot(X_AXIS*1.789 + Y_AXIS*0.894).scale(0.5)

        c = Dot(-X_AXIS*1.789 + Y_AXIS*0.894).scale(0.5)

        ab = Line(a.get_center(), b.get_center(), stroke_width=1.7)

        bc = Line(b.get_center(), c.get_center(), stroke_width=1.7)

        ac = DashedLine(a.get_center(), c.get_center(), stroke_width=1.7)

        s = Dot(Z_AXIS*2).scale(0.5)

        sa = Line(s.get_center(), a.get_center(), stroke_width=1.7)

        sb = Line(s.get_center(), b.get_center(), stroke_width=1.7)

        sc = Line(s.get_center(), c.get_center(), stroke_width=1.7)

        #sa.set_color(GREEN)

        #sb.set_color(BLUE)

        #sc.set_color(PURPLE_A)



        #self.add(a, b, c, s)



        pyramid = VGroup(ac, ab, bc, sa, sb, sc)

        an = TexMobject("A").scale(0.5)
        an.shift(DOWN*1.35 + LEFT*1.5)

        cn = TexMobject("C").scale(0.5)
        cn.next_to(b)
        cn.shift(DOWN)

        bn = TexMobject("B").scale(0.5)
        bn.next_to(c)
        bn.shift(RIGHT*0.3 + DOWN*0.1)

        sn = TexMobject("S").scale(0.5)
        sn.shift(UP*2.2)


        names = VGroup(an, bn, cn, sn)

        names.set_color(BLACK)

        self.add_fixed_in_frame_mobjects(names)

        self.play(ShowCreation(ac), ShowCreation(ab), ShowCreation(bc), ShowCreation(sa), ShowCreation(sb), ShowCreation(sc), names.set_color, WHITE)

        a, b = b, a
        bh = DashedLine(b.get_center(), (a.get_center() + c.get_center()) / 2, stroke_width=1.7)

        self.wait()

        h = TexMobject("H").scale(0.5)

        h.shift(RIGHT*0.65 + DOWN*0.65)

        h.set_color(BLACK)

        self.add_fixed_in_frame_mobjects(h)

        bh.set_color(ORANGE)

        self.play(
            ShowCreation(bh), h.set_color,
            WHITE, ShowCreation(Line(bh.get_end() + DOWN*0.15, bh.get_end() + RIGHT*0.15 + DOWN*0.15, stroke_width=1.7)),
            ShowCreation(Line(bh.get_end() + RIGHT*0.15 + DOWN*0.15, bh.get_end() + RIGHT*0.15, stroke_width=1.7))

        )
        self.wait()

        mn = DashedLine(ab.get_center(), ac.get_center(), stroke_width=1.7)

        m = TexMobject("M", color=BLACK).scale(0.5)
        n = TexMobject("N", color=BLACK).scale(0.5)

        m.shift(LEFT*1.4)
        n.shift(RIGHT*0.7 + UP*0.6)

        self.add_fixed_in_frame_mobjects(m, n)

        s = TextMobject("$MN - $ средняя линия").scale(0.5)
        s.set_color(BLACK)
        s.shift(LEFT*5+UP*3)
        self.add_fixed_in_frame_mobjects(s)


        self.play(ShowCreation(mn), m.set_color, WHITE, n.set_color, WHITE, s.set_color, WHITE)

        self.wait()

        e = (mn.get_center() + mn.get_end()) / 2 + Z_AXIS

        bc, ac, ab = ac, bc, ab

        eb = DashedLine(e, bc.get_start(), stroke_width=1.7)

        eh = DashedLine(e, bh.get_end(), stroke_width=1.7)

        ed = TexMobject("E", color=BLACK).scale(0.5)

        ed.shift(UP*1.4 + RIGHT*0.2)

        self.add_fixed_in_frame_mobjects(ed)

        self.play(ShowCreation(eb), ShowCreation(eh), ed.set_color, WHITE)

        self.wait()

        ek = DashedLine(e, mn.get_center(), stroke_width=1.7, color=BLUE)



        k = TexMobject("K").scale(0.5)
        k.set_color(BLACK)
        k.shift(LEFT*0.3)
        self.add_fixed_in_frame_mobjects(k)
        self.play(ShowCreation(ek), k.set_color, WHITE)

        self.wait()
        def show(x, y):
            x.set_color(BLACK)
            self.add_fixed_in_frame_mobjects(x)
            x.next_to(y, DOWN)
            self.play(x.set_color, WHITE)

        s1 = TextMobject("$K - $ середина $BH$").scale(0.5)

        show(s1, s)

        self.wait()

        s2 = TextMobject(r"$EK \perp BH$").scale(0.5)

        show(s2, s1)

        self.wait()

        s3 = TextMobject("$MN \perp BH$").scale(0.5)

        show(s3, s2)

        self.wait()

        s4 = TexMobject("MEN \perp ABC").scale(0.5)

        show(s4, s3)

        s5 = TexMobject("SO \perp ABC").scale(0.5)

        so = DashedLine(Z_AXIS*2, Z_AXIS*2-Z_AXIS*2, stroke_width=1.7, color=GREEN)

        self.play(ShowCreation(so))

        show(s5, s4)

        s0 = TexMobject(r"S^\prime").scale(0.5)
        s0.set_color(BLACK)
        self.add_fixed_in_frame_mobjects(s0)

        s0.shift(DOWN*0.25)

        self.play(s0.set_color, WHITE)

        self.wait()

        e0 = TexMobject("E^\prime").scale(0.4)
        e0.set_color(BLACK)
        e0.shift(RIGHT*0.15 + UP*0.15)
        self.add_fixed_in_frame_mobjects(e0)

        ee0 = DashedLine(e, e - Z_AXIS, stroke_width=1.7, color=GREEN)

        self.play(ShowCreation(ee0))


        self.play(e0.set_color, WHITE)

        self.wait()









class Test(GraphScene):
    def construct(self):
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            return factorial(n-1)*n

        def taylor_approximation_cos(k, x):
            value = 0
            for i in range(k):
                value = value + ((x ** (2 * i) * (-1) ** i) / factorial(2 * i))
            return value

        def get(i):
            return self.get_graph(lambda x: taylor_approximation_cos(i, x), x_min=-3 * np.pi,
                                   x_max=3 * np.pi)

        self.setup_axes(animate=True)
        old = get(1)

        graph = get(0)
        self.play(ShowCreation(graph), run_time=3)

        for i in range(1, 15):
            new_graph = get(i)
            self.play(Transform(graph, new_graph), run_time=3)
            self.wait()

if __name__ == "__main__":
    os.system(r"python C:\Users\Danil\manim\manim.py dvi1970-5.py Slide1 -p")