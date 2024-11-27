class Stone:
    def __init__(self, s_Type: str, x: int = None, y: int = None):
        self.s_Type = s_Type  # iron, N, S, etc.
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y