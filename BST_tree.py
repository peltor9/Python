Node* insert(Node* node, int key)  
{      if (node == NULL)  				# 1. Perform the normal BST insertion 
        return(newNode(key));  
    if (key < node->key)  
        node->left = insert(node->left, key);  
    else if (key > node->key)  
        node->right = insert(node->right, key);  
    else 							# Equal keys are not allowed in BST  
        return node; 
       node->height = 1 + max(height(node->left),  	 # 2. Update height of this ancestor node 
                        height(node->right));  
 
   # 3. Get the balance factor of this ancestor node to check whether this node became unbalanced
    int balance = getBalance(node);  		# If this node becomes unbalanced, then  there are 4 cases

    if (balance > 1 && key < node->left->key)  	 # Left Left Case  
        return rightRotate(node);  

    if (balance < -1 && key > node->right->key)  	 # Right Right Case 
        return leftRotate(node);

    if (balance > 1 && key > node->left->key)  { 	    # Left Right Case 	   
        node->left = leftRotate(node->left);  
        return rightRotate(node);  	 } 

    if (balance < -1 && key < node->right->key)  {   	# Right Left Case   
        node->right = rightRotate(node->right);  
        return leftRotate(node);  	}  

        return node;  	} 		# return the (unchanged) node pointer 
