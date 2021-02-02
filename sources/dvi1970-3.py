from manim import*
import os

class Slide1(Scene):
    def construct(self):
        self.wait()
        title = Tex("Решить задачу:")
        task = Tex("""Три гонщика (сначала $A$, потом $B$ и затем $C$) стартуют с интервалом в 1 мин из одной точки кольцевого шоссе
                    и двигаются в одном направлении с постоянными скоростями.""", """ Каждый гонщик затрачивает на круг более двух
                    минут.""", """ Сделав три круга, гонщик $A$ в первый раз догоняет $B$ у точки старта,""", """ а еще через три минуты он
                    вторично обгоняет $C$.""", " Гонщик $B$ впервые догнал $C$ также у точки старта, закончив 4 круга.",
                   """ Сколько минут тратит на круг гонщик $A$?"""
            ).scale(0.5)

        title.set_color(GREEN)

        title.shift(UP * 1.2)
        task.next_to(title, DOWN)
        box = SurroundingRectangle(task)
        box.set_color(DARK_GREY)

        self.play(ShowCreation(title), ShowCreation(task), ShowCreation(box))

        self.wait(5)

        temp = UP * 2.5

        self.play(FadeOut(title))

        self.play( task.animate.shift(temp), box.animate.shift(temp))

        self.wait(2)

        path = Circle(radius=1.5, color=BLUE)

        path.shift(DOWN*1.5+RIGHT*4)

        self.play(ShowCreation(path))

        self.wait()

        # drivers dots
        start = Dot(path.get_top()).scale(0.7)
        a = MathTex("A, v_a").scale(0.5)
        ad = Dot(path.get_top()).scale(0.7)
        b = MathTex("B, v_b").scale(0.5)
        bd = Dot(path.get_top()).scale(0.7)
        c = MathTex("C, v_c").scale(0.5)
        cd = Dot(path.get_top()).scale(0.7)

        a.next_to(path, UP)
        b.next_to(path, UP)
        c.next_to(path, UP)
        value = ValueTracker(0)

        temp = 0.5

        tracker = DecimalNumber(0).add_updater(lambda x: x.set_value(value.get_value())).scale(temp)

        label = Tex("Время: ").scale(temp)
        minute = Tex("мин.").scale(temp)
        label.shift(RIGHT + UP*0.5)

        tracker.next_to(label, RIGHT)
        minute.next_to(tracker, RIGHT)

        hcolor = PINK

        self.play(ShowCreation(a), ShowCreation(ad),
                  ShowCreation(start), ShowCreation(tracker),
                  ShowCreation(label), ShowCreation(minute))

        self.wait()

        r = (a.get_center() - path.get_center())[1]

        # dot moving
        temp = Arc(start_angle=PI/2, angle=-PI/3, radius=(a.get_center() - path.get_center())[1], arc_center=path.get_center())

        self.play(MoveAlongPath(a, temp), Rotate(ad, angle=-PI/3, about_point=path.get_center()),
                  value.animate.set_value(1), run_time=3)

        self.play(ShowCreation(b), ShowCreation(bd))

        self.play(
            MoveAlongPath(
                a, Arc(
                    start_angle=PI/6, angle=-PI/3, radius=r, arc_center=path.get_center()
                )
            ), Rotate(ad, angle=-PI/3, about_point=path.get_center()), value.animate.set_value(2),
            MoveAlongPath(
                b, Arc(
                    start_angle=PI / 2, angle=-PI / 4, radius=r, arc_center=path.get_center()
                )
            ), Rotate(bd, angle=-PI/4, about_point=path.get_center()),
            run_time=3
        )

        self.play(ShowCreation(c), ShowCreation(cd))

        self.play(
            MoveAlongPath(
                a, Arc(
                    start_angle=-PI / 6, angle=-PI / 3, radius=r, arc_center=path.get_center()
                )
            ), Rotate(ad, angle=-PI / 3, about_point=path.get_center()), value.animate.set_value(3),
            MoveAlongPath(
                b, Arc(
                    start_angle=PI / 4, angle=-PI / 4, radius=r, arc_center=path.get_center()
                )
            ), Rotate(bd, angle=-PI / 4, about_point=path.get_center()),
            MoveAlongPath(
                c, Arc(
                    start_angle=PI/2, angle=-PI/6*1.7, radius=r, arc_center=path.get_center()
                )
            ), Rotate(cd, angle=-PI/6*1.7, about_point=path.get_center()),
            run_time=3
        )

        self.wait()

        self.play(task[2].animate.set_color(hcolor))

        self.wait()

        solution1 = MathTex(r"{3\cdot S \over v_a}", "=", r"{2\cdot S \over v_b}", "+ 1").scale(0.5)

        solution1.next_to(box, DOWN)
        solution1.shift(LEFT * 3 + DOWN)

        self.play(FadeIn(solution1[0]))

        self.play(FadeIn(solution1[2]))

        self.play(FadeIn(solution1[3]))

        self.play(FadeIn(solution1[1]))


        self.play(task[2].animate.set_color(WHITE), task[4].animate.set_color(hcolor))

        solution2 = MathTex(r"{4\cdot S \over v_b}", "=", r"{3\cdot S \over v_c}", "+1")
        solution2.next_to(solution1, DOWN).scale(0.5)

        self.play(FadeIn(solution2[0]))

        self.play(FadeIn(solution2[2]))

        self.play(FadeIn(solution2[3]))

        self.play(FadeIn(solution2[1]))

        self.wait()

        self.play(task[4].animate.set_color(WHITE), task[2].animate.set_color(hcolor), task[3].animate.set_color(hcolor))

        solution3 = MathTex(r"{3\cdot S \over v_a} + 3 ", " = ", r" {3\cdot S", r"+ 3\cdot v_a", r"-2\cdot S", r" \over v_c}", "+2").scale(0.5)

        solution3.next_to(solution2, DOWN)

        self.play(FadeIn(solution3[0]))

        self.play(FadeIn(solution3[1]))

        self.play(FadeIn(solution3[2]))

        self.play(FadeIn(solution3[3]))

        self.play(FadeIn(solution3[4]))

        self.play(FadeIn(solution3[5]))

        self.play(FadeIn(solution3[6]))

        self.play(task[2].animate.set_color(WHITE), task[3].animate.set_color(WHITE))

        self.wait()

        ta = MathTex(r"t_a = {S \over v_a}")

        tb = MathTex(r"t_b = {S \over v_b}")

        tc = MathTex(r"t_c = {S \over v_c}")

        tq = MathTex(r"t_a - ?").scale(0.5)

        tb.next_to(ta, DOWN)
        tc.next_to(tb, DOWN)
        g = VGroup(ta, tb, tc).scale(0.5)
        tq.next_to(g, DOWN)

        self.play(ShowCreation(g))

        self.play(ShowCreation(tq))

        self.wait()

        temp = MathTex(r"3\cdot t_a = 2\cdot t_b + 1").scale(0.5)

        temp.next_to(box, DOWN)
        temp.shift(LEFT * 3 + DOWN)

        self.play(Transform(solution1, temp))

        solution1 = temp

        temp = MathTex(r"4\cdot t_b = 3\cdot t_c +1").scale(0.5)

        temp.next_to(solution1, DOWN)

        self.play(Transform(solution2, temp))
        solution2 = temp

        temp = MathTex(r"3\cdot t_a +1 = t_c + 3 \cdot{t_c \over t_a}").scale(0.5)

        temp.next_to(solution2, DOWN)

        self.play(Transform(solution3, temp))
        solution3 = temp

        self.wait()

        solution4 = MathTex(r"t_c = {4\cdot t_b-1 \over 3}", r"= 2\cdot t_a-1").scale(0.5)

        solution4.next_to(solution3, DOWN)

        self.play(ShowCreation(solution4[0]))

        self.play(ShowCreation(solution4[1]))

        solution5 = MathTex(r"t_a^2 - 4t_a + 3 = 0").scale(0.5)

        solution5.next_to(solution4, DOWN)

        self.play(ShowCreation(solution5))

        self.wait()

        solution6 = MathTex(r"t_a = 3").scale(0.5)

        solution6.next_to(solution5, DOWN)

        ans = Tex("ОТВЕТ:").scale(0.7)
        ans.set_color(GREEN)

        ans.next_to(solution6, LEFT)

        self.play(ShowCreation(solution6))

        self.wait()

        self.play(ShowCreation(ans))


        self.wait(5)

















if __name__ == '__main__':
    os.system(r"python3 -m manim dvi1970-3.py Slide1 -p")
    #Slide1().render()