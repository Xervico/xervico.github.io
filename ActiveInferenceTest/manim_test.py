from manim import *
# Increase the frame rate in the config

config.output_file = "Table2Test.mp4"  # Set output file name
config.fps = 60
class CreateTable(Scene):
    def construct(self):
        # Data for the table (converted to strings)
        data = [
            ["0.175", "0.025", "0.025", "0.025"],
            ["0.175", "0.025", "0.025", "0.025"],
            ["0.175", "0.025", "0.025", "0.025"],
            ["0.175", "0.025", "0.025", "0.025"]
        ]

        # Create the table with custom font size and color
        table = Table(
            data,
            include_outer_lines=True,
            element_to_mobject_config={"font_size": 36},  # Set font size for all cells
            
        )
        # Set the colors for each row
        table.set_row_colors(RED, YELLOW, BLUE, GREEN)

        # Animate the creation of the table
        self.play(Create(table), run_time=3) # Slower animation (3 seconds)
        self.wait(5)

from manim import *

class Table2(Scene):
    def construct(self):
        data = [
            ["0.175", "0.025", "0.025", "0.025"],
            ["0.175", "0.025", "0.025", "0.025"],
            ["0.175", "0.025", "0.025", "0.025"],
            ["0.175", "0.025", "0.025", "0.025"]
        ]

        # Create the table without any outer lines
        table = Table(
            data,
            include_outer_lines=False,
            line_config={"stroke_width": 4, "color": WHITE},
            element_to_mobject_config={"font_size": 30, "color": WHITE}
        ).scale(0.8).center()  # Center the table

        # Set row colors
        table.set_row_colors(RED, YELLOW, BLUE, GREEN)  # Specify the colors for each row

        # Animate the fading in of the entire table
        self.play(FadeIn(table), run_time=2)
        self.wait(1)  # Wait for 1 second to show the table

        # Move the table down and to the left by specified amounts
        x = 3  # Movement to the left
        y = 2  # Movement down
        count = 1
        scale_factor = 0.6  # Scale down to 60%
        textTPM = Text("TPM =", font_size=30).shift((DOWN * y) + (LEFT * 6))
        textTime = MathTex(f"t = {count}", font_size=70).shift(UP * 2 + LEFT * 3.5)

        # Update function to increment count and update the text
        def update(mob):
            nonlocal count  # Allows the function to modify the outer variable
            if count < 6:  # Limit to 6 updates
                count += 1  # Increment count
                mob.set_tex(f"t = {count}")  # Update the displayed text

        # Add the updater to the MathTex object
        textTime.add_updater(update)

        # Animate the movement and scaling down
        self.play(
            table.animate.move_to(table.get_center() + DOWN * y + LEFT * x).scale(scale_factor),
            run_time=3  # Animate for 3 seconds
        )
        self.play(Write(textTPM))
        self.wait(1)
        self.play(Write(textTime))
        self.wait(6)  # Keep the scene active to allow updates to happen
        textTime.remove_updater(update)  # Remove the updater after the wait





