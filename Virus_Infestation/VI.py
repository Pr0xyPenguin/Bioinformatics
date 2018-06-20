import random
from Bio import SeqIO

#Necessary initialization for reading our fasta file
genom_shotgun_sequence = []

#Reading fasta file
for record in SeqIO.parse("6.37_nucleotide.fasta", "fasta"):
    genom_shotgun_sequence = genom_shotgun_sequence + list(record.seq) #we take all the chains that make up the virus

#Necessary initializations for program
product_sequence = ''
changes = []
i = 0
while True:
    k = 0
    #if necleotide A then replace with multyA
    if genom_shotgun_sequence[i] == 'A':
        k = k +random.randint(1,5)
    #if necleotide C then replace with multyC
    elif genom_shotgun_sequence[i] == 'C':
        k = k + random.randint(1,10)
    #if necleotide G or T then replace with multyG or multy T respectively
    else:
        k = k + random.randint(1,10)
        while(random.randint(0,1)==1):#We want a number larger or equal of 1 but we don't want to overflow our memory
            k = k + random.randint(1,10)
    #we check the next nucleotide, if it is the same as the current one we keep the sum (k) to prevent duplications
    if (i < len(genom_shotgun_sequence)-1 and genom_shotgun_sequence[i] != genom_shotgun_sequence[i+1]):
            product_sequence = product_sequence + genom_shotgun_sequence[i] + '!' +str(k)
    i = i + 1
    if (i >= len(genom_shotgun_sequence)):
        #to prevent our index to be out of bounds we add the last multyNucleotide when we exit the loop
        product_sequence = product_sequence + genom_shotgun_sequence[i-1] + '!' +str(k)
        break


print(product_sequence)
