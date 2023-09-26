from manim import *
import math

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
class Trenie(Scene):
    def construct(self):
        angle = Variable(0, r"\alpha").move_to(UP*3)
        friction_coefficient = Variable(0.41, "f").next_to(angle,DOWN)
        force_gravity = Variable(9.81, "F_g").next_to(friction_coefficient,DOWN)
        force_1 = Variable(0, r"F_1 = F_g \cdot sin \: \alpha").move_to(DOWN)
        force_N = Variable(0,r"F_N = F_g \cdot cos \: \alpha").next_to(force_1,DOWN)
        force_T = Variable(0,r"F_t = F_N \cdot f").next_to(force_N,DOWN)
        force_1.add_updater(lambda f: f.tracker.set_value(force_gravity.tracker.get_value()*math.sin(math.radians(angle.tracker.get_value()))))
        force_N.add_updater(lambda f: f.tracker.set_value(force_gravity.tracker.get_value()*math.cos(math.radians(angle.tracker.get_value()))))
        force_T.add_updater(lambda f: f.tracker.set_value(force_N.tracker.get_value() * 0.41390728476))
        plane = Line(start=LEFT,end=RIGHT*3)
        compare_text = MathTex(r"F_1 < F_t").next_to(force_T,DOWN)
        box = Rectangle(width=1,height=1).shift(UP*0.5+RIGHT*2.5)
        self.add(angle,plane,force_gravity,force_1,force_N,force_T,friction_coefficient,box,compare_text)
        self.play(angle.tracker.animate.set_value(45/2),Rotate(plane,angle=PI/8,about_point=LEFT), Rotate(box,angle=PI/8,about_point=LEFT), run_time=5, rate_func=linear)
        self.remove(compare_text)
        compare_text = MathTex(r"F_1 = F_t").next_to(force_T,DOWN)
        self.add(compare_text)
        self.play(box.animate.move_to(LEFT+UP*0.5),run_time=5, rate_func=linear)
