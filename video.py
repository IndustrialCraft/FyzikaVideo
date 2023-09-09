from manim import *

class Video(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square
    
        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        self.add(ds_m)
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[1, 10], use_smoothing=False)
        area = ax.get_area(graph=graph, x_range=(1,10))
        area.set_fill(BLUE)
        self.add(ax)
        self.play(Create(graph,run_time=5),Write(area,run_time=5))
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
        self.wait()

class RPP(Scene):
    def construct(self):
        initial_speed = 3
        animation_length = 5
        distance_axes = Axes(x_range=[0,animation_length,1],y_range=[0,initial_speed*2-1,1],axis_config={"include_numbers": True},tips=False)
        distance_axes_labels = distance_axes.get_axis_labels(y_label='v[m \cdot s^{-1}]', x_label='t[s]').set_color(WHITE)
        distance_graph = distance_axes.plot(lambda x: initial_speed, x_range=(0,animation_length))
        distance_graph_run = distance_graph.copy().set_color(RED)
        distance_group = Group(distance_axes,distance_graph,distance_graph_run)
        distance_group.shift(RIGHT)
        variable_time = Variable(0,"t")
        variable_velocity = Variable(initial_speed,"v")
        variable_velocity.next_to(variable_time,DOWN)
        variable_distance = Variable(0, "s = v \cdot t")
        variable_distance.next_to(variable_velocity,DOWN)
        ball = Circle(radius=0.5,fill_color=RED,fill_opacity=1) 
        ball.shift(LEFT*5)
        self.add(distance_axes_labels,distance_axes,distance_graph,variable_time,variable_velocity,variable_distance)
        self.play(Create(distance_graph_run),ball.animate().shift(RIGHT*10),variable_time.tracker.animate.set_value(animation_length), variable_distance.tracker.animate.set_value(initial_speed*animation_length), run_time=animation_length, rate_func=linear)
         


