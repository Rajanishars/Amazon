def find_starting_pump(n: int, petrol: list, distance: list) -> int:
    total_surplus = 0
    current_surplus = 0
    start_index = 0
    for i in range(n):
        net_petrol = petrol[i] - distance[i]
        total_surplus += net_petrol
        current_surplus += net_petrol
        if current_surplus < 0:
            start_index = i + 1
            current_surplus = 0
    return start_index if total_surplus >= 0 else -1
n_input = int(input("Enter the number of petrol pumps (N): "))
petrol_input = list(map(int, input("Enter petrol amounts separated by spaces: ").split()))
distance_input = list(map(int, input("Enter distances separated by spaces: ").split()))
result = find_starting_pump(n_input, petrol_input, distance_input)
print(result)
