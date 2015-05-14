__author__ = 'Frankie'

import math
import sys
import os.path
from Animal_Path import Point, Line, Path
import json


def main():

    list = []
    path = Path()

    try:
        f = sys.argv[1]
    except IndexError:
        f = os.path.dirname(os.path.realpath(__file__)) + "/json_points.json"
        try:
            path_points = json.loads(open(f).read())
        except ValueError:
            print("No JSON object in file")
            return

    try:
        interval = int(path_points[1]['t'])
    except (SyntaxError, NameError):
        print("Please enter a numeric interval")
        return

    time = 0

    for line in path_points:
        try:
            temp = [int(line['x']), int(line['y'])]

        except ValueError:
            print("Points are not in correct format in file " + (os.path.realpath(f)))
            return
        list.append(Point(temp[0], temp[1], time))
        time += interval
        if len(list) == 2:
            path.add_to_path(Line(list[0], list[1]))
            list.reverse()
            list.pop()

    if not path.move_check():
        print("Animal did not move")
        return

    for i in range(int(math.ceil((float(len(path.line_segments)+1)*interval)/60))):
        hour_path = Path()
        for seg in path.line_segments:
            if seg.end.time in range(i*60, (i+1)*60):
                hour_path.add_to_path(seg)
        if len(hour_path.line_segments) > 0:
            if hour_path.same_point_check():
                print("Animal did not move during hour %s" %(i+1))
            else:
                print("Curviness over hour %s is %s " % ((i+1), hour_path.calc_curviness()))
        else:
            print("Animal did not move during hour %s" % (i+1))
    print("Curviness of whole path is %s" % (path.calc_curviness()))

if __name__ == "__main__":
    main()

