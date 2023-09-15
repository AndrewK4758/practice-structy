import pprint as pp
def permutations(items):
  if len(items) == 0:
    return [[]]
  
  first_item = items[0]
  all_perms_list = []
  for perm in permutations(items[1:]):
    for i in range(len(perm) + 1):
      all_perms_list.append(perm[:i] + [first_item] + perm[i:])
  return all_perms_list
  

pp.pprint(permutations(['a', 'b', 'c', 'd', 'e']))