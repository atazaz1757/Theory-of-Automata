class Checking_DFA:
    word=' '
    initial_state=0
    final_state=0
    current_state=0

    def _init_(self):
        self.word=' '
        self.initial_state=0
        self.final_state=0
    def constructor(self,w,i,c,f):
        self.word=w
        self.initial_state=i
        self.current_state = c
        self.final_state=f

    def transitionfunction(self,alphabet,state):
        if state==0:
            if alphabet=='a':
                state=2
            elif alphabet=='b':
                state=2
            elif alphabet=='c':
                state=1
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==1:
            if alphabet=='a':
                state=3
            elif alphabet=='b':
                state=2
            elif alphabet=='c':
                state=2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==2:
            if alphabet=='a':
                state=3
            elif alphabet=='b':
                state=3
            elif alphabet=='c':
                state=3
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==3:
            if alphabet=='a':
                state=3
            elif alphabet=='b':
                state=3
            elif alphabet=='c':
                state=3
            else:
                print("INVALID CHARACTER: ", alphabet)

        return state

    def DFA_working(self,neword):
        self.word = neword
        for i in self.word:
            self.current_state = self.transitionfunction(self,i, self.current_state)
        if self.current_state == self.final_state:
            print("VALID STRING: ", neword,"\n")
        else:
            print("INVALID STRING: ", neword,"\n")

if __name__ == "__main__":
    print("DFA ")
    word = str(input("Enter the String: "))
    Checking_DFA()
    Checking_DFA.constructor(Checking_DFA, word, 0, 0, 2)
    Checking_DFA.DFA_working(Checking_DFA, word)
