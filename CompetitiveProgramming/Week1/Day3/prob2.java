 import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static class BinaryTreeNode {

        public int value;
        public BinaryTreeNode left;
        public BinaryTreeNode right;

        public BinaryTreeNode(int value) {
            this.value = value;
        }

        public BinaryTreeNode insertLeft(int leftValue) {
            this.left = new BinaryTreeNode(leftValue);
            return this.left;
        }

        public BinaryTreeNode insertRight(int rightValue) {
            this.right = new BinaryTreeNode(rightValue);
            return this.right;
        }
    }

public static boolean isBalanced(BinaryTreeNode root) {
int lh; 
int rh; 
if (root == null)
return true;
lh = height(root.left);
rh = height(root.right);
if (Math.abs(lh - rh) <= 1
&& isBalanced(root.left)
&& isBalanced(root.right))
return true;
return false;
}
static int height(BinaryTreeNode node) 
{
if (node == null)
return 0;
return 1 + Math.max(height(node.left), height(node.right));
        
    }
}