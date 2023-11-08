class GF:
    def car(self):
        return "old car"


class F(GF):
    #  def car(self):
    #     return "honda civic"
    pass


class S(F):
    # def car(self):
    #     return "Lambo"
    pass


son = S()
print(son.car())
