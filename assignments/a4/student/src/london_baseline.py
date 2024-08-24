# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    # pass
    with open("birth_dev.tsv", encoding='utf-8') as fin:
        lines = [x.strip().split('\t') for x in fin]
        if len(lines[0]) == 1:
            print('No gold birth places provided; returning 0.0')
            return accuracy
        true_places = [x[1] for x in lines]
        total = len(true_places)
        correct = len(list(filter(lambda x: x == "London", true_places)))
        accuracy = (float(correct) / float(total)) * 100
        ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
