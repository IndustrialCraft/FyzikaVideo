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
        variable_time.value.unit = r"s"
        area_group = Group()
        def area_under_curve_updater(p):
            if len(p) > 0:
                p.remove(p[0])
            area = distance_axes.get_area(graph=distance_graph,x_range=(0,variable_time.tracker.get_value()),color=[YELLOW,YELLOW])
            p.add(area)
        area_group.add_updater(area_under_curve_updater)
        variable_velocity = Variable(initial_velocity,"v",num_decimal_places=0)
        variable_velocity.value.unit = r"m \cdot s^{-1}"
        variable_velocity.next_to(variable_time,DOWN)
        variable_distance = Variable(0, "s = v \cdot t")
        variable_distance.value.unit = r"m"
        variable_distance.color = YELLOW
        variable_distance.next_to(variable_velocity,DOWN)
        ball = Circle(radius=0.5,fill_color=RED,fill_opacity=1) 
        ball.shift(LEFT*5+UP*1.5)
        self.add(area_group,distance_axes_labels,distance_axes,distance_graph,variable_time,variable_velocity,variable_distance)
        self.play(Create(distance_graph_run),ball.animate().shift(RIGHT*10),variable_time.tracker.animate.set_value(animation_length), variable_distance.tracker.animate.set_value(initial_velocity*animation_length), run_time=animation_length, rate_func=linear)
         
class RZP(Scene):
    def construct(self):
        initial_velocity = 3
        acceleration = 2.5
        animation_length = 5
        distance_axes = Axes(x_range=[0,animation_length,1],y_range=[0,initial_velocity+acceleration*animation_length,1],axis_config={"include_numbers": True},tips=False)
        distance_axes_labels = distance_axes.get_axis_labels(y_label='v[m \cdot s^{-1}]', x_label='t[s]').set_color(WHITE)
        distance_graph = distance_axes.plot(lambda x: initial_velocity+acceleration*x, x_range=(0,animation_length))
        distance_graph_run = distance_graph.copy().set_color(RED)
        distance_group = Group(distance_axes,distance_graph,distance_graph_run)
        #distance_group.shift(RIGHT)
        variable_time = Variable(0,"t")
        variable_time.value.unit = r"s"
        variable_velocity = Variable(initial_velocity,"v_0",num_decimal_places=0)
        variable_velocity.value.unit = r"m \cdot s^{-1}"
        variable_velocity.next_to(variable_time,DOWN)
        variable_acceleration = Variable(acceleration,"a",num_decimal_places=1)
        variable_acceleration.value.unit = r"m \cdot s^{-2}"
        variable_acceleration.next_to(variable_velocity,DOWN)
        variable_distance = Variable(0, "s = v_0 \cdot t + \dfrac{1}{2} a \cdot t^2")
        variable_distance.value.unit = r"m"
        variable_distance.color = YELLOW
        variable_distance.next_to(variable_acceleration,DOWN)
        area_group = Group()
        def area_under_curve_updater(p):
            if len(p) > 0:
                p.remove(p[0])
            area = distance_axes.get_area(graph=distance_graph,x_range=(0,variable_time.tracker.get_value()),color=[YELLOW,YELLOW])
            p.add(area)
        area_group.add_updater(area_under_curve_updater)
        def distance_updater(v):
            time = variable_time.tracker.get_value() 
            v.tracker.set_value(time*initial_velocity+0.5*acceleration*time*time)
        variable_distance.add_updater(distance_updater)
        ball = Circle(radius=0.5,fill_color=RED,fill_opacity=1)
        ball.add_updater(lambda b: b.move_to(UP*1.5+LEFT*5+RIGHT*variable_distance.tracker.get_value()*(10/(animation_length*initial_velocity+0.5*acceleration*animation_length**2))))
        self.add(area_group,distance_axes_labels,distance_axes,distance_graph,variable_time,variable_velocity,variable_acceleration,variable_distance,ball)
        self.play(Create(distance_graph_run),variable_time.tracker.animate.set_value(animation_length),run_time=animation_length,rate_func=linear)
