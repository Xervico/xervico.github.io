def construct(self):
    line = Line(LEFT, RIGHT)
    theta_1_val = MathTex('\\theta=' + str(round(line.get_angle(), 3))).move_to(1.5 * DOWN)
    print(line.get_angle())

    def update(mob):
        mob.become(MathTex('\\theta=' + str(round(line.get_angle(), 3))).move_to(1.5*DOWN))

    theta_1_val.add_updater(update)
    self.play(FadeIn(line))
    self.add(line)
    self.play(FadeIn(theta_1_val))
    self.add(theta_1_val)
    self.play(Rotate(line, angle=round(2*PI, 13), run_time=5, rate_func=rate_functions.ease_in_out_quad))
    self.wait()