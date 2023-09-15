def subsets(elements):
  if not elements:
    return [[]]
  
  first_ele = elements[0]
  remaining_eles = elements[1:]
  without_first_ele = subsets(remaining_eles)

  with_first_ele = []
  for val in without_first_ele:
    with_first_ele.append([first_ele, *val])

  return without_first_ele + with_first_ele

print(subsets(['a', 'b', 'c']))