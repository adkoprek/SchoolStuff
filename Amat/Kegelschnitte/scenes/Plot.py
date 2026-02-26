from manim import *
import numpy as np


SHIFT = 3 * RIGHT 

def half_ellipse_points(a, b):
    x_points = np.linspace(-a, a, 100)
    return np.array([
        [x, b * np.sqrt(1 - (x ** 2) / (a ** 2)), 0] for x in x_points
    ])

def ellipse_to_angle(a, b, t):
    angles = np.linspace(0, t, 100)
    return np.array([
        [a * np.cos(l), b * np.sin(l), 0] for l in angles 
    ])


class Plot(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-3, 3, 0.5],
            y_range=[-3, 3, 0.5],
            background_line_style={
                "stroke_color": BLUE_A,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).shift(SHIFT)
        arrow = Arrow().next_to(grid, LEFT, buff=1)
        formula = MathTex("\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1").next_to(arrow, LEFT, buff=1)

        self.play(Create(formula), Create(arrow), Create(grid))
        self.wait(1)

        formula_u = MathTex(
            "y=b \\cdot \\sqrt{1 - \\frac{x^2}{a^2}}"
        ).set_color(RED).scale(0.7)

        formula_d = MathTex(
            "y=- b \\cdot \\sqrt{1 - \\frac{x^2}{a^2}}"
        ).set_color(GREEN).scale(0.7)

        formulas = VGroup(
            formula_u,
            formula_d
        ).arrange(DOWN, buff=1).next_to(arrow, LEFT, buff=1)

        self.play(Transform(formula, formulas))
        self.wait(1)

        points = half_ellipse_points(2, 1)
        ellipse_u = Line().set_points_as_corners(points).set_color(RED)
        ellipse_u.shift(SHIFT)
        self.play(Create(ellipse_u))
        self.wait(1)

        ellipse_d = Line().set_points_as_corners(-points).set_color(GREEN)
        ellipse_d.shift(SHIFT)
        self.play(Create(ellipse_d))
        self.wait(1)

        self.play(FadeOut(ellipse_u), FadeOut(ellipse_d), FadeOut(formula))
        self.wait(1)

        t = ValueTracker(0)

        formula_para = MathTex(
            "(a \\cdot \\cos t, b \\cdot \\sin t)"
        )
        t_ui = DecimalNumber(t.get_value(), num_decimal_places=2, include_sign=False)
        t_ui.add_updater(lambda l: l.set_value(t.get_value()))

        parameter = VGroup(
            formula_para,
            VGroup(
                MathTex("t="),
                t_ui
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.6).next_to(arrow, LEFT, buff=0.3).scale(0.8)

        self.play(Create(parameter))
        self.wait(1)

        ellipse = always_redraw(
            lambda: Line()
            .set_points_as_corners(ellipse_to_angle(2, 1, t.get_value()))
            .shift(SHIFT)
            .set_stroke(color=YELLOW, width=3)
        )
        self.add(ellipse)

        tip = always_redraw(
            lambda: Dot(ellipse.get_end())
        )
        self.add(tip)

        self.play(t.animate.set_value(2 * np.pi), run_time=6.28, rate_func=linear)
        self.wait(1)

        self.play(t.animate.set_value(4 * np.pi), run_time=6.28, rate_func=linear)
        self.wait(1)
