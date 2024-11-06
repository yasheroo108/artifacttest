import streamlit as st
import math

#add that is answer is negative its impossible

st.title("Reverse Functions")

mode = st.selectbox("Which 3D shape's variable would you like to calculate", ("Prism", "Pyramid", "Cylinder", "Cone", "Sphere"))
st.markdown("`Made by Yash, Powered by Streamlit`") 
st.markdown("""<a href="https://testytester.streamlit.app/">Surface Area and Volume</a>""", unsafe_allow_html=True)

if mode == "Prism":
    base = st.number_input("How many sides does your prism's base have?", min_value=3)
    
    if base == 3:
        st.latex(r"V = \frac{lw}{2}*H")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, H = prism height</p>""", unsafe_allow_html=True)
        var = st.selectbox("Which variable would you like to calculate?", ("Length", "Width", "Prism Height"))

        if var == "Length":
            st.latex(r"l = \frac{\frac{V}{h}}{w}*2")
            w = st.number_input("What is the base's width?", min_value=0.01)
            h = st.number_input("What is the prism's height?", min_value=0.01)
            v = st.number_input("What is the prism's volume?", min_value=0.01)
            answer = ((v/h)/w)*2
            st.write("The length of the base is ", answer, "units.")

        if var == "Width":
            st.latex(r"l = \frac{\frac{V}{h}}{w}*2")
            l = st.number_input("What is the base's length?", min_value=0.01)
            h = st.number_input("What is the prism's height?", min_value=0.01)
            v = st.number_input("What is the prism's volume?", min_value=0.01)
            answer = ((v/h)/l)*2
            st.write("The width of the base is ", answer, "units.")

        if var == "Prism Height":
            st.latex(r"l = \frac{\frac{V}{l}}{w}*2")
            w = st.number_input("What is the base's width?", min_value=0.01)
            l = st.number_input("What is the base length?", min_value=0.01)
            v = st.number_input("What is the prism's volume?", min_value=0.01)
            answer = ((v/l)/w)*2
            st.write("The height of the prism is ", answer, "units.")

    if base == 4: 
        fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))

        if fourmode == "Common":
            st.latex(r"V = lwh")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = length, w = width, h = prism height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Length", "Width", "Prism Height"))
            if var == "Length":
                st.latex(r"l = \frac{\frac{V}{w}}{h}")
                w = st.number_input("What is the width of the base?", min_value=0.01)
                h = st.number_input("What is the height of the prism?", min_value=0.01)
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                answer = (v/w)/h
                st.write("The length is ", answer, " units.")

            if var == "Width":
                st.latex(r"w = \frac{\frac{V}{l}}{h}")
                l = st.number_input("What is the length of the base?", min_value=0.01)
                h = st.number_input("What is the height of the prism?", min_value=0.01)
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                answer = (v/l)/h
                st.write("The width is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"h = \frac{\frac{V}{l}}{w}")
                l = st.number_input("What is the length of the base?", min_value=0.01)
                w = st.number_input("What is the width of the base?", min_value=0.01)
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                answer = (v/l)/w
                st.write("The height is ", answer, " units.")

        if fourmode == "Trapezoid":
            st.latex(r"V = \frac{h(a+b)}{2}*H")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = base height, a = top side, b = bottom side, H = prism height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("a", "b", "Base Height", "Prism Height"))

            if var == "a":
                st.latex(r"a = \frac{\frac{2V}{H}}{h}-b")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                bh = st.number_input("What is the height of the base?", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                b = st.number_input("What is b (top or bottom side of base)?", min_value=0.01)
                answer = (((2*v)/ph)/bh)-b
                st.write("a is ", answer, " units.")

            if var == "b":
                st.latex(r"b = \frac{\frac{2V}{H}}{h}-a")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                bh = st.number_input("What is the height of the base?", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                a = st.number_input("What is a (top or bottom side of base)?", min_value=0.01)
                answer = (((2*v)/ph)/bh)-a
                st.write("a is ", answer, " units.")

            if var == "Base Height":
                st.latex(r"h = \frac{\frac{2V}{H}}{a+b}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                ph = st.number_input("What is the prism's height?", min_value=0.01)
                a = st.number_input("What is a (top or bottom side of base)?", min_value=0.01)
                b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                answer = ((2*v)/ph)/(a+b)
                st.write("The base height is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"H = \frac{2V}{h(a+b)}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                bh = st.number_input("What is the base height?", min_value=0.01)
                a = st.number_input("What is a (top or bottom side)?", min_value=0.01)
                b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                answer = (2*v)/(bh*(a+b))
                st.write("The prism height is ", answer, " units")

    if base > 4:
        st.warning("Prisms with bases with more than 5 sides will only calculate shapes with regular bases.")
        st.latex(r"V = \frac{AP}{2}*h")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, h = prism height</p>""", unsafe_allow_html=True)
        var = st.selectbox("Which variable would you like to calculate?", ("Apothem", "Perimeter", "Prism Height"))

        if var == "Apothem":
            st.latex(r"A = \frac{\frac{P}{x}}{2tan(\frac{180}{x})}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
            p = st.number_input("What is the perimieter of the base?", min_value=0.01)
            answer = (p/base)/(2*math.tan(math.radians(180/base)))
            st.write("The apothem is ", answer, " units.")

        if var == "Perimeter":
            st.latex(r"P = Ax(2tan(\frac{180}{x}))")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
            a = st.number_input("What is the apothem of the base?", min_value=0.01)
            answer = a*(2*math.tan(math.radians(180/base)))*base
            st.write("The perimieter is ", answer, " units.")

        if var == "Prism Height":
            st.latex(r"h = \frac{2V}{AP}")
            v = st.number_input("What is the volume of the prism?", min_value=0.01)
            e = st.number_input("What is the edge length of the base?", min_value=0.01)
            answer = (2*v) / ((e / (2*math.tan(math.radians(180 / base)))) * e*base)
            st.write("The prism height is ", answer, " units.")

if mode == "Pyramid":
    base = st.number_input("How many sides does your pyramid's base have?", min_value=3)

    if base == 3:
        st.latex(r"V = \frac{\frac{lw}{2}*h}{3}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = pyramid height</p>""", unsafe_allow_html=True)
        var = st.selectbox("Which variable would you like to calculate?", ("Base Length", "Base Width", "Pyramid Height"))

        if var == "Base Length":
            st.latex(r"l = \frac{6V}{wh}")
            v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
            w = st.number_input("What is the width of the base?", min_value=0.01)
            h = st.number_input("What is the height of the pyramid?", min_value=0.01)
            answer = (6*v)/(w*h)
            st.write("The base's length is ", answer, " units.")

        if var == "Base Width":
            st.latex(r"w = \frac{6V}{lh}")
            v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
            l = st.number_input("What is the length of the base?", min_value=0.01)
            h = st.number_input("What is the height of the pyramid?", min_value=0.01)
            answer = (6*v)/(l*h)
            st.write("The base's width is ", answer, " units.")

        if var == "Pyramid Height":
            st.latex(r"h = \frac{6V}{lw}")
            v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
            l = st.number_input("What is the length of the base?", min_value=0.01)
            w = st.number_input("What is the width of the base?", min_value=0.01)
            answer = (6*v)/(l*w)
            st.write("The pyramid's height is ", answer, " units.")

    if base == 4:
        fourmode = st.selectbox("Do you have a pyramid with a common base or a trapezoid base?", ("Common", "Trapezoid"))

        if fourmode == "Common":
            st.latex(r"V = \frac{lwh}{3}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = base height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Base Length", "Base Width", "Pyramid Height"))
            if var == "Base Length":
                st.latex(r"l = \frac{3V}{hw}")
                v = st.number_input("What is the volume of your pyramid?", min_value=0.01)
                bw = st.number_input("What is the base width?", min_value=0.01)
                ph = st.number_input("What is the prism height?", min_value=0.01)
                answer = (3*v)/(ph*bw)
                st.write("The length is ", answer, " units.")

            if var == "Base Width":
                st.latex(r"w = \frac{3V}{lh}")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                l = st.number_input("What is the length of the base?", min_value=0.01)
                h = st.number_input("What is the height of the prism?", min_value=0.01)
                answer = (3*v)/(l*h)
                st.write("The width of the base is ", answer, " units.")

            if var == "Pyramid Height":
                st.latex(r"h = \frac{3V}{lw}")
                v = st.number_input("What is the volume?", min_value=0.01)
                l = st.number_input("What is the length of the base?", min_value=0.01)
                w = st.number_input("What is the width of the base?", min_value=0.01)
                answer = (3*v)/(l*w)
                st.write("The pyramid height is ", answer, " units.")
        
        if fourmode == "Trapezoid":
            st.latex(r"\frac{h(a+b)*H}{6}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = base height, a = base top side, b = base bottom side, H = prism height</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Base Height", "a", "b", "Prism Height"))
            if var == "Base Height":
                st.latex(r"h = \frac{6V}{H(a+b)}")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                ph = st.number_input("What is the pyramid height?", min_value=0.01)
                a = st.number_input("What is a of the base (The top of bottoms side of the trapezoid)?", min_value=0.01)
                b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                answer = (6*v)/(ph*(a+b))
                st.write("The base height is ", answer, " units.")

            if var == "a":
                st.latex(r"a = \frac{6V}{Hh}-b")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                ph = st.number_input("What is the height of the pyramid?", min_value=0.01)
                bh = st.number_input("What is the height of the base?", min_value=0.01)
                b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                answer = ((6*v)/(ph*bh))-b
                st.write("a is", answer, "units.")

            if var == "b":
                st.latex(r"a = \frac{6V}{Hh}-b")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                ph = st.number_input("What is the height of the pyramid?", min_value=0.01)
                bh = st.number_input("What is the height of the base?", min_value=0.01)
                a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                answer = ((6*v)/(ph*bh))-a
                st.write("b is", answer, "units.")
            
            if var == "Prism Height":
                st.latex(r"H = \frac{6V}{h(a+b)}")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                bh = st.number_input("What is the base pyramid?", min_value=0.01)
                a = st.number_input("What is a of the base (The top of bottoms side of the trapezoid)?", min_value=0.01)
                b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                answer = (6*v)/(bh*(a+b))
                st.write("The pyramid height is ", answer, " units.")

    if base > 4:
        st.warning("Pyramids with bases with more than 5 sides will only calculate shapes with regular bases.")
        st.latex(r"V = \frac{\frac{AP}{2}*h}{3}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, h = pyramid height</p>""", unsafe_allow_html=True)
        var = st.selectbox("Which variable would you like to calculate?", ("Apothem", "Perimeter", "Pyramid Height"))

        if var == "Apothem":
            st.latex(r"A = \frac{\frac{P}{x}}{2tan(\frac{180}{x})}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
            p = st.number_input("What is the perimieter of the base?", min_value=0.01)
            answer = (p/base)/(2*math.tan(math.radians(180/base)))
            st.write("The apothem is ", answer, " units.")

        if var == "Perimeter":
            st.latex(r"P = Ax(2tan(\frac{180}{x}))")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
            a = st.number_input("What is the apothem of the base?", min_value=0.01)
            answer = a*(2*math.tan(math.radians(180/base)))*base
            st.write("The perimieter is ", answer, " units.")

        if var == "Pyramid Height":
            st.latex(r"h = \frac{6V}{AP}")
            v = st.number_input("What is the volume of the prism?", min_value=0.01)
            e = st.number_input("What is the side length of the base?", min_value=0.01)
            answer = (6*v)/((e / (2 * math.tan(math.radians(180 / base))))*(e*base))
            st.write("The pyramid height is ", answer, "units.")

if mode == "Cylinder":
    circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

    if circlemode == "Radius":
        st.latex(r"V = r^2πh")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = height</p>""", unsafe_allow_html=True)
        var = st.selectbox("What variable would you like to calculate?", ("Radius", "Cylinder Height"))

        if var == "Radius":
            st.latex(r"r = \sqrt{\frac{V}{πh}}")
            v = st.number_input("What is the volume of the cylinder?", min_value=0.01)
            h = st.number_input("What is the height of the cylinder?", min_value=0.01)
            answer = math.sqrt(v/(math.pi*h))
            st.write("The radius is ", answer, " units.")

        if var == "Cylinder Height":
            st.latex(r"h = \frac{V}{πr²}")
            v = st.number_input("What is the volume of the prism?", min_value=0.01)
            r = st.number_input("What is the radius?", min_value=0.01)
            answer = v/(math.pi*r**2)
            st.write("The cylinder height is ", answer, " units.")

    if circlemode == "Diameter":
        st.latex(r"V = (\frac{d}{2})^2πh")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = height</p>""", unsafe_allow_html=True)
        var = st.selectbox("What is the variable you'd like to calculate?", ("Diameter", "Prism Height"))

        if var == "Diameter":
            st.latex(r"d = 2\sqrt{\frac{V}{πh}}")
            v = st.number_input("What is the volume of the prism?", min_value=0.01)
            h = st.number_input("What is the height of the prism?", min_value=0.01)
            answer = 2*(math.sqrt((v/(math.pi*h))))
            st.write("The diameter is ", answer, " units.")

        if var == "Prism Height":
            st.latex(r"h = \frac{V}{π(\frac{d}{2})²}")
            v = st.number_input("What is the volume of the prism?", min_value=0.01)
            d = st.number_input("What is the diameter of the base?", min_value=0.01)
            answer = v/(math.pi*((d/2)**2))
            st.write("The cylinder height is ", answer, " units.")

