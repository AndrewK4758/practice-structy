def create_combinations(items, k):
  if k == 0:
    return [[]]
  if k > len(items):
    return []
  
  first_ele = items[0]
  with_first_ele = []

  for val in create_combinations(items[1:], k-1):
    with_first_ele.append([first_ele, *val])
  
  without_first_ele = create_combinations(items[1:], k)

  return with_first_ele + without_first_ele
  
print(create_combinations(["a", "b", "c"], 2))