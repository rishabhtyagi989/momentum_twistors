"""
Class containing the bracket expressions
"""

from sympy import Function, latex
from sympy import symbols

class ab(Function):
    """Angle Bracket class"""
    def _latex(self, printer, exp=1):
        """Overwriting the latex outputs to get the appropriate latex string"""
        a, b = [printer._print(i) for i in self.args]
        a = a.replace('p_{', "").replace('}', "")
        b = b.replace('p_{', "").replace('}', "")
        if exp == 1:
            return r"\langle %s %s \rangle" % (a, b)
        else:
            return r"\langle %s %s \rangle^{%s}" % (a, b, exp)
        
class sb(Function):
    """Square Bracket class"""
    def _latex(self, printer, exp=1):
        """Overwriting the latex outputs to get the appropriate latex string"""
        a, b = [printer._print(i) for i in self.args]
        a = a.replace('p_{', "").replace('}', "")
        b = b.replace('p_{', "").replace('}', "")
        if exp == 1:
            return r"\left[ %s %s \right]" % (a, b)
        else:
            return r"\left[ %s %s \right]^{%s}" % (a, b, exp)
class tw(Function):
    """Momentum Twistor Bracket class"""
    def _latex(self, printer, exp=1):
        """Overwriting the latex outputs to get the appropriate latex string"""
        a, b, c, d = [printer._print(i) for i in self.args]
        a = a.replace('p_{', "").replace('}', "")
        b = b.replace('p_{', "").replace('}', "")
        c = c.replace('p_{', "").replace('}', "")
        d = d.replace('p_{', "").replace('}', "")
        if exp == 1:
            return r"\langle %s %s %s %s \rangle" % (a, b, c, d)
        else:
            return r"\langle %s %s %s %s \rangle" % (a, b, c, d, exp)
