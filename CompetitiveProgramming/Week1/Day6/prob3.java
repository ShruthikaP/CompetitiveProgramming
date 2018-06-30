import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
import java.util.*;
public class Solution{
    public static class MaxStack{
    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> s2 = new Stack<>();
    public void push(int item) {
        s1.push(item);
        if (s2.empty() || item >= s2.peek()) {
            s2.push(item);
        }
    }
    public int pop(){
        int item = s1.pop();
        if (item == s2.peek()) {
            s2.pop();
        }
        return item;
    }
    public int getMax(){
        return s2.peek();
    }
}
}