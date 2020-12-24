from manimlib.imports import *
import os
import pyclbr

class FL2(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        base1 = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}"
        )
        VGroup(title, base1).arrange(DOWN)

        self.play(
        Write(title),
        FadeInFrom(base1, UP)
        )
        self.wait(2)
