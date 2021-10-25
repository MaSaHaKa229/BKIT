from lab2_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Square"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{} {} colour with side {} square {}.'.format(
            self.color.colorproperty,
            Square.get_figure_type(),
            self.side,
            self.mesure()
        )
