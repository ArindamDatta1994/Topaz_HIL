def rank_results(results, distances):
    paired = list(zip(results, distances[0]))
    paired.sort(key=lambda x: x[1])  # lower distance = better
    return [r[0] for r in paired]