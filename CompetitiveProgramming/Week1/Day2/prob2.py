def intersect(x, a, y, b):
    hp = max(x, y)
    lp = min(x + a, y + b)
    if hp >= lp:
        return (None, None)
    length = lp - hp
    return (hp, length)

def find_rectangular_overlap(rect1, rect2):
    new_x, new_a  = intersect(rect1['left_x'], rect1['width'], rect2['left_x'], rect2['width'])
    new_y, new_b = intersect(rect1['bottom_y'], rect1['height'], rect2['bottom_y'], rect2['height'])
    if not new_a or not new_b:
        return {
            'left_x'   : None,
            'bottom_y' : None,
            'width'    : None,
            'height'   : None,
        }

    return {
        'left_x'   : new_x,
        'bottom_y' : new_y,
        'width'    : new_a,
        'height'   : new_b,
    }