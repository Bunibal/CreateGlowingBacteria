conv_dic = {"A": "T", "T": "A", "G": "C", "C": "G"}


def compstrand(strand):
    return "".join([conv_dic[bp] for bp in strand])


def read_input_stick(filename):
    with open(filename, "r") as file:
        seqs = [line.rstrip('\n') for line in file]
        plasmid = seqs[0]
        rest_plasm = seqs[1]
        gfp = seqs[2]
        res1, res2 = seqs[3].split()
        p5_pl, p3_pl = cut(plasmid, rest_plasm)
        p5_gfp, p3_gfp = cut(gfp, res1, res2, plas=False)
        return p5_pl[0] + p5_gfp + p5_pl[1], p3_pl[0] + p3_gfp + p3_pl[1]


def cut(seq, *args, plas=True):
    if plas:
        i = seq.find(args[0])
        prime5 = (seq[:i + 1], seq[i + 1:])
        prime3 = (compstrand(seq[:i + 5]), compstrand(seq[i + 5:]))

    else:
        i = seq.find(args[0])
        j = seq.rfind(args[1])
        prime5 = seq[i + 1:j + 1]

        comp = compstrand(seq)
        i = comp.find(compstrand(args[0]))
        j = comp.rfind(compstrand(args[1]))
        prime3 = comp[i + 5:j + 5]
    return prime5, prime3


prime5, prime3 = read_input_stick(input())

print(prime5)
print(prime3)
