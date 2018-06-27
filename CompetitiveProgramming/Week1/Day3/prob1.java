import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
    public static class BinaryTreeNode {
        public int x;
        public BinaryTreeNode left;
        public BinaryTreeNode right;
        public BinaryTreeNode(int x) {
            this.x = x;
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
public static boolean isBinarySearchTree(BinaryTreeNode root) {
       int min=Integer.MIN_VALUE;
       int max=Integer.MAX_VALUE;
       return check(root,min,max);
   }
   public static boolean check(BinaryTreeNode r,int min,int max){
       if(r==null) return true;
       if(r.x<=min || r.x>max) return false;
       return check(r.left,min,r.x) && check(r.right,r.x,max);
   }
}