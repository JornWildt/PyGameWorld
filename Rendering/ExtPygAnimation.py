import pygame
import pyganim

# This class accepts a list of images (frames) and splits into one isometric sized 3D grid
# of "size_boxe" dimensions where each grid item contains the same number of frames, just smaller.
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
                        inv_z = (size_box[2]-z-1)
                        xpos = (x+y) * xmult
                        ypos = (y-x) * ymult + inv_z * zmult
                        ysize = 48 if z != 0 else 64
                        sub_image = pygame.Surface((64,ysize), pygame.SRCALPHA)
                        # sub_image.fill((128,0,0,128))
                        sub_image.blit(frame[0], (0,0), (xpos,ypos,64,ysize))
                        sub_frames.append((sub_image,frame[1]))
                    animation = pyganim.PygAnimation(sub_frames)
                    animation.play()
                    self.sub_animations[x][y][z] = animation

        self.animation = pyganim.PygAnimation(frames)


    def play(self):
        self.animation.play()


    # Render one a sub-animation (indexed by "offset") at position.
    def blit(self, screen, pos, offset):
        # Currently, the rendering findes a bit more boxes/tiles than necessary, so verify boundaries
        if offset[0] < self.size_box[0] and offset[1] < self.size_box[1] and offset[2] < self.size_box[2]:
            self.sub_animations[offset[0]][offset[1]][offset[2]].blit(screen, pos)
