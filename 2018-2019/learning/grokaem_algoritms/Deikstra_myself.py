def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for i in costs:
        cost = costs[i]
        if cost < lowest_cost and i not in processed:
            lowest_cost = cost
            lowest_cost_node = i
    return lowest_cost_node