class Sila(Scene):
    def construct(self):
        box_large = Rectangle(color=RED,fill_color=RED,fill_opacity=1,width=3.5,height=3.5).shift(LEFT*5+UP*2)
        box_large_arrow = Arrow()
        box_large_arrow.add_updater(lambda a:a.put_start_and_end_on(box_large.get_center(),box_large.get_center()+RIGHT*3))
        box_large_mass = MathTex("m = 2kg")
        box_large_mass.add_updater(lambda b: b.move_to(box_large.get_center() + UP*0.5))
        box_large_acceleration = MathTex("a = 0.5m \cdot s^{-2}")
        box_large_acceleration.add_updater(lambda b: b.move_to(box_large.get_center() + DOWN*0.5))
        box_small = Rectangle(color=RED,fill_color=RED,fill_opacity=1,width=3,height=2.5).shift(LEFT*5+DOWN*3)
        box_small_arrow = Arrow()
        box_small_arrow.add_updater(lambda a:a.put_start_and_end_on(box_small.get_center(),box_small.get_center()+RIGHT*3))
        box_small_mass = MathTex("m = 1kg")
        box_small_mass.add_updater(lambda b: b.move_to(box_small.get_center() + UP*0.5))
        box_small_acceleration = MathTex("a = 1m \cdot s^{-2}")
        box_small_acceleration.add_updater(lambda b: b.move_to(box_small.get_center() + DOWN*0.5))
        variable_force = Variable(1,"F",num_decimal_places=0).shift(LEFT*5 + DOWN*0.75)
        variable_force.value.unit = r"N"
        force_formula = MathTex("F = m \cdot a \Rightarrow a = \dfrac{F}{m}")
        force_formula.shift(RIGHT*3.5 + DOWN*0.75)
        self.add(box_large,box_large_arrow,box_small,box_small_arrow,box_large_mass,box_small_mass,variable_force,force_formula,box_large_acceleration,box_small_acceleration)
        self.play(box_large.animate.shift(RIGHT*5),box_small.animate.shift(RIGHT*10),run_time=5,rate_func=rush_into)

class DostredivaSila(Scene):
    def construct(self):
        center = Dot(point=ORIGIN,radius=0.2)
        rotating_body = Circle(color=RED,fill_color=RED,fill_opacity=1,radius=0.5).shift(UP*3)
        force_arrow = Arrow(start=UP*2.75,end=UP*1.5)
        rope = Line(color=YELLOW,stroke_width=2)
        rope.add_updater(lambda r:r.put_start_and_end_on(ORIGIN,rotating_body.get_center()))
        variable_mass = Variable(1,"m",num_decimal_places=0).shift(DOWN)
        variable_mass.value.unit = r"kg"
        variable_velocity = Variable(1,"v",num_decimal_places=0).next_to(variable_mass,DOWN)
        variable_velocity.value.unit = r"m \cdot s^{-1}"
        variable_radius = Variable(1,"r",num_decimal_places=0).next_to(variable_velocity,DOWN)
        variable_radius.value.unit = r"m"
        variable_force = Variable(0,"F_D = \dfrac{mv^2}{r}").next_to(variable_radius,DOWN)
        variable_force.value.unit = r"N"
        variable_force.add_updater(lambda v: v.tracker.set_value(variable_velocity.tracker.get_value()**2))
        self.add(rope,center,rotating_body,force_arrow,variable_mass,variable_velocity,variable_radius,variable_force)
        self.play(Rotate(rotating_body,angle=2*PI,about_point=ORIGIN),Rotate(force_arrow,angle=2*PI,about_point=ORIGIN),rate_func=linear,run_time=4)
        variable_velocity.tracker.set_value(2)
        force_arrow.put_start_and_end_on(UP*2.75,UP*0.5)
        self.play(Rotate(rotating_body,angle=2*PI,about_point=ORIGIN),Rotate(force_arrow,angle=2*PI,about_point=ORIGIN),rate_func=linear,run_time=2)
