# AoC 2017 - Day 6a

def load_data():
    with open('input.txt', 'r') as infile:
        vals = [int(x) for x in infile.read().strip().split()]
    return {n:vals[n] for n in range(16)}

def balance(state):
    prevstates = set()
    staterep = ''.join([str(x) for x in state.values()])

    while staterep not in prevstates:
        prevstates.add(staterep)
        highbank = min([k for k, v in state.items() if v == max(state.values())])
        distval = state[highbank]
        state[highbank] = 0
        for x in range(1, distval + 1):
            state[(highbank + x) % len(state)] += 1
        staterep = ''.join([str(x) for x in state.values()])

    return len(prevstates)

def main():
    print(balance(load_data()))

if __name__ == '__main__':
    main()
