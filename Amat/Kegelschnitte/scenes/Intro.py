from manim import *
import numpy as np

from manim import *

SCALE = 1.5
SHIFT = 2.5 * LEFT


class Intro(Scene):
    def construct(self):
        a = ValueTracker(0.001)

        # === CIRCLE AND DOT ===
        dot = always_redraw(
            lambda: Dot(
                [1.5 * np.cos(a.get_value()), 1.5 * np.sin(a.get_value()), 0],
                color=YELLOW
            ).shift(SHIFT)
        )

        self.play(Create(dot))
        self.wait(1)

        # === FIRST ROTATION (WITHOUT GRID) ===
        self.play(
            a.animate.set_value(2 * np.pi),
            run_time=2*np.pi,
            rate_func=linear
        )
        self.wait(1)
        a.set_value(0)

        # === ADD GRID ===
        grid = NumberPlane(
            x_range=[-3, 3, 0.5],
            y_range=[-3, 3, 0.5],
            background_line_style={
                "stroke_color": BLUE_A,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
        ).shift(SHIFT)

        self.play(FadeIn(grid))
        self.wait(1)

        # === TRACED PATH + PROJECTION LINES ===
        traced_path = TracedPath(
            dot.get_center,
            stroke_color=YELLOW,
            stroke_width=3
        )

        x_line = always_redraw(lambda: Line(
            start=[dot.get_x(), SHIFT[1], 0],
            end=dot.get_center(),
            color=RED
        ))
        y_line = always_redraw(lambda: Line(
            start=[SHIFT[0], dot.get_y(), 0],
            end=dot.get_center(),
            color=GREEN
        ))

        # === COORDINATE AND TIME LABELS ===
        texts = always_redraw(
            lambda: VGroup(
                MathTex(
                    f"\\left({(dot.get_x() - SHIFT[0])/SCALE:.2f}, {(dot.get_y()-SHIFT[1])/SCALE:.2f} \\right)"
                ),
                MathTex(f"t = {a.get_value():.2f}"),
                Label("place").set_color(BLACK),
                Label("plaec").set_color(BLACK)
            ).arrange(DOWN, buff=0.4).next_to(grid, RIGHT, buff=1)
        )

        self.add(grid, traced_path, x_line, y_line, texts)

        self.play(
            a.animate.set_value(2 * np.pi),
            run_time=2*np.pi,
            rate_func=linear
        )
        self.wait(1)

        self.play(FadeOut(x_line), FadeOut(y_line))
        a.set_value(0)

        x_axis = always_redraw(
            lambda: Line(ORIGIN, [1, 0, 0])
                .set_stroke(WHITE, 0.5)
        )
        self.add(x_axis)

        hyp = always_redraw(
            lambda: Line(SHIFT, dot.get_center())
                .set_color(BLUE)
        )
        self.play(Create(hyp))

        def make_angle():
            a1 = x_axis.get_angle()
            a2 = hyp.get_angle()
            if np.isclose(a1, a2):
                return VGroup()
            return Angle(x_axis, hyp, radius=0.4, quadrant=(1,1)).set_color(RED)

        angle = always_redraw(make_angle)
        self.play(Create(angle))

        def make_label():
            theta_val = a.get_value()
            label = MathTex(
                rf"{theta_val:.2f}",
                color=RED
            ).scale(0.7)
            label.shift(
                SHIFT + 
                [2 * np.cos(a.get_value() + 0.1), 2 * np.sin(a.get_value() + 0.1), 0]
            )
            return label

        theta_label = always_redraw(make_label)
        self.play(Create(theta_label))

        self.play(
            a.animate.set_value(6.28), 
            run_time=2*np.pi,
            rate_func=linear
        )

        # === EQUATIONS APPEAR ===
        texts2 = VGroup(
            MathTex(
                f"\\left({(dot.get_x() - SHIFT[0])/SCALE:.2f}, {(dot.get_y()-SHIFT[1])/SCALE:.2f} \\right)"
            ),
            MathTex(f"t = {a.get_value():.2f}"),
            MathTex("x(t) = ?"),
            MathTex("y(t) = ?")
        ).arrange(DOWN, buff=0.4).next_to(grid, RIGHT, buff=1)

        self.play(Transform(texts, texts2))
        self.wait(1)
