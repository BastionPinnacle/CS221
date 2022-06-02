import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

############################################################
# Custom Types
# NOTE: You do not need to modify these.

"""
You can think of the keys of the defaultdict as representing the positions in the sparse vector,
while the values represent the elements at those positions. Any key which is absent from the dict means that
that element in the sparse vector is absent (is zero). Note that the type of the key used should not affect the
algorithm. You can imagine the keys to be integer indices (e.g., 0, 1, 2) in the sparse vectors, but it should work
the same way with arbitrary keys (e.g., "red", "blue", "green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problem 3a

def find_alphabetically_last_word(text: str) -> str:
    """
    Given a string |text|, return the word in |text| that comes last
    lexicographically (i.e., the word that would come last after sorting).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() handy here. If the input text is an empty string, 
    it is acceptable to either return an empty string or throw an error.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(text.split())

    # END_YOUR_CODE

#print(find_alphabetically_last_word("big poppa biggie notorious"))
############################################################
# Problem 3b

def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc1[0]-loc2[0])**2+(loc1[1]-loc2[1])**2)
    # END_YOUR_CODE

print(euclidean_distance([1,0],[0,0]))
############################################################
# Problem 3c

def mutate_sentences(sentence: str) -> List[str]:
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 17 lines of code, but don't worry if you deviate from this)
    words = sentence.split()
    pairs = {}
    length = len(words)
    for i in range(1,length,1):
        if(words[i-1] in pairs):
            pairs[words[i-1]].append(words[i])
        else:
            pairs[words[i-1]] = [words[i]]
    pairs[""] = [k for k in pairs.keys()]
    current_phrase = [""]
    all_phrases = []

    

print(mutate_sentences("the cat and the mat"))

############################################################
# Problem 3d

def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Given two sparse vectors (vectors where most of the elements are zeros) |v1| and |v2|, each
    represented as collections.defaultdict(float), return their dot product.

    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return sum([v*v2[k] for k,v in v1.items() if k in v2 ])
    # END_YOUR_CODE
v2 = {'1' : 1.0, '2' : 3.0, '6': 6.0}
for k in v2:
    print(k)
#v1 = {'1' : 1.0, '2' : 2.0, '4': 4.0, '6': 6.0}
#
#print(sparse_vector_dot_product(v1,v2))
############################################################
# Problem 3e

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scalar is zero, you are allowed to modify v1 to include any additional keys in v2, 
    or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for k in v2:
        if(k in v1):
            v1[k]+=(scale*v2[k])
        else:
            v1[k]= (scale*v2[k])
    # END_YOUR_CODE

    
############################################################
# Problem 3f

def find_singleton_words(text: str) -> Set[str]:
    """
    Split the string |text| by whitespace and return the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    words = text.split("")
    d = {}
    for word in words:
        if(word in d):
            d[word] = 1
        else:
            d[word]+=1
    return [k for k,v in d.items() if v ==1]
    # END_YOUR_CODE
