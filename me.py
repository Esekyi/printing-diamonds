"""     
     for i in range(N):
              spaces = N-(i+1)
              asterix = i+1
              print('{}{}'.format(" "* spaces, "$" * asterix))
print_asterix(6)
print_asterix(3)
print_asterix(16)
"""
def print_asterix(N):
       for i in range(1,N+1):
              space1 = N - i
              stars1 = (2*i)-1
              print('{}{}'.format(" "* space1, "*"* stars1))
       for j in range(N-1,0,-1):
              space2 = N - j
              stars2 = (2*j)-1
              print('{}{}'.format(" "* space2, "*"* stars2))

print_asterix(5)