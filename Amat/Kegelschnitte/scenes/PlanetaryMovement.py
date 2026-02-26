from manim import *


scale = 0.025
shift = 2.4 * LEFT
c_val = scale * 2.5
a_val = scale * 149.6
b_val = scale * 149

class PlanetaryMovement(Scene):
    def construct(self):
        c = ValueTracker(c_val)    
        a = ValueTracker(b_val)    
        b = ValueTracker(a_val)    

        axes = NumberPlane(
            x_range=[-500, 500, 10],
            y_range=[-300, 300, 10],
            background_line_style={

                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).scale(scale).shift(shift)
        self.play(Create(axes))

        sun = always_redraw(
            lambda: Dot([c.get_value(), 0, 0], 8)
                    .scale(scale)
                    .shift(shift)
                    .set_color(YELLOW)
        )

        ellipse = always_redraw(
            lambda: Ellipse(2 * a.get_value(), 2 * b.get_value()).set_color(BLUE).shift(shift)
        )
        self.play(Create(sun), Create(ellipse))
        self.wait(1)

        major = always_redraw(
            lambda: Line(
                start=[-a.get_value(), 0, 0],
                end=[0, 0, 0],
            ).set_color(GREEN).shift(shift)
        )
        major_label = MathTex(f"a={a_val/scale}").set_color(GREEN)
        major_label.next_to(major, UP, buff=0.2)
        self.play(Create(major), Create(major_label))
        self.wait(1)

        minor = always_redraw(
            lambda: Line(
                start=[0, 0, 0],
                end=[0, b.get_value(), 0],
            ).set_color(RED).shift(shift)
        )
        minor_label = MathTex(f"b={b_val/scale}").set_color(RED)
        minor_label.next_to(major, RIGHT, buff=0.2)
        minor_label.shift(1.8 * UP)
        self.play(Create(minor), Create(minor_label))
        self.wait(1)

        self.play(
            b.animate.set_value(120 * scale),
            c.animate.set_value(90 * scale)
        )
        self.wait(1)

        t = ValueTracker(1 / 7)

        pluto = always_redraw(
            lambda: Dot(
                [a.get_value() * np.cos(t.get_value() * 2 * np.pi),
                 b.get_value() * np.sin(t.get_value() * 2 * np.pi),
                 0],
                radius=0.1
            ).set_color(DARK_BROWN).shift(shift)
        )
        self.play(Create(pluto))
        self.wait(1)

        time = DecimalNumber(t.get_value(), num_decimal_places=2)
        time.add_updater(lambda l: l.set_value(t.get_value()))

        time_label = VGroup(
            MathTex("t="),
            time
        ).arrange(RIGHT, buff=0.1)

        time_label.shift(3 * UP + 4 * RIGHT)
        self.play(Create(time_label))
        self.wait(1)

        t1 = DecimalNumber(t.get_value(), num_decimal_places=2)
        t1.add_updater(lambda l: l.set_value(t.get_value()))
        t2 = DecimalNumber(t.get_value(), num_decimal_places=2)
        t2.add_updater(lambda l: l.set_value(t.get_value()))

        x_cor = VGroup(
            MathTex(f"x(t)={a_val / scale} \\cdot \\cos(", "2\\pi", "\\cdot"),
            t1,
            MathTex(")"),
        ).arrange(RIGHT, buff=0.1).scale(0.7)
        y_cor = VGroup(
            MathTex(f"y(t)={b_val / scale} \\cdot \\sin(", "2\\pi", "\\cdot"),
            t2,
            MathTex(")")
        ).arrange(RIGHT, buff=0.1).scale(0.7)
        x_cor.next_to(time, DOWN, buff=0.6)
        y_cor.next_to(x_cor, DOWN)

        self.play(Create(x_cor), Create(y_cor))
        self.wait(1)

        t12 = DecimalNumber(t.get_value(), num_decimal_places=2)
        t12.add_updater(lambda l: l.set_value(t.get_value()))
        t22 = DecimalNumber(t.get_value(), num_decimal_places=2)
        t22.add_updater(lambda l: l.set_value(t.get_value()))

        x_cor_marked = VGroup(
            MathTex(f"x(t)={a_val / scale} \\cdot \\cos(", "2\\pi", "\\cdot").set_color_by_tex("2\\pi", RED),
            t12,
            MathTex(")"),
        ).arrange(RIGHT, buff=0.1).scale(0.7)
        y_cor_marked = VGroup(
            MathTex(f"y(t)={b_val / scale} \\cdot \\sin(", "2\\pi", "\\cdot").set_color_by_tex("2\\pi", RED),
            t22,
            MathTex(")")
        ).arrange(RIGHT, buff=0.1).scale(0.7)
        x_cor_marked.next_to(time, DOWN, buff=0.6)
        y_cor_marked.next_to(x_cor_marked, DOWN)

        self.play(
            Transform(x_cor, x_cor_marked),
            Transform(y_cor, y_cor_marked)
        )
        self.wait(1)

        self.play(
            t.animate.set_value(1 / 7 + 1),
            run_time=5,
            rate_func=linear
        )

