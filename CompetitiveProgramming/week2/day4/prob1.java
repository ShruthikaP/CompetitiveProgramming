import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
    public static boolean hasPalindromePermutation(String s) { 
        int[] a = new int[128];
        for (int i = 0; i < s.length(); i++) {
            a[s.charAt(i)]++;
        }
        int c = 0;
        for (int j = 0; j < a.length && c <= 1; j++) {
            c += a[j] % 2;
        }
         if (c > 1)
        return false;
    }
 return true;
}