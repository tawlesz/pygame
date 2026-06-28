#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame import Surface, Rect

from code.Const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, WIN_WIDTH
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('assets/BgMenu.png') #load img
        self.rect = self.surf.get_rect(left=0, top=0) #define where the img will begin to be drawn

    def run(self, ): 
        pygame.mixer_music.load('assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2 ), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2 ), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2 ), 200 + (i * 30)))

            pygame.display.flip()

            # check for all events   
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() # close window
                   print('pygame End')
                   quit() # end pygame
    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)