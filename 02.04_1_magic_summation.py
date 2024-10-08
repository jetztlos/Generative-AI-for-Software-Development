import sys
# import numpy
import numpy as np

def magic_summation(n, seed=None):
    ### DO NOT REMOVE OR CHANGE THE COMMAND BELOW 
    ### AS IT WON'T BE POSSIBLE TO CORRECTLY GRADE YOUR SOLUTION
    np.random.seed(seed=seed)
    if n <= 2:
        return "n cannot be less than or equal to 2"
    elif not isinstance(n, int):
        return "n must be an integer"
    ### YOUR CODE HERE ###
        
    magic_list = list(range(1, n + 1))
    indices_to_remove = set([int(np.random.random() * n) + 1 for _ in range(int(np.random.random() * n) + 1)])

    if len(indices_to_remove) == len(magic_list):
        print("Magic summation is equal to 0.")
        return 0

    def iterator():
        for idx in indices_to_remove:
            if idx < len(magic_list):
                magic_list.pop(idx)
        for i in range(len(magic_list)):
            if i < len(magic_list) - 1:
                magic_list[i] = magic_list[i + 1] // magic_list[i]
        for el in magic_list:
            yield el

    it = iterator()
    magic_summation_value = 0

    while True:
        try:
            magic_summation_value += next(it)
        except StopIteration:
            break

    print("Magic summation is equal to: {0}.".format(magic_summation_value))
    return magic_summation_value
    ### YOUR CODE ENDS HERE ###

    # return magic_summation_value

#######################################
####### DO NOT EDIT THIS PART #########
#######################################

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("You must pass at most two arguments, the value for n and/or the random seed")
        sys.exit()
    elif len(sys.argv) == 1:
        print("You must pass at least one argument, the value for n")
        sys.exit()
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        seed = int(sys.argv[2])
    else:
        n = int(sys.argv[1])
        seed = None

    magic_summation(n, seed=seed)