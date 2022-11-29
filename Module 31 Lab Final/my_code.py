def haf_Adder(A, B):
    sum = A ^ B
    carry = A & B

    print('sum of halfAdder', sum)
    print('carry of halfAdder', carry)

if __name__ == "__main__":
    A = 0
    B = 1
    haf_Adder(A,B)


