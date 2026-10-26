# 1. Start with this list
shopping = ["bread", "milk", "sugar"]
print("Start:", shopping)

# 2. Add "eggs" to the end
shopping.append("eggs")

# 3. Change "sugar" to "honey" -> sugar is at index 2
shopping[2] = "honey"

# 4. Remove "bread"
shopping.remove("bread")

# 5. Print the 2nd item (index 1, because we start counting at 0)
print("The 2nd item is:", shopping[1])

# 6. How many items left?
print("Total items:", len(shopping))
print("Final list:", shopping)