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
	public static int findLargest(BinaryTreeNode root){
		 BinaryTreeNode current=root;
		 while(current.right!=null){
			current=current.right;
		 }
		 return current.value;
	}
	public static int findSecondLargest(BinaryTreeNode root) {
		 if(root==null || (root.left==null && root.right==null)){
			 throw new IllegalArgumentException("Tree must have at least 2 nodes");
		 }
		 BinaryTreeNode current= root;
		 while(true){
			 if(current.left!=null && current.right==null)
		 		return findLargest(current.left);
		 	 if(current.right!=null && current.right.left==null && current.right.right==null)
		 		return current.value;
		  	current=current.right;
		 }
	 }
}