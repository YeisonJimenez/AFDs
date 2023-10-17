from afd import AFD_Moore1, AFD_Moore

# afd1 = AFD_Moore1()
# simbolo = '010'
# q = 'q2'
#
# # estado_siguiente = afd.next_state(q, simbolo)
# # print(f'El estado siguiente es: {estado_siguiente}')
# # print(f'La salida es: {afd.salida}')
# print('--' * 50, '\n\n')
# print('--' * 50)
# cadena = '0001010010101010001010'
# evaluar = afd1.evaluar(cadena)
# # print(f'Autómata con entrada: {cadena}. {evaluar}')
cadena = '000001010011100101'
num_states = 3
outs = ['00', '01', '10']
trans = ['000', '001', '010', '011', '100', '101']

afd = AFD_Moore(num_states=num_states, outs=outs, symbols=trans)

afd.transition(state='q0', simbol='000', next_state='q0')
afd.transition(state='q0', simbol='001', next_state='q1')
afd.transition(state='q1', simbol='010', next_state='q2')
afd.transition(state='q1', simbol='011', next_state='q1')
afd.transition(state='q2', simbol='100', next_state='q0')
afd.transition(state='q2', simbol='101', next_state='q1')
next_state = afd.next_state('q0', '001')
afd.evaluate(cadena)
print(f'Estados del autómata: {afd.states}')
print(f'Transiciones: {afd.transitions}')
print(f'El estado siguiente es: {next_state}')