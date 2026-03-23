class MinStack:

    def __init__(self):
        # •	Assign 2 list one for stack & other for history
        self.stack = []
        self.his = []    

    def push(self, val: int):
        # •	If the stack is empty.
        if not self.stack:
            #•	Push the value to stack
            self.stack.append(val)
            # •	Append the current value to the history list
            self.his.append(val)
        # •	Elif compare with current value if it is less than his[-1]
        elif val < self.his[-1]:
            # •	Append the current value to his
            self.his.append(val)
            self.stack.append(val)
        # •	Elif it was equal or greater than his[-1]
        else:
            # •	Append the his[-1] to the his
            self.his.append(self.his[-1])
            self.stack.append(val)
        

    def pop(self):
        # •	Remove the last element from stack
        self.stack.pop()
        # •	Remove the last element from his
        self.his.pop()
    def top(self):
        # •	Return the last element from the main stack without removing
        return self.stack[-1]

    def getMin(self):
        # •	Return the his[-1] 
        return self.his[-1]