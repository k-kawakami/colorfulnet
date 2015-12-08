def xyz2rgb(xyz):
    def from_linear(v):
        def clamp(v):
            if v < 0.0:
                return 0.0
            elif v > 1.0:
                return 1.0
            else:
                return v
        if v <= 0.0031308:
            return int(clamp(v * 12.92) * 255.0 + 0.5)
        else:
            return int(clamp(1.055 * v ** (1.0 / 2.4) - 0.055) * 255.0 + 0.5)
    rgb_linear = [ 3.2410 * xyz[0] - 1.5374 * xyz[1] - 0.4986 * xyz[2],
                  -0.9692 * xyz[0] + 1.8760 * xyz[1] + 0.0416 * xyz[2],
                   0.0556 * xyz[0] - 0.2040 * xyz[1] + 1.0570 * xyz[2]]
    return [from_linear(c) for c in rgb_linear]

def rgb2xyz(rgb):
    def to_linear(c):
        v = c / 255.0
        if v <= 0.04045:
            return v / 12.92
        else:
            return ((v + 0.055) / 1.055) ** 2.4
    v = [to_linear(c) for c in rgb]
    return [ 0.4124 * v[0] + 0.3576 * v[1] + 0.1805 * v[2],
             0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2],
             0.0193 * v[0] + 0.1192 * v[1] + 0.9505 * v[2]]

def xyz2lab(xyz):
    def f(t):
        d = 6.0 / 29.0
        if t > (d ** 3):
            return t ** (1.0 / 3.0)
        else:
            return (1.0 / 3.0) * ((1 / d) ** 2) * t + (4.0 / 29.0)
    xyzn =  [0.9504,  1.0000, 1.0888] # D65
    return [116.0 * f(xyz[1] / xyzn[1]) - 16.0,
            500.0 * (f(xyz[0] / xyzn[0]) - f(xyz[1] / xyzn[1])),
            200.0 * (f(xyz[1] / xyzn[1]) - f(xyz[2] / xyzn[2]))]

def lab2xyz(lab):
    d = 6.0 / 29.0
    def f(fn, nn):
        if fn > d:
            return nn * (fn ** 3)
        else:
            return (fn - 16.0 / 116.0) * 3 * (d ** 2) * nn
    xyzn =  [0.9504,  1.0000, 1.0888] # D65
    fy = (lab[0] + 16.0) / 116.0
    fx = fy + lab[1] / 500.0
    fz = fy - lab[2] / 200.0
    return [f(fx, xyzn[0]), f(fy, xyzn[1]), f(fz, xyzn[2])]

def rgb2lab(rgb):
    return xyz2lab(rgb2xyz(rgb))

def lab2rgb(lab):
    return xyz2rgb(lab2xyz(lab))
