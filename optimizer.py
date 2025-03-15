from data_loader import df
def optimize_budget(data, budget):
    platforms = data["platform"].unique()
    allocations = {}
    
    for platform in platforms:
        platform_data = data[data["platform"]==platform]
        avg_cac = platform_data["CAC"].mean()
        
        # Allocate budget inversely proportional to CAC
        allocations[platform] =budget * (1/ avg_cac) / sum(1 / data.groupby("platform")["CAC"].mean())
    return allocations
budget = 100000 # $100k marketing budget
allocations = optimize_budget(df, budget)
print("Optimized Budget Allocation:", allocations)