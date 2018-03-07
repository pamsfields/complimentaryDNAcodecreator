def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    length=len(dna)
    return length

dna=input(print("Enter a sequence of DNA: "))
lengthDNA=get_length(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1)>len(dna2):
        result="True"
    else:
        result="False"
    return result

dna1=input(print("Enter a sequence of DNA: "))
dna2=input(print("Enter another sequence of DNA: "))
longerDNA=is_longer(dna1, dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count=dna.count(nucleotide)
    return count

nucleotide=print("Enter a nucleotide to count: ")#will be using the value requested above for a DNA sequence
occurrance=count_nucleotides(dna, nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    count=dna1.count(dna2)
    if count<0:
        result="True"
    else:
        result="False"
    return result

searchFindings=contains_sequence(dna1, dna2)# will be using the sequences requested above for dna1 and dna2


def is_valid_sequence(dna):
    '''attempting to find all characters that are not A, C, T, G in the expression given
    valid sequences would include ACTGATCGA and CATTAGACT
    invalid sequences would include THISISSILLY and PROGRAMMINGISHARD
    '''
    import re #This will check for specific expressions needed, re stands for regular expressions
    if (re.match(r'[ACTG]$',dna)):
        result= "Valid"
    else:
        result= "Invalid"
    return result
        
sequenceResult=is_valid_sequence(dna) #will be using the values requested above for dna1 and dna2 in function


def insert_sequence(dna1, dna2, insert):
    '''will need to find a way to add an insertion point, then add the sequence requested,
    and finish typing the sequence.
    Examples include "ACTGTGCA" and "ACT" with insert being 5, should return "ACTGACTTGCA"
    '''
    new_sequence=dna1[:insert] + 'dna2' + dna1[insert:]
    return new_sequence

insert=int(print("What position would you like to insert the second sequence of DNA?: "))#will be using the values for dna1 and dna2 above to complete commands
sequence_with_insertion=inser_sequence(dna1, dna2, insert)


def get_complement(nucleotide):
    '''will need to find the complimentary nucleotide for the requested input.
    I need to confirm the nucleotide that was entered was returned correctly first before getting an output correct
    '''
    import re
    pattern=r'[ACTG]'
    if re.search(pattern,nucleotide):
        complement="invalid entry"
    else:
        if nucleotide=="A":
            complement="T"
        elif nucleotide=="T":
            complement="A"
        elif nucleotide=="C":
            complement="G"
        else:
            complement="C"
    return complement

complementaryNucleotide=get_complement(nucleotide)# will be using the value requested above for nucleotide


def get_complimentary_sequence(dna):
    '''will need to find the complimentary strand for the requested input.
    I need to confirm the strand that was entered was returned correctly first before getting an output correct
    '''
    import re
    pattern=r'[actg]'
    if re.search(pattern,nucleotide):
        complementaryStrand="invalid entry"
    else:
        complementaryStrand=dna.replace("A", "T").replace("C", "G").relace("T", "A").replace("G", "C")
    return complementaryStrand

complementaryDNA=get_complimentary_sequence(dna)

