"""
Experiment 1: User Reaction Time
Amelia St. Claire | MindTech-Research
"""

import random
import time

def main():
    print("Experiment 1: User Reaction Time")
    print("Press Enter as soon as you see 'Go!'")
    input("Press Enter to start...")

    reaction_times = []
    num_trials = 10

    for trial in range(num_trials):
        delay = random.randint(2, 5)  # Random delay before showing "Go!"
        time.sleep(delay)

        print("Go!")
        start_time = time.time()
        input()  # Wait for Enter key press
        end_time = time.time()

        reaction_time = end_time - start_time
        reaction_times.append(reaction_time)
        print(f"Trial {trial + 1}: Reaction Time = {reaction_time:.2f} seconds")

    avg_reaction_time = sum(reaction_times) / num_trials
    print(f"\nAverage Reaction Time: {avg_reaction_time:.2f} seconds")

if __name__ == "__main__":
    main()
