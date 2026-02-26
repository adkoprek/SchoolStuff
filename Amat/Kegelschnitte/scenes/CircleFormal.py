from manim import *
import numpy as np

from manim import *

class CircleFormal(Scene):
    def construct(self):
        ################## Title #########################
        title = Title("Parametrisierung")
        self.play(Write(title))
        self.wait(0.3)

        ################## Question #########################
        eq1 = MathTex("x(t) = \\, ?", color=WHITE)
        eq2 = MathTex("y(t) = \\, ?").next_to(eq1, DOWN, aligned_edge=LEFT)
        question_group = VGroup(eq1, eq2).scale(1.2).to_edge(UP, buff=3)

        self.play(Write(eq1), Write(eq2))
        self.wait(0.5)

        ################## Answer #########################
        eq1_solv = MathTex("x(t) = \\cos(t)", color=WHITE)
        eq2_solv = MathTex("y(t) = \\sin(t)", color=WHITE).next_to(eq1_solv, DOWN, aligned_edge=LEFT)
        answer_group = VGroup(eq1_solv, eq2_solv).move_to(question_group)

        # Add color highlights for x and y
        eq1_solv[0][0].set_color(BLUE)
        eq2_solv[0][0].set_color(RED)

        self.play(Transform(eq1, eq1_solv), Transform(eq2, eq2_solv))
        self.wait(0.5)

        ################## Proof #########################
        eq3 = MathTex("x^2", "+" "y^2", "=1")
        eq3.next_to(eq2_solv, DOWN, buff=0.8)

        eq3_solv = MathTex("\\cos^2 t", "+", "\\sin^2 t",  "= 1")
        eq3_solv.next_to(eq2_solv, DOWN, buff=0.8)

        eq3_solv2 = MathTex("1 = 1")
        eq3_solv2.next_to(eq2_solv, DOWN, buff=0.8)

        # Color the variables in all steps
        eq3.set_color_by_tex("x", BLUE)
        eq3.set_color_by_tex("y", RED)
        eq3_solv.set_color_by_tex("\\cos", BLUE)
        eq3_solv.set_color_by_tex("\\sin", RED)

        # Animate proof nicely spaced
        self.play(FadeIn(eq3, shift=UP))
        self.wait(0.5)
        self.play(ReplacementTransform(eq3, eq3_solv))
        self.wait(0.5)
        self.play(ReplacementTransform(eq3_solv, eq3_solv2))
        self.wait(0.8)

        ################## Finishing Touch #########################
        box = SurroundingRectangle(VGroup(eq1_solv, eq2_solv), color=YELLOW, buff=0.4)
        self.play(Create(box))
        self.wait(1.5)

        self.play(FadeOut(box), FadeOut(eq1), FadeOut(eq2), FadeOut(eq3_solv2), FadeOut(title))
        self.wait(0.5)

