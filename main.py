import heapq


def min_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        cable_a = heapq.heappop(cables)
        cable_b = heapq.heappop(cables)
        combined_cables = cable_a + cable_b
        total_cost += combined_cables
        heapq.heappush(cables, combined_cables)

    return total_cost, sum(cables)


source_cables = [8, 4, 5, 6, 12]
overall_costs, total_cables = min_cost(source_cables)
print(f"Загальні витрати: {overall_costs}, довжина кабелів: {total_cables}")
