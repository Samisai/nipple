#!/usr/bin/env python

import os
from pynput import keyboard
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('nipple')

ctrl_pressed = False
shift_pressed = False
current_sound_file = None

force_playsound = len(os.sys.argv) > 1 and os.sys.argv[1] == '--playsound'

try:
    if force_playsound:
        raise ImportError

    import pygame
    use_pygame = True
    pygame.mixer.init()
    logger.info('use pygame for playing sound')
except ImportError:
    try:
        from playsound import playsound, PlaysoundException
        use_pygame = False
        logger.info('use playsound for playing sound')
    except ImportError:
        import os
        if force_playsound:
            print "install playsound, when forcing it, or use pygame"
        else: 
            print "install either pygame or playsound (e.g. via pip)"
        os.sys.exit(1)


def play(sound_file):
    if use_pygame:
        try:
            global current_sound_file
            pygame.mixer.music.stop()
            if not sound_file is current_sound_file:
                current_sound_file = sound_file
                pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except pygame.error:
            logger.debug('no file "%s" found' % sound_file)
    else:
        try:
            playsound(sound_file)
        except PlaysoundException:
            logger.debug('no file "%s" found' % sound_file)


def on_press(key):
    global ctrl_pressed
    global shift_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = True

    if key == keyboard.Key.shift:
        shift_pressed = True

    if ctrl_pressed and shift_pressed:
        if key == keyboard.Key.f1:
            play('nipple_s1.ogg')
        elif key == keyboard.Key.f2:
            play('nipple_s2.ogg')
        elif key == keyboard.Key.f3:
            play('nipple_s3.ogg')
        elif key == keyboard.Key.f4:
            play('nipple_s4.ogg')
        elif key == keyboard.Key.f5:
            play('nipple_s5.ogg')
        elif key == keyboard.Key.f6:
            play('nipple_s6.ogg')
        elif key == keyboard.Key.f7:
            play('nipple_s7.ogg')
        elif key == keyboard.Key.f8:
            play('nipple_s8.ogg')
        elif key == keyboard.Key.f9:
            play('nipple_s9.ogg')
        elif key == keyboard.Key.f10:
            play('nipple_s10.ogg')
        elif key == keyboard.Key.f11:
            play('nipple_s11.ogg')
        elif key == keyboard.Key.f12:
            play('nipple_s12.ogg')


    elif ctrl_pressed:
        if key == keyboard.Key.f1:
            play('nipple1.ogg')
        elif key == keyboard.Key.f2:
            play('nipple2.ogg')
        elif key == keyboard.Key.f3:
            play('nipple3.ogg')
        elif key == keyboard.Key.f4:
            play('nipple4.ogg')
        elif key == keyboard.Key.f5:
            play('nipple5.ogg')
        elif key == keyboard.Key.f6:
            play('nipple6.ogg')
        elif key == keyboard.Key.f7:
            play('nipple7.ogg')
        elif key == keyboard.Key.f8:
            play('nipple8.ogg')
        elif key == keyboard.Key.f9:
            play('nipple9.ogg')
        elif key == keyboard.Key.f10:
            play('nipple10.ogg')
        elif key == keyboard.Key.f11:
            play('nipple11.ogg')
        elif key == keyboard.Key.f12:
            play('nipple12.ogg')

def on_release(key):
    global ctrl_pressed
    global shift_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = False

    if key == keyboard.Key.shift:
        shift_pressed = False

def main():
    lis = keyboard.Listener(on_press=on_press, on_release=on_release)
    lis.start() # start to listen on a separate thread
    lis.join() # no this if main thread is polling self.keys

if __name__ == '__main__':
    main()