class WordMachine:
    def __init__(self):
        self.result = []
        self.error = ''

    def opperation_error(self):
        self.error = 'Operations need at least two inputs'

    def push(self,input):
        self.result.append(input)
    
    def pop(self):
        del self.result[-1]
    
    def duplicate(self):
        if not len(self.result) > 0:
            self.error = 'List is empty / impossible opperation'
            return 
        self.result.append(self.result[-1])

    def sub(self):
        if not len(self.result)> 1:
            self.opperation_error()
            return
        r = self.result[-2] - self.result[-1]
        result = self.result[:-2]
        result.append(r)
        self.result = result
        
    def add(self):
        if not len(self.result)> 1:
            self.opperation_error()
            return
        r = self.result[-2] + self.result[-1]
        result = self.result[:-2]
        result.append(r)
        self.result = result
    
    def reset(self):
        self.result = []
        self.error = ''

    def interpreter(self,op):
        if op == "+":
            self.add()
            return
        if op == "-":
            self.sub()
            return
        if op.lstrip("-").isnumeric():
            self.push(int(op))
            return
        if op == "POP":
            self.pop()
        if op == "DUP":
            self.duplicate()


    def get_result(self,input):
        self.reset()
        input_list = input.split(" ")
        for op in input_list:
            self.interpreter(op)
        return self.result

