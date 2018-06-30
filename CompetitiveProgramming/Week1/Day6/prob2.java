import java.util.Stack;
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution{
    public static class QueueTwoStacks{
        private Stack<Integer> s1 = new Stack<>();
        private Stack<Integer> s2 = new Stack<>();
        public void enqueue(int item){
            s1.push(item);
        }
        public int dequeue(){
        if (s2.isEmpty()){
            while (!s1.isEmpty()){
               s2.push(s1.pop());
            }
        }
        return s2.pop();
        }
    }
}