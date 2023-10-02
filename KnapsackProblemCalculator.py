def parse_input(filename):
  with open(filename, 'r') as file:
    content = file.read().strip()
    content = content.replace('{', '(').replace('}', ')')
    capacity, items = eval(content)
    return capacity, items


def knapsack_01(capacity, items):
    n = len(items)
    
    # Initializing the table for Dynamic Programming(0s in the whole matrix table in order to shape the table to the correct dimensions)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Building up the DP table
    for i in range(1, n + 1):
      for w in range(capacity + 1):
        # Unpacking the weight and value for current item
        value, weight, _ = items[i - 1] # example: v1=1, w1=2
            
        if weight <= w:
          dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value) # we are going to either place the one above the current value, or include the previus item that is positioned in index "[w-weight]" plus the current value
        else:
          dp[i][w] = dp[i-1][w] #then, place the value that is avobe the current value

    # Retrieving the items that are selected
    selected_items = [] #here we will store the items that get the most pofit based on the table we created above
    w = capacity
    
    # We start the backtracking from the last item (n) and move towards the first (1).
    for i in range(n, 0, -1):
      
      # Extracting the value, weight, and quantity of the current item.
      value, weight, _ = items[i-1]
      
      # If the value at the current cell (dp[i][w]) is different from the value right above it (dp[i-1][w]),
      # it indicates that the current item (items[i-1]) was included in the optimal solution for the current 
      # weight w. This is the essence of the dynamic programming solution for the 0/1 knapsack problem.
      if dp[i][w] != dp[i-1][w]:
        
        # As this item is included in the optimal solution, we add its index to the selected_items list.
        selected_items.append(i)
        
        # We then subtract the weight of this item from w to move left in the DP table. This represents 
        # the remaining weight after including the current item in the solution.
        w -= weight

    # Returning the max value ,the dp table, and selected items 
    return dp[n][capacity], dp, selected_items

# Reading input from file
filename = "10.txt"
capacity, items = parse_input(filename)

max_profit, table, selected = knapsack_01(capacity, items)
actual_selected_items = [items[i-1] for i in selected]
print("Actual selected items:", actual_selected_items)

print("Maximum profit:", max_profit)
print("Selected items:", selected)

# Printing the DP table (uncomment the code below if you are using smalldatasets)
# for row in table:
#     print(row)
