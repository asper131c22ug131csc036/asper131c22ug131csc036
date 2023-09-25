def linear_search_product(product_list, target_product):
  indices = []
  for i, product in enumerate(product_list):
    if product == target_product:
      indices.append(i)
  return indices


products = ["pen", "pencil", "pen", "eraser", "scale", "pen"]
target = "pen"
result = linear_search_product(products, target)
print(result)