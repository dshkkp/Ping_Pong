import pygame
from objects.paddle import Paddle
from objects.ball import Ball



class GameEngine:
    def __init__(self, config: dict):
        self.config = config

        win_w = config["window"]["width"]
        win_h = config["window"]["height"]
        panel_w = config["window"]["panel_width"]

        self.field_x = panel_w
        self.field_width = win_w - panel_w
        self.field_height = win_h

        paddle_cfg = config["paddle"]
        ball_cfg = config["ball"]

        # левый паддл
        self.left_paddle = Paddle(
            self.field_x + 30,
            self.field_height / 2 - paddle_cfg["height"] / 2,
            paddle_cfg["width"],
            paddle_cfg["height"],
            paddle_cfg["speed"],
            self.field_height,
        )

        # правый паддл
        self.right_paddle = Paddle(
            self.field_x + self.field_width - 30 - paddle_cfg["width"],
            self.field_height / 2 - paddle_cfg["height"] / 2,
            paddle_cfg["width"],
            paddle_cfg["height"],
            paddle_cfg["speed"],
            self.field_height,
        )

        self.ball = Ball(
            self.field_x + self.field_width / 2,
            self.field_height / 2,
            ball_cfg["size"],
            ball_cfg["base_speed"],
            self.field_width,
            self.field_height,
        )

        self.score_left = 0
        self.score_right = 0

        self.state = GameState.RUNNING
        self.win_score = config["game"]["win_score"]

        self.difficulty_name = config["game"]["initial_difficulty"]
        self.difficulty_multiplier = config["difficulty_presets"][self.difficulty_name]
        
