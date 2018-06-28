import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
    public static boolean contains(int[] array, int n) {
        int low = 0, high = array.length - 1;
        while (low <= high){
            int mid = low + (high-low)/2;
            if (array[mid] == n)
                return true;    
            if (array[mid] < n)
                low = mid + 1;
            else
                high = mid - 1;
        }     
        return false;
    } 
}