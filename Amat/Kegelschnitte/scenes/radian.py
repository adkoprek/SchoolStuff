from manim import *
import numpy as np


class Radian(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-3, 3, 0.5],
            y_range=[-3, 3, 0.5],
            background_line_style={
                "stroke_color": BLUE_A,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
        )
        self.play(Create(grid))

        t = ValueTracker(0.001)

        # X-axis ray (long so it's treated as a half-line)
        x_axis = always_redraw(
            lambda: Line(ORIGIN, [1, 0, 0]).set_color(WHITE)
        )

        # Moving dot on the unit circle
        dot = always_redraw(
            lambda: Dot([np.cos(t.get_value()), np.sin(t.get_value()), 0])
        )

        # Line from origin to dot (hypotenuse)
        hyp = always_redraw(
            lambda: Line(ORIGIN, dot.get_center()).set_color(BLUE)
        )

        # Safe angle (ignore parallel cases)
        def make_angle():
            a1 = x_axis.get_angle()
            a2 = hyp.get_angle()
            if np.isclose(a1, a2):
                return VGroup()  # skip drawing when parallel
            return Angle(x_axis, hyp, radius=0.4, quadrant=(1,1))

        angle = always_redraw(make_angle)

        self.play(Create(x_axis), Create(dot), Create(hyp), Create(angle))
        self.play(t.animate.set_value(2 * np.pi - 0.001), run_time=5, rate_func=linear)
        self.wait()