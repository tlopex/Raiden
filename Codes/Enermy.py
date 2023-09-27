class Enermy:
    posx_upper_bound = 580
    posx_lower_bound = -90
    posy_upper_bound = 450
    posy_lower_bound = -40

    def __init__(other, x, y, sx, sy, imagepath):
        other.posx = x
        other.posy = y
        other.speedx = sx
        other.speedy = sy
        other.image = imagepath

def local1():
    Target = Enermy(0, 50, 5, 5, "enermy.png")

if __name__ == "__main__":
    local1()
