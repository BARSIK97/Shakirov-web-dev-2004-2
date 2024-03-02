n, m = map(int, input().split()) 
cargo = [] 

for _ in range(m):
    name, weight, cost = input().split() 
    weight = int(weight)
    cost = int(cost)
    cargo.append((name, weight, cost)) 

cargo.sort(key=lambda x: x[2] / x[1], reverse=True) 
current_weight = 0
loaded_cargo = [] 

for name, weight, cost in cargo:
    if current_weight + weight <= n:
        loaded_weight = weight 
    else: 
        loaded_weight = n - current_weight 
        loaded_cost = cost * loaded_weight / weight
        loaded_cargo.append((name, loaded_weight, loaded_cost))
        current_weight += loaded_weight
        if current_weight == n: 
            break

for name, weight, cost in loaded_cargo:
    print(name, "{:.2f}".format(weight), "{:.2f}".format(cost))

