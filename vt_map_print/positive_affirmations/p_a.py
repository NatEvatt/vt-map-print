#!/usr/bin/env python
import random

def print_affirmation() :
    """Prints out a randomly selected affirmation. Test that your python environment is set up correctly and that everything correctly installed.  """
    compliments = ["I can tap into a wellspring of inner happiness anytime I wish.",
                    "By allowing myself to be happy, I inspire others to be happy as well.",
                    "Every day and in every way I am getting better and better",
                    "I am abundantly joyful and happy",
                    "I find beauty and joy in ordinary things",
                    "My life is a joy. I relax easily and open myself up to delightful surprises",
                    "My life is a joy filled with love, fun and friendship",
                    "I choose love, joy and freedom, open my heart and allow wonderful things to flow into my life.",
                    "I am free, and always have been. Experiences that made me feel like a victim were only experiences that appeared and disappeared in the arena of consciousness that I am",
                    "Every day and in every way I am getting better and better"]

    test = random.randint(1,len(compliments) - 1)
    print(compliments[test])

if __name__ == '__main__':
    print_affirmation()
