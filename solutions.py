def solve_max_profit(n):
    # Building definitions: (Name, Build Time, Earnings per unit of operational time)
    buildings = [
        ('T', 5, 1500),  # Theatre
        ('P', 4, 1000),  # Pub[cite: 1]
        ('C', 10, 2000)  # Commercial Park[cite: 1]
    ]
    
    # dp[t] stores (max_earnings, building_mix) at time t
    dp = [(0, {'T': 0, 'P': 0, 'C': 0}) for _ in range(n + 1)]
    
    for t in range(n + 1):
        curr_earn, curr_mix = dp[t]
        for name, time_taken, rate in buildings:
            if t + time_taken <= n:
                finish_time = t + time_taken
                operational_time = n - finish_time
                new_earn = curr_earn + (operational_time * rate)
                
                if new_earn > dp[finish_time][0]:
                    new_mix = curr_mix.copy()
                    new_mix[name] += 1
                    dp[finish_time] = (new_earn, new_mix)
                    
    # Find the maximum earnings achieved at any timeline state
    max_total_earn = 0
    best_mix = {'T': 0, 'P': 0, 'C': 0}
    for t in range(n + 1):
        if dp[t][0] > max_total_earn:
            max_total_earn = dp[t][0]
            best_mix = dp[t][1]
            
    return max_total_earn, best_mix