class Trenie(Scene):
    def construct(self):
        angle = Variable(0, r"\alpha").move_to(UP*3.5)
        angle.value.unit = r"^\circ"
        friction_coefficient = Variable(0.41, "f").next_to(angle,DOWN)
        force_gravity = Variable(9.81, "F_g").next_to(friction_coefficient,DOWN)
        force_gravity.value.unit = "N"
        force_gravity.color = RED
        force_gravity_arrow = Arrow(color=RED)
        force_1 = Variable(0, r"F_1 = F_g \cdot sin \: \alpha").move_to(DOWN)
        force_1.color = GREEN
        force_1.value.unit = "N"
        force_1_arrow = Arrow(color=GREEN)
        force_N = Variable(0,r"F_N = F_g \cdot cos \: \alpha").next_to(force_1,DOWN)
        force_N.value.unit = "N"
        force_N.color = BLUE
        force_N_arrow = Arrow(color=BLUE)
        force_T = Variable(0,r"F_t = F_N \cdot f").next_to(force_N,DOWN)
        force_T.value.unit = "N"
        force_T.color = YELLOW
        force_T_arrow = Arrow(color=YELLOW)
        force_1.add_updater(lambda f: f.tracker.set_value(force_gravity.tracker.get_value()*math.sin(math.radians(angle.tracker.get_value()))))
        force_N.add_updater(lambda f: f.tracker.set_value(force_gravity.tracker.get_value()*math.cos(math.radians(angle.tracker.get_value()))))
        force_T.add_updater(lambda f: f.tracker.set_value(force_N.tracker.get_value() * 0.41390728476))
        plane = Line(start=LEFT,end=RIGHT*3)
        compare_text = MathTex(r"F_1 < F_t").next_to(force_T,DOWN)
        box = Rectangle(width=1,height=1).shift(UP*0.5+RIGHT*2.5)
        force_gravity_arrow.add_updater(lambda a:a.put_start_and_end_on(box.get_center(),box.get_center()+DOWN*(9.81/5)))
        force_1_arrow.add_updater(lambda a:a.put_start_and_end_on(box.get_center(),box.get_center()+(DOWN*math.sin(math.radians(angle.tracker.get_value()))+LEFT*math.cos(math.radians(angle.tracker.get_value())))*(force_1.tracker.get_value()/5+0.4)))
        force_N_arrow.add_updater(lambda a:a.put_start_and_end_on(box.get_center(),box.get_center()+(DOWN*math.cos(math.radians(angle.tracker.get_value()))+RIGHT*math.sin(math.radians(angle.tracker.get_value())))*(force_N.tracker.get_value()/5)))
        force_T_arrow.add_updater(lambda a:a.put_start_and_end_on(box.get_center()+DOWN*0.5*math.cos(math.radians(angle.tracker.get_value()))+RIGHT*0.5*math.sin(math.radians(angle.tracker.get_value())),box.get_center()+DOWN*0.5*math.cos(math.radians(angle.tracker.get_value()))+RIGHT*0.5*math.sin(math.radians(angle.tracker.get_value()))+(UP*math.sin(math.radians(angle.tracker.get_value()))+RIGHT*math.cos(math.radians(angle.tracker.get_value())))*(force_T.tracker.get_value()/5+0.4)))
        self.add(angle,plane,force_gravity,force_1,force_N,force_T,friction_coefficient,box,compare_text,force_T_arrow,force_gravity_arrow,force_1_arrow,force_N_arrow)
        self.play(angle.tracker.animate.set_value(45/2),Rotate(plane,angle=PI/8,about_point=LEFT), Rotate(box,angle=PI/8,about_point=LEFT), run_time=5, rate_func=linear)
        self.remove(compare_text)
        compare_text = MathTex(r"F_1 = F_t").next_to(force_T,DOWN)
        self.add(compare_text)
        self.play(box.animate.move_to(LEFT+UP*0.5),run_time=5, rate_func=rush_into)
class Energia(Scene):
    def construct(self):
        pendulum = Circle(radius=0.5,fill_color=RED,fill_opacity=1).shift(UP*2)
        line = Line(start=UP*4,end=ORIGIN)
        pendulum.rotate(angle=PI/3,about_point=UP*4)
        line.add_updater(lambda l:line.put_start_and_end_on(UP*4,pendulum.get_center()))
        mass = Variable(1,"m",num_decimal_places=0).shift(UP*1.5)
        mass.value.unit = "kg"
        acceleration_gravity = Variable(9.81,"g").next_to(mass,DOWN)
        acceleration_gravity.value.unit = "m \cdot s^{-2}"
        height = Variable(0,"h").next_to(acceleration_gravity,DOWN)
        height.value.unit = "m"
        height.add_updater(lambda h:h.tracker.set_value(pendulum.get_center()[1]-2))
        velocity = Variable(0,"v").next_to(height,DOWN)
        velocity.value.unit = "m \cdot s^{-1}"
        energy_potential = Variable(9.81,"E_p = m \cdot g \cdot h").next_to(velocity,DOWN)
        energy_potential.value.unit = "J"
        energy_potential.add_updater(lambda e:e.tracker.set_value(height.tracker.get_value()*9.81))
        energy_kinetic = Variable(0,"E_k = \dfrac{1}{2}mv^2").next_to(energy_potential,DOWN)
        energy_kinetic.value.unit = "J"
        energy_kinetic.add_updater(lambda e:e.tracker.set_value((1-height.tracker.get_value())*9.81))
        velocity.add_updater(lambda v:v.tracker.set_value(math.sqrt(energy_kinetic.tracker.get_value()*2)))
        energy = Variable(9.81,"E = E_p + E_k").next_to(energy_kinetic,DOWN)
        energy.value.unit = "J"
        self.add(pendulum,line,mass,mass,acceleration_gravity,height,energy_potential,energy_kinetic,energy,velocity)
        for _ in range(0,2):
            self.play(Rotate(pendulum,angle=-PI/3*2,about_point=UP*4),run_time=2.5,rate_func=smooth)
            self.play(Rotate(pendulum,angle=PI/3*2,about_point=UP*4),run_time=2.5,rate_func=smooth)
