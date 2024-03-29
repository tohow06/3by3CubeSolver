#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename      : video.py
# Author        : Kim K
# Created       : Fri, 29 Jan 2016
# Last Modified : Sun, 31 Jan 2016


from sys import exit as Die
try:
    import sys
    import cv2
    from colordetection import ColorDetector
    # from rubikscubetracker import RubiksVideo, RubiksImage, merge_two_dicts, RubiksOpenCV
    import os
    import sys
    import numpy as np
    import time
except ImportError as err:
    Die(err)


class Webcam:

    def __init__(self):
        self.cam              = cv2.VideoCapture(0)
        self.stickers         = self.get_sticker_coordinates('main')
        self.current_stickers = self.get_sticker_coordinates('current')
        self.preview_stickers = self.get_sticker_coordinates('preview')

    def get_sticker_coordinates(self, name):
        """
        Every array has 2 values: x and y.
        Grouped per 3 since on the cam will be
        3 rows of 3 stickers.

        :param name: the requested color type
        :returns: list
        """
        stickers = {
            'main': [
                [440, 120], [640, 120], [840, 120],
                [440, 320], [640, 320], [840, 320],
                [440, 510], [640, 510], [840, 510]
            ],
            'current': [
                [20, 20], [54, 20], [88, 20],
                [20, 54], [54, 54], [88, 54],
                [20, 88], [54, 88], [88, 88]
            ],
            'preview': [
                [20, 130], [54, 130], [88, 130],
                [20, 164], [54, 164], [88, 164],
                [20, 198], [54, 198], [88, 198]
            ]
        }
        return stickers[name]


    def draw_main_stickers(self, frame):
        """Draws the 9 stickers in the frame."""
        for x,y in self.stickers:
            cv2.rectangle(frame, (x,y), (x+100, y+100), (255,255,255), 2)

    def draw_current_stickers(self, frame, state):
        """Draws the 9 current stickers in the frame."""
        for index,(x,y) in enumerate(self.current_stickers):
            cv2.rectangle(frame, (x,y), (x+16, y+16), ColorDetector.name_to_rgb(state[index]), -1)

    def draw_preview_stickers(self, frame, state):
        """Draws the 9 preview stickers in the frame."""
        for index,(x,y) in enumerate(self.preview_stickers):
            cv2.rectangle(frame, (x,y), (x+32, y+32), ColorDetector.name_to_rgb(state[index]), -1)

    def color_to_notation(self, color):
        """
        Return the notation from a specific color.
        We want a user to have green in front, white on top,
        which is the usual.

        :param color: the requested color
        """
        notation = {
            'g'  : 'F',
            'w'  : 'U',
            'b'   : 'B',
            'r'    : 'R',
            'o' : 'L',
            'y' : 'D'
        }
        return notation[color]
            
    def writefile(self, state, count):
        color = open('rubikcubecolor.txt', 'r')
        colors = color.readlines()
        color.close()
        colorss =''
        app = []
        colorss = colorss + state[0] + ','
        for i in range(1, 8, 1):
            colorss = colorss + state[i] + ','
        colorss = colorss + state[8] + '\n'
        if count >= 1 and count <= 4:
            app.append(state[2])
            app.append(state[5])
            app.append(state[8])
            app.append(state[1])
            app.append(state[4])
            app.append(state[7])
            app.append(state[0])
            app.append(state[3])
            app.append(state[6])
            state = app
        elif count == 5:
            app.append(state[6])
            app.append(state[3])
            app.append(state[0])
            app.append(state[7])
            app.append(state[4])
            app.append(state[1])
            app.append(state[8])
            app.append(state[5])
            app.append(state[2])
            state = app
        if colorss not in colors:
            color = open('rubikcubecolor.txt', 'a')
            color.write(state[0] + ',')
            for i in range(1, 8, 1):
                color.write(state[i] + ',')
            color.write(state[8] + '\n')
            color.close()
            count += 1
        return count

    def scan(self):
        """
        Open up the webcam and scans the 9 regions in the center
        and show a preview in the left upper corner.

        After hitting the space bar to confirm, the block below the
        current stickers shows the current state that you have.
        This is show every user can see what the computer toke as input.

        :returns: dictionary
        """

        sides   = {}
        preview = ['w','w','w',
                   'w','w','w',
                   'w','w','w']
        state   = [0,0,0,
                   0,0,0,
                   0,0,0]
        os.system('echo > testcolor.txt')
        os.system('rm -rf rubikcubecolor.txt')
        os.system('echo > rubikcubecolor.txt')
        count = 0
        
        while True:
            _, frame = self.cam.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            key = cv2.waitKey(10) & 0xff
            flag = 0
            # init certain stickers.
            self.draw_main_stickers(frame)
            self.draw_preview_stickers(frame, preview)
            
            for index,(x,y) in enumerate(self.stickers):
                roi          = hsv[y:y+100, x:x+100]
                avg_hsv      = ColorDetector.average_hsv(roi)
                color_name   = ColorDetector.get_color_name(avg_hsv)
                state[index] = color_name
                # update when space bar is pressed.
                if key == 32:
                    preview = list(state)
                    self.draw_preview_stickers(frame, state)
                    face = self.color_to_notation(state[4])
                    notation = [self.color_to_notation(color) for color in state]
                    sides[face] = notation
            if key == 32:
                flag += 1
                count = self.writefile(state, count)
            if key == ord('b'):
                flag += 1
                delete = open('rubikcubecolor.txt', 'r')
                deletes = delete.readlines()
                delete.close()
                deletes.pop()
                add = open('rubikcubecolor.txt', 'w')
                for i in range(len(deletes)):
                    add.write(deletes[i])
                add.close()
            tick = time.time()
            if flag == 1:
                while True:
                    if time.time() - tick >= 0.2:
                        break
            # show the new stickers
            self.draw_current_stickers(frame, state)

            # append amount of scanned sides
            text = 'scanned sides: {}/6'.format(len(sides))
            cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

            # quit on escape.
            if key == 27:
                break

            # show result
            cv2.imshow("default", frame)
        self.cam.release()
        cv2.destroyAllWindows()
        return sides if len(sides) == 6 else False

webcam = Webcam()
