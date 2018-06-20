import random
from Bio import SeqIO
from Bio.Blast import NCBIWWW

history = []

for record in SeqIO.parse("sequence_1.fasta", "fasta"):
    m = len(record)

for record in SeqIO.parse("sequence_2.fasta", "fasta"):
    n = len(record)




if (m%2 == 0 or n%2 == 0):
    winner = True
else:
    winner = False


print(m,n)
while(True):
    if (n < m):
        m, n = n, m
    if m == 1 and n == 1:
        break
    else:
        if m%2 == 0 :
            if((m/ 2)%2 == 1):
                m, n = m/2, m/2
            else:
                m, n = 1, m-1
        elif n%2 == 0:
            if((n/ 2)%2 == 1):
                m, n = n/2, n/2
            else:
                m, n = n - 1, 1
        else:
            temp = random.randint(1,max(m, n))
            m, n = temp, max(m, n) - temp
    print(m, n)

for i in range(len(history)):
    print(history[i])
if winner == True:
    print('Player 1 wins!')
else:
    print('Player 2 wins!')
