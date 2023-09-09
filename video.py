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
        initial_velocity = 3
        animation_length = 5
        distance_axes = Axes(x_range=[0,animation_length,1],y_range=[0,initial_velocity*2-1,1],axis_config={"include_numbers": True},tips=False)
        distance_axes_labels = distance_axes.get_axis_labels(y_label='v[m \cdot s^{-1}]', x_label='t[s]').set_color(WHITE)
        distance_graph = distance_axes.plot(lambda x: initial_velocity, x_range=(0,animation_length))
        distance_graph_run = distance_graph.copy().set_color(RED)
        distance_group = Group(distance_axes,distance_graph,distance_graph_run)
        #distance_group.shift(RIGHT)
        variable_time = Variable(0,"t")
        variable_velocity = Variable(initial_velocity,"v")
        variable_velocity.next_to(variable_time,DOWN)
        variable_distance = Variable(0, "s = v \cdot t")
        variable_distance.next_to(variable_velocity,DOWN)
        ball = Circle(radius=0.5,fill_color=RED,fill_opacity=1) 
        ball.shift(LEFT*5)
        self.add(distance_axes_labels,distance_axes,distance_graph,variable_time,variable_velocity,variable_distance)
        self.play(Create(distance_graph_run),ball.animate().shift(RIGHT*10),variable_time.tracker.animate.set_value(animation_length), variable_distance.tracker.animate.set_value(initial_velocity*animation_length), run_time=animation_length, rate_func=linear)
         
class RZP(Scene):
    def construct(self):
        initial_velocity = 3
        acceleration = 1
        animation_length = 5
        distance_axes = Axes(x_range=[0,animation_length,1],y_range=[0,initial_velocity+acceleration*animation_length,1],axis_config={"include_numbers": True},tips=False)
        distance_axes_labels = distance_axes.get_axis_labels(y_label='v[m \cdot s^{-1}]', x_label='t[s]').set_color(WHITE)
        distance_graph = distance_axes.plot(lambda x: initial_velocity+acceleration*x, x_range=(0,animation_length))
        distance_graph_run = distance_graph.copy().set_color(RED)
        distance_group = Group(distance_axes,distance_graph,distance_graph_run)
        #distance_group.shift(RIGHT)
        variable_time = Variable(0,"t")
        variable_velocity = Variable(initial_velocity,"v_0")
        variable_velocity.next_to(variable_time,DOWN)
        variable_acceleration = Variable(acceleration,"a")
        variable_acceleration.next_to(variable_velocity,DOWN)
        variable_distance = Variable(0, "s = v_0 \cdot t + \dfrac{1}{2} a \cdot t^2")
        variable_distance.next_to(variable_acceleration,DOWN)
        def distance_updater(v):
            time = variable_time.tracker.get_value() 
            v.tracker.set_value(time*initial_velocity+0.5*acceleration*time*time)
        variable_distance.add_updater(distance_updater)
        ball = Circle(radius=0.5,fill_color=RED,fill_opacity=1)
        ball.add_updater(lambda b: b.move_to(LEFT*5+RIGHT*variable_distance.tracker.get_value()*(10/(animation_length*initial_velocity+0.5*acceleration*animation_length**2))))
        self.add(distance_axes_labels,distance_axes,distance_graph,variable_time,variable_velocity,variable_acceleration,variable_distance,ball)
        self.play(Create(distance_graph_run),variable_time.tracker.animate.set_value(animation_length),run_time=animation_length,rate_func=linear)

class Sila(Scene):
    def construct(self):
        box_large = Rectangle(color=RED,fill_color=RED,fill_opacity=1,width=3,height=3).shift(LEFT*5+UP*2)
        box_large_mass = Text("m = 2")
        box_large_mass.add_updater(lambda b: b.move_to(box_large.get_center() + UP*0.5))
        box_large_acceleration = Text("a = 0.5")
        box_large_acceleration.add_updater(lambda b: b.move_to(box_large.get_center() + DOWN*0.5))
        box_small = Rectangle(color=RED,fill_color=RED,fill_opacity=1,width=2,height=2).shift(LEFT*5+DOWN*3)
        box_small_mass = Text("m = 1")
        box_small_mass.add_updater(lambda b: b.move_to(box_small.get_center() + UP*0.5))
        box_small_acceleration = Text("a = 1")
        box_small_acceleration.add_updater(lambda b: b.move_to(box_small.get_center() + DOWN*0.5))
        variable_force = Variable(1,"F").shift(LEFT*5 + DOWN*0.75)
        force_formula = MathTex("F = m \cdot a \Rightarrow a = \dfrac{F}{m}")
        force_formula.shift(RIGHT*3.5 + DOWN*0.75)
        self.add(box_large,box_small,box_large_mass,box_small_mass,variable_force,force_formula,box_large_acceleration,box_small_acceleration)
        self.play(box_large.animate.shift(RIGHT*5),box_small.animate.shift(RIGHT*10),run_time=5,rate_func=rush_into)

class DostredivaSila(Scene):
    def construct(self):
        center = Dot(point=ORIGIN,radius=0.2)
        rotating_body = Circle(color=WHITE,fill_color=WHITE,fill_opacity=1,radius=0.5).shift(UP*3)
        force_arrow = Arrow(start=UP*3,end=UP*1)
        variable_velocity = Variable(1,"v").shift(DOWN)
        variable_force = Variable(0,"F_D = \dfrac{mv^2}{r}").next_to(variable_velocity,DOWN)
        variable_force.add_updater(lambda v: v.tracker.set_value(variable_velocity.tracker.get_value()**2))
        self.add(center,rotating_body,force_arrow,variable_velocity,variable_force)
        self.play(Rotate(rotating_body,angle=2*PI,about_point=ORIGIN),Rotate(force_arrow,angle=2*PI,about_point=ORIGIN),rate_func=linear,run_time=4)
        variable_velocity.tracker.set_value(2)
        force_arrow.put_start_and_end_on(UP*3,ORIGIN)
        self.play(Rotate(rotating_body,angle=2*PI,about_point=ORIGIN),Rotate(force_arrow,angle=2*PI,about_point=ORIGIN),rate_func=linear,run_time=2)

