from colorthief import ColorThief

def get_color(path):
    color_thief = ColorThief(path)
    color = color_thief.get_color(quality=1)
    return '#%02x%02x%02x' % color
