from manim import *
import numpy as np

SHIFT = LEFT * 3
SCALE = 0.4

def ellipse_vertices(a, b):
    angles = np.linspace(0, 2 * np.pi, 100)
    return np.array([
        [a * np.cos(x), b * np.sin(x), 0] for x in angles
    ])

class EllipseIntuitive(Scene):
    def construct(self):
        # === Coordinate Plane ===
        axes = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": BLUE_A,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).shift(SHIFT).scale(SCALE)

        self.play(Create(axes))
        self.wait(1)

        # === ValueTrackers ===
        a = ValueTracker(1)
        b = ValueTracker(1)

        t1 = MathTex("\\left(")
        t2 = DecimalNumber(a.get_value(), num_decimal_places=2, include_sign=False).set_color(GREEN)
        t3 = MathTex("\\cdot \\cos t, ")
        t4 = DecimalNumber(b.get_value(), num_decimal_places=2, include_sign=False).set_color(RED)
        t5 = MathTex("\\cdot \\sin t \\right)")

        t6 = MathTex("a=").set_color(GREEN)
        t7 = DecimalNumber(a.get_value(), num_decimal_places=2, include_sign=False).set_color(GREEN)
        t8 = MathTex("b=").set_color(RED)
        t9 = DecimalNumber(b.get_value(), num_decimal_places=2, include_sign=False).set_color(RED)

        # Updaters for live numeric values
        t2.add_updater(lambda m: m.set_value(a.get_value()))
        t7.add_updater(lambda m: m.set_value(a.get_value()))
        t4.add_updater(lambda m: m.set_value(b.get_value()))
        t9.add_updater(lambda m: m.set_value(b.get_value()))

        # === Dynamic Formula ===
        formula = VGroup(
            VGroup(
                VGroup(t1, t2, t3).arrange(RIGHT, buff=0.1),
                VGroup(t4, t5).arrange(RIGHT, buff=0.1)
            ).arrange(RIGHT, buff=0.3),
            VGroup(t6, t7).arrange(RIGHT, buff=0.05),
            VGroup(t8, t9).arrange(RIGHT, buff=0.05)
        ).arrange(DOWN, buff=0.5)

        formula.next_to(axes, RIGHT, buff=0.8)
        self.play(Create(formula))
        self.wait(1)

        # === Dynamic Ellipse ===
        ellipse = always_redraw(
            lambda: Polygon(*ellipse_vertices(a.get_value(), b.get_value()))
            .shift(SHIFT)
            .scale(SCALE)
            .set_stroke(color=YELLOW, width=3)
        )

        lx = always_redraw(
            lambda: Line(
                start=[-a.get_value(), 0, 0],
                end=[a.get_value(), 0, 0])
            .shift(SHIFT)
            .scale(SCALE)
            .set_stroke(color=GREEN, width=5)
            .set_z_index(10)
        )
        ly = always_redraw(
            lambda: Line(
                start=[0, -b.get_value(), 0],
                end=[0, b.get_value(), 0])
            .shift(SHIFT)
            .scale(SCALE)
            .set_stroke(color=RED, width=5)
            .set_z_index(2)
        )

        self.add(ellipse, lx, ly)

        # === Animations ===
        self.play(a.animate.set_value(4), b.animate.set_value(1), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(9), b.animate.set_value(1), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(9), b.animate.set_value(9), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(1), b.animate.set_value(9), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(1), b.animate.set_value(1), run_time=2)
        self.wait(1)
