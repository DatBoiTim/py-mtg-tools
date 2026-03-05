#!/bin/python3
import typing

class Mana:
    """
    This can be cost, current pool, amounts produced on trigger
    For the case of costs, all values should be negative
    For multi-X costs a should be a negative number equal to X*number of X costs. So XX cost of X=1 would have an a of -2.
    """
    w: int
    b: int
    u: int # This is blue
    g: int
    r: int
    c: int # This is colorless/generic
    a: int # Any color, like treasure tokens or X costs
    t: int # Total

    def __init__(self, wh, bl, ub, gr, rd, cl, an):
        self.w = wh
        self.b = bl
        self.u = ub
        self.g = gr
        self.r = rd
        self.c = cl
        self.a = an
        self._calc_total()

    def adjust_mana(self, delta: typing.Self) -> None:
        """
        Adjusts mana by the delta
        """
        self._set_w(self.w + prod.w)
        self._set_b(self.b + prod.b)
        self._set_u(self.u + prod.u)
        self._set_g(self.g + prod.g)
        self._set_r(self.r + prod.r)
        self._set_c(self.c + prod.c)
        self._set_a(self.a + prod.a)
        self._calc_total

    def _set_w(value: int) -> None:
        self.w = value

    def _set_b(value: int) -> None:
        self.b = value

    def _set_u(value: int) -> None:
        self.u = value

    def _set_g(value: int) -> None:
        self.g = value

    def _set_r(value: int) -> None:
        self.r = value

    def _set_c(value: int) -> None:
        self.c = value

    def _set_a(value: int) -> None:
        self.a = value

    def _calc_total(self) -> None:
        self.t = self.w + self.b + self.u + self.g + self.r + self.c + self.a
    

def main():
    # Note: For anything with an X cost the krarkulator will cast all spells with the same X, rather than just the highest while remaining mana positive for a win, copy, and cast.
    flip_it()
    win_count: int = 0 # e.g. Okaun
    fail_count: int = 0 # e.g. The coinflip minotaur
    cast_count: int = 0 # e.g. Aetherflux Reservoir
    copy_count: int = 0 # e.g. Any copy triggers which don't produce mana
    total_spells: int = 0 # How many of the original plus copies are you resolving from this? Note: if you have instants to copy spells on the stack, resolve that first before whatever you are copying.

if __name__ == "__main__":
    main()
    
