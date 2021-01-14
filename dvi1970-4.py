from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        self.wait()

        lg = TextMobject("\sffamily{Cramming}")
        lg.scale(1.2)
        lg.shift(UP * 0.25)
        lg2 = TextMobject("\sffamily{firstly}")
        lg2.scale(1.2)
        lg2.set_color(GREEN)
        lg2.next_to(lg, DOWN)
        self.play(DrawBorderThenFill(lg), DrawBorderThenFill(lg2))

        self.play(*(FadeOut(i) for i in self.get_mobjects()))


class Slide1(Scene):
    def construct(self):
        self.wait()
        title = TextMobject("Решить задачу:")
        task = TextMobject("""В выпуклом четырехугольнике $ABCD$ заключены две окружности одинакового радиуса $r$, 
                          касающиеся друг друга внешним образом. Центр первой окружности находится на отрезке, 
                          соединяющем вершину $A$ с серединой $F$ стороны $CD$, а центр второй окружности находится 
                          на отрезке, соединящем вершину $C$ с серединой $E$ стороны $AB$. Первая окружность касается 
                          сторон $AB$, $AD$, $CD$; вторая окружность касается сторон $AB$, $BC$, $CD$. Найти сторону $AC$.
                          """).scale(0.5)

        title.set_color(GREEN)

        title.shift(UP * 1.2)
        task.next_to(title, DOWN)
        box = SurroundingRectangle(task)
        box.set_color(DARK_GREY)

        self.play(ShowCreation(title), ShowCreation(task), ShowCreation(box))

        self.wait()

        self.play(*(FadeOut(i) for i in self.get_mobjects()))


