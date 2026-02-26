from manim import *
import numpy as np

SCALE = 5
SHIFT = LEFT * 2

def circle_points():
    angles = np.linspace(-1 / 12 * np.pi, 7 / 12 * np.pi, 100)
    return np.array([
        [SCALE * np.cos(a), SCALE * np.sin(a), 0] for a in angles
    ])

class CircleIntuitive(Scene):
    def construct(self):
        # === Axes (first quadrant only) ===
        axes = NumberPlane(
            x_range=[-.2, 1.2, 0.5],
            y_range=[-.2, 1.2, 0.5],
            background_line_style={
                "stroke_color": BLUE_A,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).scale(SCALE).shift(SHIFT)

        # === Circle (using points) ===
        circle = VMobject()
        circle.set_points_as_corners(circle_points())
        circle.set_color(YELLOW)
        circle.shift(2.5 * (LEFT + DOWN) + SHIFT)
        self.add(circle)

        # === Point on the circle ===
        t = np.pi/3
        point_coords = np.array([SCALE*np.cos(t), SCALE*np.sin(t), 0]) 
        point = Dot(point_coords, color=YELLOW)
        point.shift(2.5 * (DOWN + LEFT) + SHIFT)

        # === Line to point === 
        hyp = Line(start=ORIGIN, end=point_coords, color=BLUE)
        hyp.shift(2.5 * (DOWN + LEFT) + SHIFT)
        hyp_len = MathTex("1").next_to(hyp, UL, buff=-1.5)

        # === Add all to scene ===
        self.play(
            Create(axes),
            Create(circle),
            Create(point),
            Create(hyp),
            Create(hyp_len)
        )
        self.wait(1)

        # === Label for the point ===
        coord_label = MathTex("(x(t), y(t))").next_to(point, UR, buff=0.1)

        # === Projections ===
        y_proj = DashedLine(start=[point_coords[0], 0, 0], end=point_coords, color=RED)
        y_proj.set_stroke(RED, 6)
        y_proj.shift(2.5 * (DOWN + LEFT) + SHIFT)
        x_proj = DashedLine(start=[0, point_coords[1], 0], end=point_coords, color=GREEN)
        x_proj.set_stroke(GREEN, 6)
        x_proj.shift(2.5 * (DOWN + LEFT) + SHIFT)

        self.play(
            Create(coord_label),
            Create(x_proj),
            Create(y_proj)
        )
        self.wait(1)

        # === Move x_proj ===
        x_proj_moved = DashedLine(start=ORIGIN, end=[point_coords[0], 0, 0], color=GREEN)
        x_proj_moved.set_stroke(GREEN, 6)
        x_proj_moved.shift(2.5 * (DOWN + LEFT) + SHIFT)

        self.play(Transform(x_proj, x_proj_moved))
        self.wait(1)


        # === Label the axis ===
        x_label = MathTex("x(t)").next_to(x_proj, DOWN, buff=0.1)
        y_label = MathTex("y(t)").next_to(y_proj, RIGHT, buff=0.1)

        self.play(Create(x_label), Create(y_label))

        # ==== Label angle ===
        angle = Angle(x_proj_moved, hyp, 1)
        angle_label = MathTex("t").next_to(angle, UR + RIGHT, buff=-0.1)
        self.play(Create(angle), Create(angle_label))
        self.wait(1)

        # === Label the axis with target function ===
        x_label_trig = MathTex("\\cos(t)").next_to(x_proj, DOWN, buff=0.1)

        self.play(Transform(x_label, x_label_trig))
        self.wait(1)

        y_label_trig = MathTex("\\sin(t)").next_to(y_proj, RIGHT, buff=0.1)
        self.play(Transform(y_label, y_label_trig))
        self.wait(1)

        cop_x_label = x_label.copy()
        cop_y_label = y_label.copy()
        cop_hyp_len = hyp_len.copy()
        self.add(cop_x_label, cop_y_label, cop_hyp_len)

        fisrt_part = MathTex("\\cos^2(t)").next_to(axes, RIGHT, buff=0.5)
        self.play(Transform(cop_x_label, fisrt_part))
        self.wait(1)

        plus = MathTex("+").next_to(fisrt_part, RIGHT, buff=0.3)
        second_part = MathTex("\\sin^2(t)").next_to(plus, RIGHT, buff=0.3)
        self.play(Create(plus), Transform(cop_y_label, second_part))
        self.wait(1)

        equal = MathTex("=").next_to(second_part, RIGHT, buff=0.3)
        third_part = MathTex("1").next_to(equal, RIGHT, buff=0.3)
        self.play(Create(equal), Transform(cop_hyp_len, third_part))

        

