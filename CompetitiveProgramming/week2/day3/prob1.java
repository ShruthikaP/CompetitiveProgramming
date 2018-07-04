import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
    public static class LinkedListNode {
        public int data;
        public LinkedListNode next;
        public LinkedListNode(int data) {
            this.data = data;
        }
    }
    public static LinkedListNode reverse(LinkedListNode headOfList) {
        LinkedListNode prev = null;
        LinkedListNode current = headOfList;
        LinkedListNode next = null;
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        headOfList = prev;
        return headOfList;
    }