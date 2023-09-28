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
        weight, value, _ = items[i - 1] # example: v1=2, w1=3
            
        if weight <= w:
          dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value) # we are going to either place the one above the current value, or include the previus item that is positioned in index "[w-weight]" plus the current value
        else:
          dp[i][w] = dp[i-1][w] #then, place the value that is avobe the current value

    # Retrieving the items that are selected
    selected_items = [] #here we will store the items that get the most pofit based on the table we created above
    w = capacity
    
    #we will go in reverse from the bottom right corner to find the maximum profit and the items to be considered
    for i in range(n, 0, -1):
      if dp[i][w] != dp[i-1][w]:
        # if the item abovce is different then we will go to the index that is calculated by substracting the weight of the column minus weigth of the item "[w-weight]" and use the index to go to the above item
        #we will first append the current row since it was selected   
        selected_items.append(i)
        
        #each item in the list is a tuple of the form (weight, value, quantity)
        #therefore we will update the weight in order to go to the next value above us 
        w -= items[i-1][0]

    # Returning the max value ,the dp table, and selected items 
    return dp[n][capacity], dp, selected_items

# Reading input from file
filename = "example.txt"
capacity, items = parse_input(filename)

max_profit, table, selected = knapsack_01(capacity, items)

print("Maximum profit:", max_profit)
print("Selected items:", selected)

# Printing the DP table (uncomment the code below if you are using smalldatasets)
for row in table:
    print(row)
