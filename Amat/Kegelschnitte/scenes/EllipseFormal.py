from manim import *

SHIFT = UP * 1.5


class EllipseFormal(Scene):
    def construct(self):
        # === Main ellipse equation ===
        ellipse = MathTex("\\frac{x^2}{a^2}", "+", "\\frac{y^2}{b^2}", "= 1")
        ellipse.shift(SHIFT)

        self.play(Create(ellipse))
        self.wait(1)

        # === Placeholder param functions ===
        x_func = MathTex("x(t)=?").next_to(ellipse, DOWN, buff=1)
        y_func = MathTex("y(t)=?").next_to(x_func, DOWN)
        x_func.set_color(BLUE)
        y_func.set_color(RED)

        func_group = VGroup(x_func, y_func)

        self.play(Create(x_func), Create(y_func))
        self.wait(1)

        # === First solution step ===
        x_func0 = MathTex(r"x(t)=\cos(t)").next_to(ellipse, DOWN, buff=1)
        y_func0 = MathTex(r"y(t)=\sin(t)").next_to(x_func, DOWN)
        x_func0.set_color(BLUE)
        y_func0.set_color(RED)
        self.play(
            ReplacementTransform(x_func, x_func0),
            ReplacementTransform(y_func, y_func0)
        )
        self.wait(1)

        # === Substitute into ellipse ===
        ellipse1 = MathTex("\\frac{\\cos ^2 t}{a^2}", "+", "\\frac{\\sin ^2 t}{b^2}", "= 1")
        ellipse1.shift(SHIFT)
        ellipse1[0][0:5].set_color(BLUE)
        ellipse1[2][0:5].set_color(RED)
        self.play(ReplacementTransform(ellipse, ellipse1))
        self.wait(1)

        # === Cross to indicate mistake ===
        cross = Cross().next_to(ellipse, RIGHT)
        cross.set_color(RED)
        cross.scale(.2)
        self.play(Create(cross))
        self.wait(1)

        # === Correct x(t) ===
        x_func1 = MathTex(r"x(t)=a \cos(t)").next_to(ellipse, DOWN, buff=1)
        x_func1.set_color(BLUE)
        ellipse2 = MathTex("\\frac{a^2 \\cos ^2 t}{a^2}", "+", "\\frac{y^2}{b^2}", "= 1")
        ellipse2.shift(SHIFT)
        ellipse2[0][0:7].set_color(BLUE)
        self.play(
            ReplacementTransform(x_func0, x_func1),
            ReplacementTransform(ellipse1, ellipse2)
        )
        self.wait(1)

        # === Simplify ellipse ===
        ellipse3 = MathTex("\\cos ^2 t", "+", "\\frac{y^2}{b^2}", "= 1")
        ellipse3.shift(SHIFT)
        ellipse3[0][0:5].set_color(BLUE)
        self.play(ReplacementTransform(ellipse2, ellipse3))
        self.wait(1)

        # === Correct y(t) ===
        y_func1 = MathTex(r"y(t)=b \sin(t)").next_to(x_func, DOWN)
        y_func1.set_color(RED)
        ellipse4 = MathTex("\\cos ^2 t", "+", "\\sin^2 t", "= 1")
        ellipse4.shift(SHIFT)
        ellipse4[0][0:5].set_color(BLUE)
        ellipse4[2][0:5].set_color(RED)
        self.play(
            ReplacementTransform(y_func0, y_func1),
            ReplacementTransform(ellipse3, ellipse4)
        )
        self.wait(1)

        # === Transform cross into green check mark ===
        check = VMobject()
        points = [
            np.array([-1.5, 0, 0]),
            np.array([-1, -0.5, 0]),
            np.array([0, 0.5, 0])
        ]
        check.set_points_as_corners(points)
        check.set_color(GREEN)
        check.set_stroke(width=4)
        check.scale(.2)
        check.next_to(ellipse, RIGHT)
        self.play(Transform(cross, check))

        box = SurroundingRectangle(func_group, color=YELLOW, buff=0.4)
        self.play(Create(box))
        self.wait(1)
