def binary_tree_depth_order(tree):
	result = []
	if not tree:
		return result
	cur_depth_nodes = [tree]
	while cur_depth_nodes:
		result.append([curr.data for curr in cur_depth_nodes])
		cur_depth_nodes = [child for curr in cur_depth_nodes for child in(curr.left, curr.right) if child]

	return result