class Hybnost(Scene):
    def construct(self):
        first_cart = self.create_cart("1",1)
        second_cart = self.create_cart("2",2)

        velocity_1 = Variable(1,"v_1").shift(UP+LEFT*1)
        velocity_1.value.unit = "m \cdot s^{-1}"
        first_cart += velocity_1
        velocity_2 = Variable(0,"v_2").shift(UP+LEFT*1)
        velocity_2.value.unit = "m \cdot s^{-1}"
        second_cart += velocity_2
        momentum_total = Variable(1,"p=p_1+p_2").shift(UP*1)
        momentum_total.value.unit = "kg \cdot m \cdot s^{-1}"
        momentum_1 = Variable(1,"p_1=m_1 \cdot v_1").next_to(momentum_total,DOWN)
        momentum_1.value.unit = "kg \cdot m \cdot s^{-1}"
        momentum_2 = Variable(0,"p_2=m_2 \cdot v_2").next_to(momentum_1,DOWN)
        momentum_2.value.unit = "kg \cdot m \cdot s^{-1}"

        first_cart.shift(DOWN*3+LEFT*5)
        second_cart.shift(DOWN*3)

        self.add(first_cart,second_cart,momentum_total,momentum_1,momentum_2)
        self.play(first_cart.animate.shift(RIGHT*3),run_time=2.5,rate_func=linear)
        momentum_1.tracker.set_value(0)
        momentum_2.tracker.set_value(1)
        velocity_1.tracker.set_value(0)
        velocity_2.tracker.set_value(0.5)
        self.play(second_cart.animate.shift(RIGHT*3),run_time=5,rate_func=linear)
    def create_cart(self,name,weight):
        group = VGroup()
        group += Rectangle(width=2,height=1)
        group += MathTex("m_"+name+"="+str(weight)+"kg")
        group += Circle(radius=0.2,color=WHITE).shift(DOWN*0.7+LEFT*0.8)
        group += Circle(radius=0.2,color=WHITE).shift(DOWN*0.7+RIGHT*0.8)
        return group
class ElektrickePole(Scene):
    def construct(self):
        charges = []
        for x in range(0,14):
            for y in range(0,8):
                arrow = Arrow(start=LEFT*(x-7)+UP*(y-4),end=LEFT*(x-7)+UP*(y-4)+UP*4,max_tip_length_to_length_ratio=0.05)
                def arrow_updater(a):
                    vector = np.copy(ORIGIN)
                    for charge in charges:
                        diff = charge[0].get_center()-a.get_start() 
                        vector += normalize(diff)*1000/np.linalg.norm(diff)*charge[1]
                        #print(str(len(charges)) + "-" + str(charge[0].get_center()) + " - " + str(vector))
                    a.put_start_and_end_on(a.get_start()+DOWN*0.0001,a.get_start() + normalize(vector)*0.5+UP*0.001)
                arrow.add_updater(arrow_updater)
                self.add(arrow)
        charge_negative = Dot(color=BLUE,radius = 0.2)
        charges.append((charge_negative,1))
        self.add(charge_negative)
        self.play(charge_negative.animate.shift(LEFT*3),run_time=5)
        charge_positive = Dot(color=BLUE,radius = 0.2)
        charges.append((charge_positive,1))
        self.add(charge_positive)
        self.play(charge_positive.animate.shift(RIGHT*3),run_time=5)
        charge_positive.color = RED
        charges[1] = (charges[1][0],-1)
        self.play(charge_positive.animate.shift(LEFT*3),run_time=5)
