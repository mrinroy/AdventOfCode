from collections import deque

"""
Base class
"""
class Operation:
    
    def eval(self, x):
        raise NotImplementedError

class Add(Operation):
    def __init__(self, x):
        self.x = x
    
    def eval(self, x):
        return self.x + x

class Sub(Operation):
    def __init__(self, x):
        self.x = x
    
    def eval(self, x):
        return self.x + x

class Mul(Operation):
    def __init__(self, x):
        self.x = x
    
    def eval(self, x):
        return self.x * x

class Div(Operation):
    def __init__(self, x):
        self.x = x
    
    def eval(self, x):
        return x // self.x

class Dbl(Operation):
    def eval(self, x):
        print(f" Perform {x} + {x}")
        return x + x

class Sqr(Operation):
    def eval(self, x):
        return x * x

class Const(Operation):
    def __init__(self, x):
        self.x = x
    
    def eval(self, x):
        return self.x


class Monkey:
    def __init__(self):
        self.holding = []
        self.operation = None
        self.divisor = None
        self.true_to = None
        self.false_to = None
        self.inspected = 0
        
    
    def add_item(self, worry):
        self.holding.append(worry)
    
    def add_items(self, items):
        self.holding.extend(items)
    
    def partition(self, scores):
        true_list, false_list = [], []
        for score in scores:
            true_list.append(score) if score % self.divisor == 0 else false_list.append(score)
        return (self.true_to, true_list),(self.false_to, false_list)

    def inspect(self):
        self.inspected += len(self.holding)
        evaluated = map(self.operation.eval, self.holding)
        self.holding = []
        return evaluated
    
    def has_item(self):
        return len(self.holding) != 0


def get_monkeys(in_file):
    monkeys = {}
    with open(in_file) as file:
        for line in file:
            line = line.strip()
            
            if line.startswith("Monkey"):
                monkey_id = int(line[7:-1])
                cur_monkey = monkeys[monkey_id] = Monkey()

            elif line.startswith("Starting items: "):
                items = deque(map(int, line[len("Starting items: "): ].split(', ')))
                cur_monkey.holding = items
            elif line.startswith("Test: divisible by "):
                divisor = int(line[len("Test: divisible by "): ])
                cur_monkey.divisor = divisor
            elif line.startswith("If true: throw to monkey "):
                true_to = int(line[len("If true: throw to monkey "): ])
                cur_monkey.true_to = true_to
            elif line.startswith("If false: throw to monkey "):
                false_to = int(line[len("If false: throw to monkey "): ])
                cur_monkey.false_to = false_to
            elif line.startswith("Operation: new = old "):
                operator, num = line[len("Operation: new = old "): ].split(' ')
                num = num
                if operator == "+":
                    cur_monkey.operation = Add(int(num)) if num != "old" else Dbl()
                elif operator == "-":
                    cur_monkey.operation = Sub(int(num)) if num != "old" else Const(0)
                elif operator == "*":
                    cur_monkey.operation = Mul(int(num)) if num != "old" else Sqr()
                elif operator == "/":
                    cur_monkey.operation = Div(int(num)) if num != "old" else Const(1) 
                
            else:
                pass
    return monkeys

def simulate(monkeys, rounds, relief_factor, cycle):
    for i in range(rounds):
        for monkey in monkeys.values():
            evaluated = monkey.inspect()
            evaluated = map(lambda x: (x // relief_factor)%cycle, evaluated)
            for monkey_id, scores in monkey.partition(evaluated):
                monkeys[monkey_id].add_items(scores)
            
            
def part_1(in_file):
    monkeys = get_monkeys(in_file)
    cycle = 1
    for m in monkeys.values():
        cycle *= m.divisor
    simulate(monkeys, 20, 3, cycle)
    top_1, top_2 = 0, 0
    for v in [m.inspected for m in monkeys.values()]:
        if v >= top_1:
            top_2, top_1 = top_1, v
        elif v > top_2:
            top_2 = v
    
    print ("Most actives: ", top_1, top_2)
    return top_1 * top_2

def part_2(in_file):
    monkeys = get_monkeys(in_file)
    cycle = 1
    for m in monkeys.values():
        cycle *= m.divisor
    simulate(monkeys, 10000, 1, cycle)
    top_1, top_2 = 0, 0
    for v in [m.inspected for m in monkeys.values()]:
        if v >= top_1:
            top_2, top_1 = top_1, v
        elif v > top_2:
            top_2 = v
    
    print ("Most actives: ", top_1, top_2)
    return top_1 * top_2

if __name__ == "__main__":
    in_file = "input.txt"
    print ("Part 1: ", part_1(in_file))
    
    print ("Part 2: ", part_2(in_file))
            
            


