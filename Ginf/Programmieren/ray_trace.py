import gturtle as gt
import math as mt


C_WIDTH = 700
C_HEIGHT = 700
V_WIDTH = 1
V_HEIGHT = 1
ORIGIN = (0, 0, 0)
DISTANCE = 1

DOT =  lambda a, b: a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
ABS =  lambda a: mt.sqrt(DOT(a, a))
CLIP = lambda x: 255 if x > 255 else x

# Cordinates are (x, z, y)

OBJECTS = [ 
    {"type": "SPHERE", "center": (0, -5001, 0), "radius": 5000, "color": (0, 255, 0)},
    {"type": "CUBE",   "center": (0, -1, 4),    "u": ((0.866, 0, 0.500), (0, 1, 0), (0.500, 0, -0.866)), "e": (1, 0.6, 1), "color": (110, 110, 110)},
    # {"type": "PRISM",  "b_base": ((), (), ()),  "t_base": ((), (), ()), color: (255, 0, 0)}
]

LIGHTS = [
    ("AMBIENT", 0.4),
    ("POINT",   0.6, (2, 1, 0)),
]

def draw_bitmap(bitmap, width, height):
    gt.penUp()
    gt.fd(height / 2)
    gt.left(90)
    gt.fd(width / 2)
    gt.rt(180)
    gt.penDown()
    for y in range(height):
        for x in range(width):
            rgb = bitmap[y][x]
            gt.setPenColor("#%02x%02x%02x" % (rgb[0], rgb[1], rgb[2]))
            gt.fd(1)

        gt.penUp()
        gt.rt(90)
        gt.fd(1)
        gt.rt(90)
        gt.fd(width)
        gt.rt(180)
        gt.penDown()

def canvas_to_viewport(x, y):
    return (x * V_WIDTH / C_WIDTH, y * V_HEIGHT / C_HEIGHT, DISTANCE)    

def compute_lightning(point, normal, view):
    i = 0
    for light in LIGHTS:
        if light[0] == "AMBIENT":
            i += light[1]
            
        else:            
            if light[0] == "POINT":
                l = (light[2][0] - point[0], light[2][1] - point[1], light[2][2] - point[2])
                t_max = 1
                
            else:
                l = light[2]
                t_max = float('inf')
                
            dot_product = DOT(normal, l)
            if dot_product > 0:
                i += light[1] * dot_product / (ABS(normal) * ABS(l))
        
    return i
    

def intersect_ray_sphere(origin, direction, sphere):
    r = sphere["radius"]
    co = (
        origin[0] - sphere["center"][0],
        origin[1] - sphere["center"][1],
        origin[2] - sphere["center"][2],
    )
    
    a = DOT(direction, direction)
    b = 2 * DOT(co, direction)
    c = DOT(co, co) - r ** 2
    
    discrimant = b ** 2 - 4 * a * c
    if discrimant < 0:
        return float("inf"), float("inf")
    
    return (-b + mt.sqrt(discrimant)) / (2 * a), (-b - mt.sqrt(discrimant)) / (2 * a)
    
def intersect_ray_cube(origin, direction, cube):
    p = [cube["center"][i] - origin[i] for i in range(3)]
    
    t_min = -float("inf")
    t_max = float("inf")  
    
    for i in range(3):
        axis = cube["u"][i]
        e_i = cube["e"][i]
        
        d = DOT(direction, axis)
        p_proj = DOT(p, axis)
        
        if abs(d) > 0.00001:
            t1 = (p_proj + e_i) / d
            t2 = (p_proj - e_i) / d
            
            if t1 > t2:
                temp = t1
                t1 = t2
                t2 = temp    
            
            t_min = max(t_min, t1)
            t_max = min(t_max, t2)
            
            if t_min > t_max:
                return float("inf"), float("inf")
        else:
            if -p_proj - e_i > 0 or -p_proj + e_i < 0:
                 return float("inf"), float("inf")
    
    return t_min, t_max

def intersect_ray_triangle(origin, direction, triangle):
    v0, v1, v3 = triangle["edges"]
    epsilon = 1e-8
    
    edge1 = [v1[i] - v0[i] for i in range(3)]
    edge2 = [v2[i] - v0[i] for i in range(3)]

def intersect_ray_prism(origin, direction, prism):
    t_min = -float("inf")
    t_max = float("inf")
    
    return t_min, t_max


def trace_ray(origin, direction, min, max):
    closest_t = float("inf")
    closest_object = None
    
    for obj in OBJECTS:
        if obj["type"] == "SPHERE":
            t1, t2 = intersect_ray_sphere(origin, direction, obj)
            
        if obj["type"] == "CUBE":
            t1, t2 = intersect_ray_cube(origin, direction, obj)
            
        if t1 > min and t1 < max and t1 < closest_t:
            closest_t = t1
            closest_object = obj
            
        if t2 > min and t2 < max and t2 < closest_t:
            closest_t = t2
            closest_object = obj
            
    if closest_object == None:
        return (255, 255, 250)
    
    point = (
        ORIGIN[0] + closest_t * direction[0],
        ORIGIN[1] + closest_t * direction[1],
        ORIGIN[2] + closest_t * direction[2],
    )
    normal = (
        point[0] - closest_object["center"][0],
        point[1] - closest_object["center"][1],
        point[2] - closest_object["center"][2],
    )
    
    if closest_object["type"] == "SPHERE":
        normal = [normal[i] / ABS(normal) for i in range(3)]
        
    elif closest_object["type"] == "CUBE":
        u = closest_object["u"]
        distances = [DOT(normal, u[i]) for i in range(3)]
        magnitudes = [abs(distances[i] / closest_object["e"][i]) for i in range(3)] 
        
        if magnitudes[0] > magnitudes[1] and magnitudes[0] > magnitudes[2]:
            normal = u[0] if distances[0] > 0 else (-u[0][0], -u[0][1], -u[0][2])
        elif magnitudes[1] > magnitudes[0] and magnitudes[1] > magnitudes[2]:
            normal = u[1] if distances[1] > 0 else (-u[1][0], -u[1][1], -u[1][2])
        else:
            normal = u[2] if distances[2] > 0 else (-u[2][0], -u[2][1], -u[2][2])
        
    inverse_direction = [direction[i] * -1 for i in range(3)]
    color_factor = compute_lightning(point, normal, inverse_direction)
    color = [closest_object["color"][i] * color_factor for i in range(3)]
    color = [CLIP(color[i]) for i in range(3)]

    return color

if __name__ == "__main__":     
    canvas = [[(0, 0, 0) for _ in range(C_WIDTH)] for _ in range(C_HEIGHT)]
    x_data = 0
    y_data = 0
    
    for y in range(int(C_HEIGHT / 2), -int(C_HEIGHT / 2), -1):
        for x in range(-int(C_WIDTH / 2), int(C_WIDTH / 2), 1):
            direction = canvas_to_viewport(x, y)
            canvas[y_data][x_data] = trace_ray(ORIGIN, direction, 1, float("inf"))
            x_data += 1
        
        x_data = 0
        y_data += 1
            
    gt.makeTurtle()
    gt.ht()
    draw_bitmap(canvas, C_WIDTH, C_HEIGHT)