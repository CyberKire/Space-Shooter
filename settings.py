class Settings():
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0,0,0)

        #Ship speed
        self.ship_speed_factor = 1.5

        #Settings for bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3