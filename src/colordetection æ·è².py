#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename      : colordetection.py
# Author        : Kim K
# Created       : Tue, 26 Jan 2016
# Last Modified : Sun, 31 Jan 2016


from sys import exit as Die
try:
    import sys
    from collections import Counter
except ImportError as err:
    Die(err)

class ColorDetection:

    def get_color_name(self, hsv):
        """ Get the name of the color based on the hue.

        :returns: string
        """
        (h,s,v) = hsv
        """colorset = open('testcolor.txt', 'a')
        colorset.write(str(h) + ',' + str(s) + ',' + str(v) + '\n')
        colorset.close()"""
        
        #print((h,s,v))
        if (h < 10 or h > 124) and s > 40:
            return 'red'
        if h <= 20 and h >= 10:
            return 'orange'
        elif h <= 255 and s <= 40:
            return 'white'
        elif h <= 45 and h > 25:
            return 'yellow'
        elif h <= 100 and h > 45:
            return 'green'
        if h > 100 and h <= 124 or s >= 215:
            return 'blue'
        
        return 'white'
        """
        if h < 15 and v < 100:
            return 'red'
        if h <= 10 and v > 100:
            return 'orange'
        elif h <= 30 and s <= 100:
            return 'white'
        elif h <= 40:
            return 'yellow'
        elif h <= 85:
            return 'green'
        elif h <= 130:
            return 'blue'

        return 'white'"""

    def name_to_rgb(self, name):
        """
        Get the main RGB color for a name.

        :param name: the color name that is requested
        :returns: tuple
        """
        color = {
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
        }
        return color[name]

    def average_hsv(self, roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = 0
        s   = 0
        v   = 0
        num = 0
        color = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        term = [0, 0, 0]
        leny = round(len(roi)/3)
        lenx = round(len(roi[0])/3)
        for i in range(3):
            for j in range(3):
                num = 0
                for y in range(0 + leny * i, leny + leny * i, 1):
                    for x in range(0 + lenx * i, lenx + lenx * i, 1):
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
                h /= num
                s /= num
                v /= num
                h = int(h)
                s = int(s)
                v = int(v)
                colorset = open('testcolor.txt', 'a')
                colorset.write(str(h) + ',' + str(s) + ',' + str(v) + '\n')
                colorset.close()
                #print(int(h), int(s), int(v))
                #s**2 + v**2 >= 44100
                if (s**2 + v**2 >= 20000):
                    color[j + 3 * i] = 1 #red
                if (s<61 and 140>=h and h>=65) or (v<(s**2-5625)/-22.5) or (s<86 and v<245 and 140>=h and h>=65):
                    color[j + 3 * i] = 3 #white
                if (s>100 and 115>=h and h>=100 and v<250) or (s>100 and 115>=h and h>=90 and v>250):
                    color[j + 3 * i] = 6 #blue
                if (s>100 and 95>=h and h>=70 and v<250) or (s>100 and 90>=h and h>=70 and v>250):
                    color[j + 3 * i] = 5 #green
                if (255>=v and v>110 and 14>=h and h>=4 and s>=75):
                    color[j + 3 * i] = 2 #orange
                if (250>v and v>10 and 45>=h and h>=14 and s>=75):
                    color[j + 3 * i] = 4 #yellow
                """if (h < 10 or h > 124) and s > 40:
                    color[j + 3 * i] = 1 #red
                if h <= 20 and h >= 10:
                    color[j + 3 * i] = 2 #orange
                elif h <= 255 and s <= 40:
                    color[j + 3 * i] = 3 #white
                elif h <= 45 and h > 25:
                    color[j + 3 * i] = 4 #yellow
                elif h <= 90 and h > 45:
                    color[j + 3 * i] = 5 #green
                if h > 90 and h <= 124:
                    color[j + 3 * i] = 6 #blue"""
        word_counts = Counter(color)
        top = word_counts.most_common(1)
        num1 = top[0][0]
        """#print(num1)
        if num1 == 1:
            term[0] = 1
        elif num1 == 2:
            term[0] = 2
        elif num1 == 3:
            term[0] = 3
        elif num1 == 4:
            term[0] = 4
        elif num1 == 5:
            term[0] = 5
        elif num1 == 6:
            term[0] = 6
        else:
            term[0] = 3
        leny = round(len(roi)/9)
        for i in range(3):
            for j in range(3):
                num = 0
                for y in range(0 + leny * i, leny + leny * i, 1):
                    for x in range(len(roi[0])):
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
                h /= num
                s /= num
                v /= num
                h = int(h)
                s = int(s)
                v = int(v)
                colorset = open('testcolor.txt', 'a')
                colorset.write(str(h) + ',' + str(s) + ',' + str(v) + '\n')
                colorset.close()
                #print(int(h), int(s), int(v))
                if (s**2 + v**2 >= 20000):
                    color[j + 3 * i] = 1 #red
                if (s<61 and 140>=h and h>=65) or (v<(s**2-5625)/-22.5) or (s<86 and v<245 and 140>=h and h>=65):
                    color[j + 3 * i] = 3 #white
                if (s>100 and 115>=h and h>=100 and v<250) or (s>100 and 115>=h and h>=90 and v>250):
                    color[j + 3 * i] = 6 #blue
                if (s>100 and 95>=h and h>=70 and v<250) or (s>100 and 90>=h and h>=70 and v>250):
                    color[j + 3 * i] = 5 #green
                if (255>=v and v>110 and 14>=h and h>=4 and s>=75):
                    color[j + 3 * i] = 2 #orange
                if (250>v and v>10 and 45>=h and h>=14 and s>=75):
                    color[j + 3 * i] = 4 #yellow"""
                """if (h < 10 or h > 124) and s > 40:
                    color[j + 3 * i] = 1 #red
                if h <= 20 and h >= 10:
                    color[j + 3 * i] = 2 #orange
                elif h <= 255 and s <= 40:
                    color[j + 3 * i] = 3 #white
                elif h <= 45 and h > 25:
                    color[j + 3 * i] = 4 #yellow
                elif h <= 90 and h > 45:
                    color[j + 3 * i] = 5 #green
                if h > 90 and h <= 124:
                    color[j + 3 * i] = 6 #blue"""
        """word_counts = Counter(color)
        top = word_counts.most_common(1)
        num1 = top[0][0]
        #print(num1)
        if num1 == 1:
            term[1] = 1
        elif num1 == 2:
            term[1] = 2
        elif num1 == 3:
            term[1] = 3
        elif num1 == 4:
            term[1] = 4
        elif num1 == 5:
            term[1] = 5
        elif num1 == 6:
            term[1] = 6
        else:
            term[1] = 3
        lenx = round(len(roi)/9)
        for i in range(3):
            for j in range(3):
                num = 0
                for y in range(len(roi)):
                    for x in range(0 + lenx * i, lenx + lenx * i, 1):
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
                h /= num
                s /= num
                v /= num
                h = int(h)
                s = int(s)
                v = int(v)"""
                """colorset = open('testcolor.txt', 'a')
                colorset.write(str(h) + ',' + str(s) + ',' + str(v) + '\n')
                colorset.close()"""
                """#print(int(h), int(s), int(v))
                if (s**2 + v**2 >= 20000):
                    color[j + 3 * i] = 1 #red
                if (s<61 and 140>=h and h>=65) or (v<(s**2-5625)/-22.5) or (s<86 and v<245 and 140>=h and h>=65):
                    color[j + 3 * i] = 3 #white
                if (s>100 and 115>=h and h>=100 and v<250) or (s>100 and 115>=h and h>=90 and v>250):
                    color[j + 3 * i] = 6 #blue
                if (s>100 and 95>=h and h>=70 and v<250) or (s>100 and 90>=h and h>=70 and v>250):
                    color[j + 3 * i] = 5 #green
                if (255>=v and v>110 and 14>=h and h>=4 and s>=75):
                    color[j + 3 * i] = 2 #orange
                if (250>v and v>10 and 45>=h and h>=14 and s>=75):
                    color[j + 3 * i] = 4 #yellow"""
                """if (h < 10 or h > 124) and s > 40:
                    color[j + 3 * i] = 1 #red
                if h <= 20 and h >= 10:
                    color[j + 3 * i] = 2 #orange
                elif h <= 255 and s <= 40:
                    color[j + 3 * i] = 3 #white
                elif h <= 45 and h > 25:
                    color[j + 3 * i] = 4 #yellow
                elif h <= 90 and h > 45:
                    color[j + 3 * i] = 5 #green
                if h > 90 and h <= 124:
                    color[j + 3 * i] = 6 #blue"""
        """word_counts = Counter(color)
        top = word_counts.most_common(1)
        num1 = top[0][0]
        #print(num1)
        if num1 == 1:
            term[2] = 1
        elif num1 == 2:
            term[2] = 2
        elif num1 == 3:
            term[2] = 3
        elif num1 == 4:
            term[2] = 4
        elif num1 == 5:
            term[2] = 5
        elif num1 == 6:
            term[2] = 6
        else:
            term[2] = 3"""
        word_counts = Counter(term)
        top = word_counts.most_common(1)
        num1 = top[0][0]
        if num1 == 1:
            return (int(5), int(100), int(100))
        elif num1 == 2:
            return (int(15), int(100), int(100))
        elif num1 == 3:
            return (int(200), int(0), int(100))
        elif num1 == 4:
            return (int(30), int(100), int(100))
        elif num1 == 5:
            return (int(60), int(100), int(100))
        elif num1 == 6:
            return (int(110), int(230), int(100))
        else:
            return (int(200), int(0), int(100))

ColorDetector = ColorDetection()
