from manim import *
import numpy as np


class LinearLaw(Scene):

	def construct(self):
		FSIZE = 40
		self.wait(2)
		# Intro
		intro = Tex("Linear Law", font_size=50).to_edge(UL)
		self.play(Write(intro))
		self.wait(2)

		ex1 = Tex("Example 1:", font_size=FSIZE).to_edge(UL)
		self.play(Transform(intro, ex1))
		self.wait(2)

		loader = VGroup(*[Dot(color=RED_A) for _ in range(4)]).arrange_submobjects().shift(DOWN / 2)

		self.play(Write(loader))
		for i in range(2):
			self.play(loader.animate(run_time=0.7, lag_ratio=0.1).shift(UP))
			self.play(loader.animate(run_time=0.7, lag_ratio=0.1).shift(DOWN))
		self.play(Unwrite(loader))

		qn1 = Tex("Transform the following equation into a linear equation: ", font_size=FSIZE).to_edge(UL).shift(
			DOWN / 2)
		self.play(Write(qn1))
		self.wait(2)

		working = Tex("$y = 3x^2 - x + 23$", font_size=FSIZE)
		self.play(Write(working))
		self.play(working.animate.shift(UP*1.5))
		self.wait(2)

		wk2 = Tex("$y+x = 3x^2 + 23$", font_size=FSIZE)
		self.play(Write(wk2))
		self.play(wk2.animate.shift(UP))
		self.wait(2)

		statement = Tex("$Y = y+x$ and $X = x^2$", font_size=FSIZE)
		self.play(Write(statement))
		self.play(statement.animate.shift(UP/2))
		self.wait(2)

		wk3 = Tex("$Y = 3X + 23$", font_size=FSIZE)
		self.play(Write(wk3))
		self.wait(5)

		self.play(Unwrite(working))
		self.play(Unwrite(wk2))
		self.play(Unwrite(statement))
		self.play(Unwrite(wk3))
		self.wait(2)

		ex2 = Tex("Example 2:", font_size=FSIZE).to_edge(UL)
		self.play(Transform(intro, ex2))
		self.wait(2)

		working = Tex("$y = 5e^{2x}$", font_size=FSIZE)
		self.play(Write(working))
		self.play(working.animate.shift(UP*1.5))
		self.wait(2)

		wk2 = Tex("$ln(y) = ln(5) + 2x$", font_size=FSIZE)
		self.play(Write(wk2))
		self.play(wk2.animate.shift(UP))
		self.wait(2)

		statement = Tex("$Y = ln(y)$ and $X = x$", font_size=FSIZE)
		self.play(Write(statement))
		self.play(statement.animate.shift(UP/2))
		self.wait(2)

		wk3 = Tex("$Y = 2X + ln(5)$", font_size=FSIZE)
		self.play(Write(wk3))
		self.wait(5)

		self.play(Unwrite(working))
		self.play(Unwrite(wk2))
		self.play(Unwrite(statement))
		self.play(Unwrite(wk3))
		self.play(Unwrite(qn1))
		self.play(Unwrite(intro))
		self.wait(2)
# '''


class LagRatios(Scene):
	def construct(self):
		ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

		# Create dot groups
		group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
		groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
		self.add(groups)

		# Label groups
		self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
		for group, ratio in zip(groups, ratios):
			self.add(Text(str(ratio), font_size=36).next_to(group, UP))

		# Animate groups with different lag_ratios
		self.play(AnimationGroup(*[
			group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
			for group, ratio in zip(groups, ratios)
		]))

		# lag_ratio also works recursively on nested submobjects:
		self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))
