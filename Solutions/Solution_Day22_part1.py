MODULO = 16777216

def transform(secret):
    secret ^= (secret * 64) % MODULO
    secret %= MODULO

    secret ^= (secret // 32) % MODULO
    secret %= MODULO

    secret ^= (secret * 2048) % MODULO
    secret %= MODULO

    return secret

def simulate_buyers(initial_secrets, iterations):
    results = []
    for secret in initial_secrets:
        for _ in range(iterations):
            secret = transform(secret)
        results.append(secret)
    return results

def read_input(file_path):
    with open(file_path, "r") as file:
        return list(map(int, file.readlines()))

file_path = "Datasets/dataset_day22.txt"
initial_secrets = read_input(file_path)
iterations = 2000

final_secrets = simulate_buyers(initial_secrets, iterations)
result_sum = sum(final_secrets)
print(result_sum)