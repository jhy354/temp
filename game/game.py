import sys

import pygame

from engine.settings import *
from engine.utils import custom_load
from engine.utils import Debug
from game.scenes import StartMenu


class GameApp:
    """
    游戏应用类
    """

    def __init__(self):

        # * Pygame Init * #
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_icon(custom_load(r"./logo.ico", (16, 16)))
        self.clock = pygame.time.Clock()
        Debug(DEBUG_MODE).div()

        self.scenes = self.load_scenes()
        self.scenes["start_menu"].activate()

        Debug(True) << "Inited Game" << "\n"
        Debug(True).div()

    @staticmethod
    def load_scenes():
        """
        加载场景
        """

        scenes = {}
        start_menu = StartMenu()

        scenes["start_menu"] = start_menu
        print(scenes)

        return scenes
