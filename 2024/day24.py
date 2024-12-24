from help import *


class Solver:
    def __init__(self):
        # parse inputs
        is_wire = True
        wires = {}
        gates = []
        for line in get_input():
            if line == '':
                is_wire = False
            elif is_wire:
                wire, val = line.split(': ')
                wires[wire] = val == '1'
            else:
                operation, z = line.split(' -> ')
                x, f, y = operation.split(' ')
                gates.append((x, f, y, z))

        self.wires = wires
        self.gates = gates

        # extras
        self.input_count = 1 + max([int(wire[1:]) for wire in self.wires])
        self.translations = {}
        self.operations = {}
        self.switched_wires = []

    def solve1(self, part2=False):
        self.solve_circuit()

        solution = self.get_z_value()
        if not part2:
            print('Solution 1: %s' % solution)
        return solution

    def solve2(self):
        """ Switches are limited to 4 and circuit is a simple adder -> partial manual search
            Simply switching the off wires at printed bits works, the switches seem to be contained at a local bit level
            So search checks are limited
        """
        solution = True
        self.switch('z06', 'fkp')
        self.switch('z11', 'ngr')
        self.switch('z31', 'mfm')
        self.switch('bpt', 'krj')

        for i in range(self.input_count):
            n = 1 << i
            self.set_inputs(n, 0)
            res = self.solve1(True)
            if res != n:
                solution = False
                print('z' + '0'*(i<10) + str(i), "is incorrect:", n, self.solve1(True))

        if not solution:
            solution = "Switches are incorrect"
        else:
            wires = self.switched_wires
            wires.sort()
            solution = ('%s,'*len(wires) % tuple(wires))[:-1]

        print('Solution 2: %s' % solution)

    def solve_circuit(self):
        gates = self.gates
        while gates:
            new_gates = []
            for x, f, y, z in gates:
                if x in self.wires and y in self.wires:
                    a, b = self.wires[x], self.wires[y]
                    if f == 'AND':
                        out = a & b
                    elif f == 'XOR':
                        out = a ^ b
                    else:
                        out = a | b
                    self.wires[z] = out
                else:
                    new_gates.append((x, f, y, z))
            gates = new_gates

    def get_z_value(self):
        count = 0
        for wire in self.wires:
            if wire[0] != 'z' or not self.wires[wire]:
                continue
            n = int(wire[1:])
            count += 1 << n
        return count

    def set_inputs(self, x, y):
        self.wires = {}
        for i in range(self.input_count):
            num = str(i)
            if i < 10:
                num = '0' + num
            self.wires['x'+num] = (x & (1 << i)) > 0
            self.wires['y'+num] = (y & (1 << i)) > 0

    def switch(self, z0, z1):
        gates = []
        for x, f, y, z in self.gates:
            if z in [z0, z1]:
                z = z0 == z and z1 or z0
            gates.append((x, f, y, z))
        self.gates = gates
        self.switched_wires += [z0, z1]


solver = Solver()
solver.solve1()
solver.solve2()