class Slide2(Scene):
    def construct(self):
        circ1 = Circle(radius=1.5, stroke_width=1.2)
        circ2 = Circle(radius=1.5, stroke_width=1.2)
        circ1.set_color(BLUE)
        circ2.set_color(BLUE)

        cof = 1.5
        circ1.shift(LEFT * cof)
        circ2.shift(RIGHT * cof)
        self.wait()
        self.play(ShowCreation(circ1), ShowCreation(circ2))

        self.wait()
        c1 = Dot(circ1.get_center()).scale(0.5)
        c2 = Dot(circ2.get_center()).scale(0.5)

        cn1 = TexMobject("O_1").scale(0.5)
        cn2 = TexMobject("O_2").scale(0.5)

        cn1.next_to(c1, DOWN)
        cn2.next_to(c2, DOWN)

        self.play(ShowCreation(c1), ShowCreation(c2), ShowCreation(cn1), ShowCreation(cn2))
        self.wait()

        ab = Line(LEFT * 2.62, RIGHT * 2.4, stroke_width=1.7)
        cd = Line(LEFT * 3.5, RIGHT * 4, stroke_width=1.7)

        ab.shift(UP * 1.5)
        cd.shift(DOWN * 1.5)

        a = Dot(ab.get_start()).scale(0.5)
        an = TexMobject("A").scale(0.5)
        an.next_to(a, UP)
        b = Dot(ab.get_end()).scale(0.5)
        bn = TexMobject("B").scale(0.5)
        bn.next_to(b, UP)
        d = Dot(cd.get_start()).scale(0.5)
        dn = TexMobject("D").scale(0.5)
        dn.next_to(d, DOWN)
        c = Dot(cd.get_end()).scale(0.5)
        cn = TexMobject("C").scale(0.5)
        cn.next_to(c, DOWN)

        g = VGroup(a, an, b, bn, c, cn, d, dn)

        self.play(ShowCreation(ab), ShowCreation(cd), ShowCreation(g))

        self.wait()

        cb = Line(cd.get_end(), ab.get_end(), stroke_width=1.7)
        da = Line(cd.get_start(), ab.get_start(), stroke_width=1.7)
        self.play(ShowCreation(cb), ShowCreation(da))

        ce = Line(c.get_center(), circ2.get_center() + (circ2.get_center() - c.get_center()), stroke_width=1.7)

        e = Dot(ce.get_end()).scale(0.5)

        en = TexMobject("E").scale(0.5)
        en.next_to(e, UP)

        af = Line(a.get_center(), circ1.get_center() * 2 - a.get_center(), stroke_width=1.7)
        f = Dot(af.get_end()).scale(0.5)
        fn = TexMobject("F").scale(0.5)
        fn.next_to(f, DOWN)
        self.play(ShowCreation(ce), ShowCreation(en), ShowCreation(e), ShowCreation(af), ShowCreation(f),
                  ShowCreation(fn))

        g = VGroup(*self.get_mobjects())

        self.play(g.shift, LEFT * 3)
        self.wait()

        # Решение

        m = Line(circ1.get_center(), circ2.get_center(), stroke_width=1.7)

        self.play(ShowCreation(m))

        self.wait()

        s = TexMobject("O_1O_2|| AB", "|| DC").scale(0.5)

        line1 = Line(circ1.get_center(), circ1.get_center()+UP*1.5, stroke_width=1.7)
        line2 = Line(circ2.get_center(), circ2.get_center() + UP * 1.5, stroke_width=1.7)

        h1 = Dot(circ1.get_center()+UP*1.5).scale(0.5)
        h2 = Dot(circ2.get_center()+UP*1.5).scale(0.5)

        h1n = TexMobject("H_1").scale(0.5)

        h2n = TexMobject("H_2").scale(0.5)

        h1n.next_to(h1, UP)
        h2n.next_to(h2, UP)

        self.play(ShowCreation(line1), ShowCreation(line2), ShowCreation(h1), ShowCreation(h2), ShowCreation(h2n), ShowCreation(h1n))

        s0 = TextMobject("$O_1O_2H_2H_1 -$ прямоугольник").scale(0.5)

        s0.shift(RIGHT * 4 + UP * 3)

        self.play(FadeInFromDown(s0))

        self.wait()



        s.next_to(s0, DOWN)

        self.play(FadeInFromDown(s[0]))

        self.wait(2)

        g = VGroup(h1, h2, h1n, h2n, line1, line2, s0)

        self.play(FadeOut(g))

        self.wait()

        self.play(FadeInFromDown(s[1]))

        s11 = TextMobject("$O_1 - $ середина $AF$").scale(0.5)

        s1 = TextMobject("$O_2 -$ середина $CE$").scale(0.5)

        s11.next_to(s, DOWN)

        self.play(FadeInFromDown(s11))

        self.wait()

        s1.next_to(s11, DOWN)

        self.play(FadeInFromDown(s1))

        self.wait()

        self.play(Indicate(circ1, color=RED, scale_factor=1), time=2)

        def indicateDots(d):
            for i in d:
                self.play(i.set_color, RED)
                self.wait()
            g = VGroup(*d)
            self.play(g.set_color, WHITE)
            self.wait()

        indicateDots([dn, an, bn])



        s2 = TextMobject(r"$AF -$  биссектриса").scale(0.5)

        s2.next_to(s1, DOWN)

        self.wait()

        self.play(FadeInFromDown(s2))

        self.wait()

        ang1 = Sector(start_angle=-1.85, arc_center=a.get_center(), outer_radius=0.3, angle=0.94)
        ang1.set_color(color=[YELLOW, PINK])
        self.play(ShowCreation(ang1), ShowCreation(af.copy()), ShowCreation(da.copy()), ShowCreation(a.copy()))

        ang2 = Sector(start_angle=-1.85 + 0.94, arc_center=a.get_center(), outer_radius=0.3, angle=0.94)

        ang2.set_color(color=[YELLOW, PINK])

        self.play(ShowCreation(ang2), ShowCreation(ab.copy()), ShowCreation(af.copy()), ShowCreation(da.copy()), ShowCreation(a.copy()))

        ang3 = Sector(start_angle=PI - 0.94, arc_center=f.get_center(), outer_radius=0.3, angle=0.94)

        ang3.set_color(color=[PINK, YELLOW])

        self.play(ShowCreation(ang3), ShowCreation(cd.copy()), ShowCreation(af.copy()), ShowCreation(f.copy()))

        self.wait()

        self.play(Indicate(circ2, color=RED, scale_factor=1), time=2)

        indicateDots([dn, cn, bn])


        s3 = TextMobject(r"$CE -$  биссектриса").scale(0.5)

        s3.next_to(s2, DOWN)

        self.play(FadeInFromDown(s3))

        self.wait()
        a = 0.58
        col = [BLUE, GREEN]

        ang = Sector(start_angle=PI - a, arc_center=c.get_center(), outer_radius=0.3, angle=a)

        ang.set_color(color=col)

        self.play(ShowCreation(ang), ShowCreation(cd.copy()), ShowCreation(ce.copy()), ShowCreation(c.copy()))

        self.wait()

        angg = Sector(start_angle=PI - 2 * a + 0.1, arc_center=c.get_center(), outer_radius=0.3, angle=a)

        angg.set_color(color=col)

        self.play(ShowCreation(angg), ShowCreation(cb.copy()), ShowCreation(ce.copy()), ShowCreation(c.copy()))

        self.wait()

        angg1 = Sector(start_angle= -a, arc_center=e.get_center(), outer_radius=0.3, angle=a)

        angg1.set_color(color=[col[1], col[0]])

        self.play(ShowCreation(angg1), ShowCreation(ab.copy()), ShowCreation(ce.copy()), ShowCreation(e.copy()))

        self.wait()

        s4 = TextMobject(r"$\triangle DAF, \triangle CBE -$ равнобедренные").scale(0.5)

        s4.next_to(s3, DOWN)

        self.play(FadeInFromDown(s4))

        p1 = TexMobject("a").scale(0.5)

        p2 = TexMobject("b")

        p1.next_to(da, LEFT)
        p1.shift(RIGHT*0.5 + UP*0.2)

        self.play(ShowCreation(p1))

        p11 = TexMobject("a").scale(0.5)

        p11.next_to(cd, DOWN)

        p11.shift(LEFT*2.3)

        self.play(ShowCreation(p11))

        self.wait()

        p12 = TexMobject("a").scale(0.5)

        p12.next_to(cd, DOWN)
        p12.shift(RIGHT*1.7)

        self.play(ShowCreation(p12))

        self.wait()

        p2.next_to(cb, RIGHT)
        p2.scale(0.5)
        p2.shift(LEFT*0.9 + UP*0.2)

        self.play(ShowCreation(p2))

        p21 = TexMobject("b").scale(0.5)

        p21.next_to(ab, UP)

        p21.shift(RIGHT*0.7)

        self.play(ShowCreation(p21))

        p22 = TexMobject("b").scale(0.5)

        p22.next_to(ab, UP)
        p22.shift(LEFT*1.6)

        self.play(ShowCreation(p22))

        self.wait()

        s5 = TexMobject("O_1O_2 = 2\cdot r = {a + b \over 2}").scale(0.5)

        s5.next_to(s4, DOWN)

        self.play(FadeInFromDown(s5))

        self.wait()

        h2 = Line(circ2.get_center()+1.5*UP, circ2.get_center()+1.5*DOWN, stroke_width=1.7)



        h1 = Line(b.get_center(), b.get_center() + DOWN*3, stroke_width=1.7)

        h = Dot(circ2.get_center()+1.5*DOWN).scale(0.5)
        h11 = Dot(b.get_center() + DOWN*3).scale(0.5)
        hn = TexMobject("H").scale(0.5)
        h1n = TexMobject("H").scale(0.5)
        h1n.next_to(h11, DOWN)
        hn.next_to(h, DOWN)
        g = VGroup(h2, h, hn)
        self.play(ShowCreation(g))
        g1 = VGroup(h1, h11, h1n)

        self.wait()

        self.play(Transform(g, g1))

        self.wait()

        r2 = TexMobject("2\cdot r").scale(0.5)

        r2.next_to(h1.get_center(), LEFT)

        r2.shift(RIGHT*0.1 + UP*0.2)

        self.play(ShowCreation(r2))

        self.wait()

        s6 = TexMobject("BH = 2\cdot r \leq b").scale(0.5)

        s6.next_to(s5, DOWN)

        self.play(FadeInFromDown(s6))

        self.wait()

        s7 = TexMobject("BH = 2\cdot r \leq a").scale(0.5)

        s7.next_to(s6, DOWN)

        self.play(FadeInFromDown(s7))

        self.wait()

        final = TexMobject("2 \cdot r \leq {a + b \over 2}").scale(0.5)
        final.next_to(s7, DOWN)

        self.play(FadeInFromDown(final))

        final1 = TexMobject("b = a = 2\cdot r").scale(0.5)
        final1.next_to(final, DOWN)
        self.play(FadeInFromDown(final1))

        self.wait()

        delg = VGroup(s, s1, s2, s3, s4, s5, s11)
        gt = VGroup(s6, s7, final, final1)
        self.play(FadeOut(delg), gt.next_to, s0, DOWN)
        self.wait()

        s1 = TextMobject("$ABCD-$ прямоугольник").scale(0.5)

        s1.next_to(gt, DOWN)

        self.play(FadeInFromDown(s1))

        self.wait()

        s2 = TexMobject("AC = \sqrt{AD^2 + DC^2}").scale(0.5)

        s2.next_to(s1, DOWN)

        self.play(FadeInFromDown(s2))

        self.wait()

        s3 = TexMobject("AC = \sqrt{(2r)^2 + (4r)^2} = 2r\cdot \sqrt{5}").scale(0.5)

        s3.next_to(s2, DOWN)

        self.play(FadeInFromDown(s3))

        self.wait()

        ans = TextMobject("ОТВЕТ:").scale(0.9)
        ans2 = TexMobject("AC = 2r\cdot \sqrt{5}").scale(0.9)
        ans.set_color(color=GREEN)
        ans2.set_color(color=GREEN)
        ans.next_to(s3, DOWN)
        ans.shift(DOWN*0.5)
        ans2.next_to(ans, DOWN)
        self.play(ShowCreation(ans), ShowCreation(ans2))

        self.wait(2)

