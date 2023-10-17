"""
Autómata Finitos Deterministas, AFDs.

"""


# import numpy as np


class AFD_Moore1:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estado_actual = 'q0'
        self.estado_siguiente = self.estado_actual
        self.estados = {'q0', 'q1', 'q2'}
        self.estados_finales = {}
        self.salidas = {'q0': '00', 'q1': '01', 'q2': '10'}

    def next_state(self, estado, simbolo):
        self.estado_actual = estado
        self.simbolo = simbolo

        if self.estado_actual == 'q0' and simbolo == '000':
            self.estado_actual, self.estado_siguiente = 'q0', 'q0'

        elif self.estado_actual == 'q0' and simbolo == '001':
            self.estado_actual, self.estado_siguiente = 'q0', 'q1'

        elif self.estado_actual == 'q1' and simbolo == '010':
            self.estado_actual, self.estado_siguiente = 'q1', 'q2'

        elif self.estado_actual == 'q1' and simbolo == '011':
            self.estado_actual, self.estado_siguiente = 'q1', 'q1'

        elif self.estado_actual == 'q2' and simbolo == '100':
            self.estado_actual, self.estado_siguiente = 'q2', 'q0'

        elif self.estado_actual == 'q2' and simbolo == '101':
            self.estado_actual, self.estado_siguiente = 'q2', 'q1'

        else:
            # raise ValueError('Transición no válida para el símbolo dado')
            self.estado_siguiente = None
            print(f'Transición no válida para el símbolo dado: {simbolo}, en el estado: {self.estado_actual}')

        if self.estado_actual == 'q0':
            self.salida = self.salidas['q0']
        elif self.estado_actual == 'q1':
            self.salida = self.salidas['q1']
        elif self.estado_actual == 'q2':
            self.salida = self.salidas['q2']
        else:
            print('El estado actual no tiene salida')

        # print(
        #     f'Transición desde {self.estado_actual} a {self.estado_siguiente} con símbolo {simbolo} y salida: {self.salida}')

        return self.estado_siguiente

    def _transiciones(self, simbolo):

        if self.estado_actual == 'q0' and simbolo == '000':
            self.estado_actual, self.estado_siguiente = 'q0', 'q0'

        elif self.estado_siguiente == 'q0' and simbolo == '001':
            self.estado_actual, self.estado_siguiente = 'q0', 'q1'

        elif self.estado_siguiente == 'q1' and simbolo == '010':
            self.estado_actual, self.estado_siguiente = 'q1', 'q2'

        elif self.estado_siguiente == 'q1' and simbolo == '011':
            self.estado_actual, self.estado_siguiente = 'q1', 'q1'

        elif self.estado_siguiente == 'q2' and simbolo == '100':
            self.estado_actual, self.estado_siguiente = 'q2', 'q0'

        elif self.estado_siguiente == 'q2' and simbolo == '101':
            self.estado_actual, self.estado_siguiente = 'q2', 'q1'

        else:
            # raise ValueError('Transición no válida para el símbolo dado')
            print(f'Transición no válida para el símbolo dado: {simbolo}, en el estado: {self.estado_actual}')

        if self.estado_actual == 'q0':
            salida = self.salidas['q0']
        elif self.estado_actual == 'q1':
            salida = self.salidas['q1']
        elif self.estado_actual == 'q2':
            salida = self.salidas['q2']
        else:
            print('El estado actual no tiene salida')

        print(
            f'Transición desde {self.estado_actual} a {self.estado_siguiente} con símbolo {simbolo} y salida: {salida}')

    def evaluar(self, cadena):
        print(f'Estados del autómata: {self.estados}')
        print(f'Estado inicial del autómata: {self.estado_inicial}')
        print(f'Cadena de entrada: {cadena}\n')
        print('...Evaluando cadena de entrada...\n')
        # Dividir la cadena en partes de tres símbolos
        partes = [cadena[i:i + 3] for i in range(0, len(cadena), 3)]
        for simbolo in partes:
            self._transiciones(simbolo)
        print('\n...Evaluación completada...')


class AFD_Moore:
    def __init__(self, num_states, outs: list = None, symbols: list = None, initial_state: str = None):
        self.num_states = num_states
        self.outs = outs
        self.simbols = symbols
        self.initial_state = initial_state
        self.num_character = len(symbols[0])
        self.states = []
        for i in range(num_states):
            states = 'q' + str(i)
            self.states.append(states)
        self.transitions = {}

    def next_state(self, state, simbol):
        if state is self.states and simbol is self.simbols:
            q_next = self.transitions[(state, simbol)]
        else:
            print(f"State {state} doesn't exist or symbol {simbol} doesn't exist!")

        # return q_next

    def transition(self, state, simbol, next_state):
        self.state = state
        self.simbol = simbol
        self.future_state = next_state
        self.transitions[(self.state, self.simbol)] = self.future_state

    def _transitions(self, simbol):
        # if self.estado_actual == 'q0' and simbolo == '000':
        #     self.estado_actual, self.estado_siguiente = 'q0', 'q0'
        # self.now_state = self.initial_state
        # if self.now_state == self.initial_statel and simbol is self.simbols:

        for state in self.transitions.keys():
            if self.transitions[state[0], simbol]:
                print(f'Transition function: ({state[0]}, {simbol}) = {self.transitions[state[0], simbol]}')
            else:
                print(f'**********Invalid sequential!***********')

    def evaluate(self, chain):
        print(f'Automaton states: {self.states}')
        print(f'Initial state: {self.initial_state}')
        print(f'Input chain: {chain}\n')
        print('...Evaluating input chain...\n')
        # Dividir la cadena en partes de símbolos
        parts = [chain[i:i + self.num_character] for i in range(0, len(chain), self.num_character)]
        for simbol in parts:
            self._transitions(simbol)
        print('\n...Evaluating completed...')


if __name__ == '__main__':
    # Ejemplo de uso
    # afd = AFD_Moore1()
    #
    # # Cadena de ejemplo
    # cadena_ejemplo = '000001010100'
    #
    # # Evaluar si la cadena es aceptada
    # es_aceptada = afd.evaluar(cadena_ejemplo)
    num_states = 3
    outs = ['00', '01', '10']
    trans = ['000', '001']
    afd = AFD_Moore(num_states=num_states, outs=outs, symbols=trans)
    afd.transition(state='q0', simbol='001', next_state='q1')
    afd.transition(state='q0', simbol='001', next_state='q1')
    next_state = afd.next_state('q0', '000')
    print(f'Estados del autómata: {afd.states}')
    print(f'Estado siguiente: {next_state}')
