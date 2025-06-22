
N = 5                 # Maximum number of broken systems
arrival_rate = 2      # Average arrivals per day(λ)
service_rate = 12     # Average services per day(μ)

# P(n)
def get_probabilities(N, arrival_rate, service_rate):
    P = [1.0] 
    for n in range(1, N + 1):
        factor = ((N - n + 1) * arrival_rate) / service_rate
        P.append(P[-1] * factor)
    total = sum(P)
    return [p / total for p in P]


Pn = get_probabilities(N, arrival_rate, service_rate)

# Part A - Average number of broken systems (L)
L = 0
for n in range(N + 1):
    L += n * Pn[n]


# Part B - Average waiting time for repair (W)
effective_arrival_rate = 0
for n in range(N + 1):
    effective_arrival_rate += (N - n) * arrival_rate * Pn[n]

if effective_arrival_rate > 0:
    W = L / effective_arrival_rate
else:
    float('inf') 


# Part C - Probability that more than 2 systems are broken
P_more_than_2_broken_systems = 0
for n in range(3, N + 1):
    P_more_than_2_broken_systems += Pn[n]


print("P(n) probabilities:")
for n, p in enumerate(Pn):
    print(f"P({n}) = {p:.4f}")

print("\nResults:")
print(f"Part 1 - Average number of broken systems (L): {L:.4f}")
print(f"Part 2 - Average waiting time for repair (W): {W:.4f} days")
print(f"Part 3 - Probability that more than 2 systems are broken: {P_more_than_2_broken_systems:.4f}")
print(f"Is the probability less than 20%? {'Yes' if P_more_than_2_broken_systems < 0.20 else 'No'}")
