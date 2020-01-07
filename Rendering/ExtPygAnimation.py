import pygame
import pyganim

class ExtPygAnimation:

    def __init__(self, settings, frames, size_box = (1,1,1)):
        self.sub_animations = [[[None for z in range(size_box[2])] for y in range(size_box[1])] for x in range(size_box[0])]
        self.size_box = size_box

        xmult = settings.map_tile_pixels/2
        ymult = settings.map_tile_pixels/4
        zmult = settings.map_tile_pixels/2

        for x in range(size_box[0]):
            for y in range(size_box[1]):
                for z in range(size_box[2]):
                    sub_frames = []
                    for frame in frames:
                        xpos = (x+y) * xmult
                        ypos = (y-x) * ymult + (size_box[2]-z-1) * zmult
                        sub_image = pygame.Surface((64,64), pygame.SRCALPHA)
                        #sub_image.fill((128,0,0,128))
                        sub_image.blit(frame[0], (0,0), (xpos,ypos,64,64))
                        sub_frames.append((sub_image,frame[1]))
                    animation = pyganim.PygAnimation(sub_frames)
                    animation.play()
                    self.sub_animations[x][y][z] = animation


        self.animation = pyganim.PygAnimation(frames)

    def play(self):
        self.animation.play()

    def blit(self, screen, pos, offset):
        #self.animation.blit(screen, pos)
        if offset[0] < self.size_box[0] and offset[1] < self.size_box[1] and offset[2] < self.size_box[2]:
            self.sub_animations[offset[0]][offset[1]][offset[2]].blit(screen, pos)
