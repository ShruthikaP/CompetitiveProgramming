import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
   public static int findDup(int[] a) {
       for (int i = 0; i <a.length; i++){
           if (a[Math.abs(a[i])] >= 0)
               a[Math.abs(a[i])] = -a[Math.abs(a[i])];
           else
               return Math.abs(a[i]);
       }    
       return 0;
   } 