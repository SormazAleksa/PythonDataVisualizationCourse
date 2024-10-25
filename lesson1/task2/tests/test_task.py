from __init__ import plt

def plot():
    line = plt.gca().lines[0]
    assert line.get_color() == 'r', "Line color should be red"
    assert line.get_marker() == 'o',  "Marker should be a circle"
    assert plt.gca().get_xgridlines(), "Grid should be enabled"

