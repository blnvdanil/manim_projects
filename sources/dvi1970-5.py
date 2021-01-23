from manim import *
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

        self.play(ShowCreation(ac), ShowCreation(ab), ShowCreation(bc), ShowCreation(sa), ShowCreation(sb), ShowCreation(sc), ApplyMethod(names.set_color, WHITE))

        a, b = b, a
        bh = DashedLine(b.get_center(), (a.get_center() + c.get_center()) / 2, stroke_width=1.7)

        self.wait()

        h = TexMobject("H").scale(0.5)

        h.shift(RIGHT*0.65 + DOWN*0.65)

        h.set_color(BLACK)

        self.add_fixed_in_frame_mobjects(h)

        bh.set_color(ORANGE)

        self.play(
            ShowCreation(bh), ApplyMethod(h.set_color,
            WHITE), ShowCreation(Line(bh.get_end() + DOWN*0.15, bh.get_end() + RIGHT*0.15 + DOWN*0.15, stroke_width=1.7)),
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


        self.play(ShowCreation(mn), ApplyMethod(m.set_color, WHITE), ApplyMethod(n.set_color, WHITE), ApplyMethod(s.set_color, WHITE))

        self.wait()

        e = (mn.get_center() + mn.get_end()) / 2 + Z_AXIS

        bc, ac, ab = ac, bc, ab

        eb = DashedLine(e, bc.get_start(), stroke_width=1.7)

        eh = DashedLine(e, bh.get_end(), stroke_width=1.7)

        ed = TexMobject("E", color=BLACK).scale(0.5)

        ed.shift(UP*1.4 + RIGHT*0.2)

        self.add_fixed_in_frame_mobjects(ed)

        self.play(ShowCreation(eb), ShowCreation(eh), ApplyMethod(ed.set_color, WHITE))

        self.wait()

        ek = DashedLine(e, mn.get_center(), stroke_width=1.7, color=BLUE)



        k = TexMobject("K").scale(0.5)
        k.set_color(BLACK)
        k.shift(LEFT*0.3)
        self.add_fixed_in_frame_mobjects(k)
        self.play(ShowCreation(ek), ApplyMethod(k.set_color, WHITE))

        self.wait()
        def show(x, y):
            x.set_color(BLACK)
            self.add_fixed_in_frame_mobjects(x)
            x.next_to(y, DOWN)
            self.play(ApplyMethod(x.set_color, WHITE))

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

        s5 = TexMobject("SS^\prime \perp ABC").scale(0.5)

        so = DashedLine(Z_AXIS*2, Z_AXIS*2-Z_AXIS*2, stroke_width=1.7, color=GREEN)

        self.play(ShowCreation(so))

        show(s5, s4)

        s0 = TexMobject(r"S^\prime").scale(0.5)
        s0.set_color(BLACK)
        self.add_fixed_in_frame_mobjects(s0)

        s0.shift(DOWN*0.25)

        self.play(ApplyMethod(s0.set_color, WHITE))

        self.wait()

        e0 = TexMobject("E^\prime").scale(0.4)
        e0.set_color(BLACK)
        e0.shift(RIGHT*0.15 + UP*0.15)
        self.add_fixed_in_frame_mobjects(e0)

        ee0 = DashedLine(e, e - Z_AXIS, stroke_width=1.7, color=GREEN)

        self.play(ShowCreation(ee0))


        self.play(ApplyMethod(e0.set_color, WHITE))

        self.wait()

        l1 = Line(UP-UP, UP*2.5, stroke_width=1.7)

        l1.shift(UP + RIGHT*3.5)


        s1 = TexMobject("S^\prime").scale(0.5)

        s = TexMobject("S").scale(0.5)

        s.shift(UP*3.5 + RIGHT*3.2)
        s1.shift(UP + RIGHT*3.2)






        l2 = Line(UP-UP, UP*1.5, stroke_width=1.7)
        l2.shift(UP + RIGHT * 5)

        e = TexMobject("E").scale(0.5)
        e1 = TexMobject("E^\prime").scale(0.5)

        e.shift(UP*2.5 + RIGHT*5.3)
        e1.shift(UP + RIGHT*5.3)

        l3 = Line(l1.get_end(), l2.get_end(), stroke_width=1.7)

        l4 = Line(l1.get_start(), l2.get_start(), stroke_width=1.7)

        g = VGroup(s1, s, l1, l2, e, e1, l3, l4)

        self.add_fixed_in_frame_mobjects(g)
        self.play(ShowCreation(g), run_time = 3)

        l5 =DashedLine(l2.get_end(), l2.get_end() + LEFT*1.5, stroke_width=1.7)

        lx = Line(l2.get_end() + LEFT*1.5, l1.get_end(), stroke_width=1.7)

        self.add_fixed_in_frame_mobjects(lx)

        h = TexMobject("P").scale(0.5)
        h.shift(UP*2.5 + RIGHT * 3.2)
        self.wait()

        self.add_fixed_in_frame_mobjects(l5, h)
        self.play(ShowCreation(l5), ShowCreation(h))
        self.wait()
        # рисуем ABC
        c1 = Line(l4.get_center() + DOWN, l4.get_center() + DOWN*3.7 + LEFT*1.6, stroke_width=1.7)

        c2 = Line(l4.get_center() + DOWN, l4.get_center() + DOWN*3.7 + RIGHT*1.6, stroke_width=1.7)

        c3 = Line(c1.get_end(), c2.get_end(), stroke_width=1.7)

        b2 = TexMobject("B").scale(0.5)

        b2.next_to(c1.get_start(), UP)

        a2 = TexMobject("A").scale(0.5)

        a2.next_to(c3.get_start(), LEFT)

        c4 = TexMobject("C").scale(0.5)

        c4.next_to(c3.get_end(), RIGHT)



        g1 = VGroup(c1, c2, c3)

        g2 = VGroup(b2, a2, c4)
        self.add_fixed_in_frame_mobjects(g1)
        self.play(ShowCreation(g1), run_time=2)
        self.wait()
        self.add_fixed_in_frame_mobjects(g2)
        self.play(ShowCreation(g2), run_time=2)
        self.wait()

        bh = Line(c1.get_start(), c1.get_start() + DOWN*2.7, stroke_width=1.7)
        d = TexMobject("H").scale(0.5)
        d.next_to(c3, DOWN)
        self.add_fixed_in_frame_mobjects(bh, d)
        self.play(ShowCreation(bh), ShowCreation(d))


        dt = Dot(bh.get_end() - (bh.get_end() - bh.get_start()) * 0.3).scale(0.5)
        e1 = TexMobject("S^\prime").scale(0.5)
        e1.next_to(dt, LEFT)
        e1.shift(RIGHT*0.1)
        self.add_fixed_in_frame_mobjects(e1, dt)
        self.play(ShowCreation(e1), ShowCreation(dt))
        self.wait()
        m = TexMobject("M").scale(0.5)
        n = TexMobject("N").scale(0.5)
        n.next_to(c1, LEFT)
        n.shift(RIGHT*0.7)
        m.next_to(c2, RIGHT)
        m.shift(LEFT*0.7)
        mn = Line(c1.get_center(), c2.get_center(), stroke_width=1.7)
        e = Dot(mn.get_center() + (mn.get_end() - mn.get_start()) * 0.3).scale(0.5)
        ep = TexMobject("E^\prime").scale(0.5)
        ep.next_to(e, DOWN)
        ep.shift(RIGHT*0.1)
        k = Dot(mn.get_center()).scale(0.5)
        kn = TexMobject("K").scale(0.5)
        kn.next_to(k, UP)
        kn.shift(LEFT*0.2 + DOWN*0.1)

        es = Line(dt.get_center(), mn.get_center() + (mn.get_end() - mn.get_start()) * 0.3, stroke_width=1.7)


        g3 = VGroup(m, n, mn, e, ep, k, kn, es)
        self.add_fixed_in_frame_mobjects(g3)
        self.play(ShowCreation(g3))

        self.wait()

        s6 = TexMobject(r"BH = {\sqrt{3} \over 2}").scale(0.5)

        s6.next_to(s5, DOWN)
        self.add_fixed_in_frame_mobjects(s6)
        self.play(FadeInFrom(s6))

        self.wait()

        s7 = TexMobject(r"KH = {\sqrt{3} \over 4}").scale(0.5)
        s7.next_to(s6, DOWN)
        self.add_fixed_in_frame_mobjects(s7)
        self.play(FadeInFrom(s7))

        self.wait()

        s8 = TexMobject(r"S^\prime H = {\sqrt{3} \over 6}").scale(0.5)
        s8.next_to(s7, DOWN)
        self.add_fixed_in_frame_mobjects(s8)
        self.play(FadeInFrom(s8))

        s9 = TexMobject(r"KS^\prime = {\sqrt{3} \over 12}").scale(0.5)
        s9.next_to(s8, DOWN)
        self.add_fixed_in_frame_mobjects(s9)
        self.play(FadeInFrom(s9))

        self.wait()

        self.play(ApplyMethod(s9.next_to, s6, DOWN), FadeOut(s8), FadeOut(s7))

        self.wait()

        s10 = TexMobject(r"KE  = BE \cdot \sin 60^\circ = {3 \over 4}").scale(0.5)

        s10.next_to(s9, DOWN)

        self.add_fixed_in_frame_mobjects(s10)
        self.play(FadeInFrom(s10))

        self.wait()

        s11 = TexMobject(r"KE^\prime  = KE \cdot \cos \alpha = {3 \over 4} \cos \alpha").scale(0.5)

        s11.next_to(s10, DOWN)
        self.add_fixed_in_frame_mobjects(s11)
        self.play(FadeInFrom(s11))
        self.wait()

        s12 = TexMobject(r"S^\prime E^\prime = \sqrt{{3 \over 12^2} + {9 \over 16} \cos^2\alpha}").scale(0.5)

        s12.next_to(s11, DOWN)

        self.add_fixed_in_frame_mobjects(s12)
        self.play(FadeInFrom(s12))

        self.wait()

        self.play(ApplyMethod(l5.set_color, RED))

        self.wait()
        s8.next_to(s6, DOWN)

        self.play(FadeOut(s9), FadeOut(s11),
                  FadeOut(g3), FadeOut(g2), FadeOut(g1), FadeOut(bh), FadeOut(d),
                  FadeOut(e1), FadeOut(dt), FadeOut(s6))
        self.play(ApplyMethod(s10.next_to, s5, DOWN))
        self.play(ApplyMethod(s12.next_to, s10, DOWN))
        self.wait()

        s13 = TexMobject(r"BS^\prime = {\sqrt{3} \over 3}").scale(0.5)

        s13.next_to(s12, DOWN)
        self.add_fixed_in_frame_mobjects(s13)
        self.play(FadeInFrom(s13))

        self.wait()

        s14 = TexMobject(r"SS^\prime = \sqrt{BS^2 - BS^{\prime2}} = \sqrt{{2 \over 3}}").scale(0.5)

        s14.next_to(s13, DOWN)

        self.add_fixed_in_frame_mobjects(s14)
        self.play(FadeInFrom(s14))
        self.wait()

        s15 = MathTex(r"EE^\prime = KE \cdot \sin\alpha = {3 \over 4} \sin\alpha").scale(0.5)
        s15.next_to(s14, DOWN)
        self.add_fixed_in_frame_mobjects(s15)
        self.play(FadeInFrom(s15))
        self.wait()

        s16 = MathTex(r"SP = SS^\prime - EE^\prime = \sqrt{2 \over 3} - {3 \over 4} \sin\alpha").scale(0.5)

        s16.next_to(g, DOWN)
        s16.shift(DOWN)
        self.add_fixed_in_frame_mobjects(s16)
        self.play(FadeInFrom(s16))
        self.wait()

        self.add_fixed_in_frame_mobjects(lx)

        self.play(ApplyMethod(lx.set_color, RED))

        self.wait()

        s17 = MathTex(r"SE = \sqrt{SP^2 + PE^2} = \sqrt{SP^2 + S^\prime E^{\prime2}}").scale(0.5)
        s17.next_to(s16, DOWN)
        self.add_fixed_in_frame_mobjects(s17)
        self.play(FadeInFrom(s17))
        self.wait()

        s18 = MathTex(r"SE = {1 \over 2} \cdot \sqrt{5 - 2 \sqrt{6} \sin\alpha}").scale(0.5)
        s18.next_to(s17, DOWN)
        self.add_fixed_in_frame_mobjects(s18)
        self.play(FadeInFrom(s18))

        ans = Tex(r"ОТВЕТ: ${1 \over 2} \cdot \sqrt{5 - 2 \sqrt{6} \sin\alpha}$").scale(0.7)
        ans.set_color(GREEN)
        ans.shift(DOWN*2.5)
        self.add_fixed_in_frame_mobjects(ans)
        self.play(FadeInFrom(ans))
        self.wait()


class Test(Scene):
    def construct(self):
        t = Triangle()
        d = Dot(t.get_vertices()[0])
        self.add(t, d)
        self.wait()



if __name__ == "__main__":
    os.system(r"manim dvi1970-5.py Slide1 -p")







