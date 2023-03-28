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

    def run(self):

        # * MAIN LOOP * #
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick(FPS) / 1000
            self.check_scenes(dt)
            self.switch_scenes()
            pygame.display.update()

    def check_scenes(self, dt):
        """
        更新场景
        """

        for scene in self.scenes.values():
            if scene.active:
                scene.run(dt)

    def switch_scenes(self):
        """
        场景转换的条件及控制
        """

        if self.scenes["start_menu"].quit_button.clicked:
            pygame.quit()
            sys.exit()

