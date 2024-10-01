#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """
    Determine the winner of the prime game between Maria and Ben.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers, where each integer n represents the set
                 {1, 2, ..., n} for a round of the game.

    Returns:
    str: The name of the player with the most wins ("Maria" or "Ben").
         Return None if no player has more wins than the other.
    """

    # Handle edge cases where there are no rounds or no valid nums
    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to know the upper limit for prime generation
    max_n = max(nums)
    
    # Step 1: Use the Sieve of Eratosthenes to mark primes up to max_n
    # Initialize a boolean array where True represents a prime number
    primes = [False, False] + [True] * (max_n - 1)  # False for 0 and 1, True for the rest

    # Mark non-prime numbers using the Sieve of Eratosthenes
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            # Mark multiples of the prime number i as non-prime
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of primes up to each number n
    # prime_count[i] will store the number of primes from 1 to i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        # Increment the prime count if i is a prime number
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Step 3: Simulate the game for each round
    for n in nums:
        # Determine the winner of the round:
        # If the number of primes up to n is odd, Maria wins; if even, Ben wins
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