if mode == "Cone":
    circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

    if circlemode == "Radius":
        st.latex(r"V = \frac{r^2πh}{3}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = height</p>""", unsafe_allow_html=True)
        var = st.selectbox("Which variable would you like to calculate?", ("Radius", "Height"))
        if var == "Radius":
            st.latex(r"r = \sqrt{\frac{3V}{πh}}")
            v = st.number_input("What is the volume of the cone?", min_value=0.01)
            h = st.number_input("What is the height of the cone?", min_value=0.01)
            answer = math.sqrt((3*v)/(math.pi*h))
            st.write("The radius is ", answer, " units.")

        if var == "Height":
            st.latex(r"\frac{3V}{πr²}")
            v = st.number_input("What is the volume of the cone?", min_value=0.01)
            r = st.number_input("What is the radius of the cone?", min_value=0.01)
            answer = (3*v)/(math.pi*r**2)
            st.write("The height is ", answer, " units.")

    if circlemode == "Diameter":
        st.latex(r"V = \frac{(\frac{d}{2})^2πh}{3}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = height</p>""", unsafe_allow_html=True)
        var = st.selectbox("Which variable would you like to calculate?", ("Diameter", "Height"))

        if var == "Diameter":
            st.latex(r"d = 2\sqrt{\frac{3V}{πh}}")
            v = st.number_input("What is the volume of the cone?", min_value=0.01)
            h = st.number_input("What is the height of the cone?", min_value=0.01)
            answer = 2*(math.sqrt((3*v)/(math.pi*h)))
            st.write("The diameter is ", answer, " units.")

        if var == "Height":
            st.latex(r"h = \frac{3V}{(\frac{d}{2})²π}")
            v = st.number_input("What is the volume of the cone?", min_value=0.01)
            d = st.number_input("What is the diameter of the base?", min_value=0.01)
            answer = (3*v)/(((d/2)**2)*math.pi)
            st.write("The height is ", answer, " units.")

if mode == "Sphere":

    circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))


    if circlemode == "Radius":
        st.latex(r"V = \frac{4}{3}πr^3")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius</p>""", unsafe_allow_html=True)
        st.warning("You are calculating the radius.")
        st.latex(r"r = \sqrt[3]{\frac{V}{\frac{4π}{3}}}")
        v = st.number_input("What is the volume of the sphere?", min_value=0.01)
        answer = math.cbrt(v/(4*math.pi/3))
        st.write("The radius is ", answer, " units.")

    if circlemode == "Diameter":
        st.latex(r"V = \frac{4}{3}π(\frac{d}{2})^3")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter</p>""", unsafe_allow_html=True)
        st.warning("You are calculating the diameter.")
        st.latex(r"d = 2\sqrt[3]{\frac{V}{\frac{4π}{3}}}")
        v = st.number_input("What is the volume of the sphere?")
        answer = 2*math.cbrt(v/((4*math.pi)/3))
        st.write("The diameter is ", answer, " units.")
