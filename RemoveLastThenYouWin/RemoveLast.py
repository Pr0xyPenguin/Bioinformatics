import random
from Bio import SeqIO
from Bio.Blast import NCBIWWW


#Needed for printing the last 5 nucleotides of our sequence
def calc_len(x):
    if x >= 5:
        return x-5
    else:
        return 0

#Necessary initialization for reading our fasta file
genom_shotgun_sequence = []
state = 0

#Reading fasta file
for record in SeqIO.parse("sequence.fasta", "fasta"):
    genom_shotgun_sequence = record.seq
    state = len(record) % 3 #to privent having the length of every new sequence being calculated on each loop

#Running BLAST and and saving its results in a XML file

print("Aligning Sequence...")
result_handle = NCBIWWW.qblast("blastn", "nt", genom_shotgun_sequence)
print("Creating XML file with results...")
with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()
print("Done")

genom_shotgun_sequence = list (genom_shotgun_sequence)

if state == 0:
    win_num = 2
else:
    win_num = 1
print ('The winner will be: Player: ' + str(win_num))
player1 = bool(random.getrandbits(1))
#state = 0 is the losing state
#state = 1 | 2 are the winning states
#The aim for the winning states is to keep the other player in the 0 state (a sequence dividable by 3)
while(genom_shotgun_sequence != []):
    player1 = not (player1)
    if state == 0 :
        #if both players follow the winning strategy then which ever the current player chooses it doesn't affect the result
        if random.randint(1,2) == 1:
            genom_shotgun_sequence.pop(len(genom_shotgun_sequence)-1)
            state = 2
        else:
            genom_shotgun_sequence.pop(len(genom_shotgun_sequence)-1)
            genom_shotgun_sequence.pop(len(genom_shotgun_sequence)-1)
            state = 1
    elif state == 1 :
        #the current player needs to have the other player constantly removing from a sequence multiple of three
        genom_shotgun_sequence.pop(len(genom_shotgun_sequence)-1)
        state = 0
    else:
        #the current player needs to have the other player constantly removing from a sequence multiple of three
        genom_shotgun_sequence.pop(len(genom_shotgun_sequence)-1)
        genom_shotgun_sequence.pop(len(genom_shotgun_sequence)-1)
        state = 0
    if player1 == True:
        print ('Player-1',len(genom_shotgun_sequence) , genom_shotgun_sequence[calc_len(len(genom_shotgun_sequence)):len(genom_shotgun_sequence)])
    else:
        print ('Player-2',len(genom_shotgun_sequence) , genom_shotgun_sequence[calc_len(len(genom_shotgun_sequence)):len(genom_shotgun_sequence)])
print ('The winner is: Player: ' + str(int(player1)+1))
