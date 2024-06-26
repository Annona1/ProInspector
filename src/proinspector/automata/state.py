from proinspector.tools.decorators import pilogger
from proinspector.automata.letter import ReadState

@pilogger
class State:
    def __init__(self,name) -> None:
        self.name = name
        self.transitions = []

    def __str__(self):
        return self.name

    def visit(self, input_letter):
        """This method computes which transition can be triggered given the
        specified input_letter. It returns a tupple made of the output letter
        that is attached to the found transition and the state it reaches.

        >>> from pylstar.automata.State import State
        >>> from pylstar.automata.Transition import Transition
        >>> from pylstar.Letter import Letter
        >>> la = Letter('a')
        >>> l0 = Letter('0')
        >>> lb = Letter('b')
        >>> l1 = Letter('1')
        >>> s0 = State("s0")
        >>> s1 = State("s1")
        >>> t0 = Transition("t0", s1, la, l0)
        >>> t1 = Transition("t1", s0, lb, l1)
        >>> s0.transitions = [t0, t1]
        >>> (output_letter, output_state) = s0.visit(la)
        >>> print(output_letter)
        Letter('0')
        >>> print(output_state)
        s1
        >>> (output_letter, output_state) = s0.visit(lb)
        >>> print(output_letter)
        Letter('1')
        >>> print(output_state)
        s0
        >>> s0.visit(None)
        Traceback (most recent call last):
        ...
        Exception: input letter cannot be None
        >>> s0.visit(l0)
        Traceback (most recent call last):
        ...
        Exception: No transition in state 's0' could be found given letter 'Letter('0')' 


        """
        
        if input_letter is None:
            raise Exception("input letter cannot be None")
        
        for transition in self.transitions:
            if transition.input_letter == input_letter:
                return (transition.output_letter, transition.output_state)
        
        # raise Exception("No transition in state '{}' could be found given letter '{}' ".format(self.name, input_letter))
        # self._logger.debug(f"All transition in state '{self.name}': [{self.transitions}]")
        self._logger.debug(f"No transition in state '{self.name}' could be found given letter '{input_letter}', adding read state interaction")
        return (ReadState(), self)