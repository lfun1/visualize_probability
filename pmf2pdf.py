"""
Visualize transformation of a probability mass function (PMF) 
to a probability distribution function (PDF) using manim.
Lisa Fung
12/02/23
"""

# Imports all contents of manim library
from manim import *
import math

class PMF2PDF(Scene):
    """
    Create animation of probability mass function (PMF) transforming
    into a probabiltiy distribution function (PDF).
    """

    # Normal distribution PDF
    def normal_dist(x, sigma=1, mu=0):
        coeff = 1 / (sigma * math.sqrt(2*PI))
        exponent = -1 / 2 * ( (x - mu) / sigma ) ** 2
        return coeff * math.exp(exponent)
    
    def construct(self, pdf_function=normal_dist):
        axes = Axes(x_range = [-5, 6, 1], y_range = [0, 0.5, 0.1], x_length = 11, y_length = 7,
                    axis_config = {"include_tip": True}, x_axis_config = {"numbers_to_include": [0]}).add_coordinates()
        axes.move_to(np.array([0, 0, 0]))
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        # Captions
        normal_pmf_text = Text("Normal PMF")
        normal_pmf_text.to_edge(UL)
        normal_pdf_text = Text("Normal PDF")
        normal_pdf_text.to_edge(UR)

        graph = axes.plot(pdf_function, x_range = [-5, 5], color = YELLOW)
        
        # Generate Riemann rectangles
        riemann_rectangles_dx1 = axes.get_riemann_rectangles(graph, x_range = [-5, 5], dx = 1, input_sample_type = 'center')
        riemann_rectangles_dx01 = axes.get_riemann_rectangles(graph, x_range = [-5, 5], dx = 0.1, input_sample_type = 'center')

        # Set up axes
        self.play(DrawBorderThenFill(axes), Write(axis_labels))

        # Show PMF
        self.play(Write(normal_pmf_text))
        self.play(Create(riemann_rectangles_dx1))
        
        self.wait(1)

        # Transition to thinner rectangles
        self.play(ReplacementTransform(riemann_rectangles_dx1, riemann_rectangles_dx01))

        # Show PDF
        self.play(Create(graph), run_time = 2)
        self.play(Transform(normal_pmf_text, normal_pdf_text))
        self.wait(2)