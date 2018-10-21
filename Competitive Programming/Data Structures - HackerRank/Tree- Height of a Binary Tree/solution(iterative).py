def height(node):
    if node is None:
        return 0
    q = [] 
      
    # Enqueue Root and Initialize Height  
    q.append(node) 
    height = -1
    while(True): 
          
        # nodeCount(queue size) indicates number of nodes 
        # at current level 
        nodeCount = len(q) 
        if nodeCount == 0 : 
            return height  
      
        height += 1 
  
        # Dequeue all nodes of current level and Enqueue 
        # all nodes of next level 
        while(nodeCount > 0): 
            node = q[0] 
            q.pop(0) 
            if node.left is not None: 
                q.append(node.left) 
            if node.right is not None: 
                q.append(node.right) 
  
            nodeCount -= 1
