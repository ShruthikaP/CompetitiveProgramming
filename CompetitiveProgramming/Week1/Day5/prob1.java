import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
    public static int findRotationPoint(String[] words) 
    {
       int l=words.length;
       int start=0;
       int end=l-1;
       int mid=start+(end-start)/2;
       return b_search(words,start,end,mid);
    }
    public static int b_search(String [] words, int start, int end, int mid){
        if (start>=end)
            return mid;
        if (words[mid].compareTo(words[end]) > 0){
            start=mid+1;
            mid=start+(end-start)/2;
            return b_search(words, start, end, mid);
        }
        if (words[mid].compareTo(words[start]) < 0){
            end=mid;
            mid=start+(end-start)/2;
            return b_search(words, start, end, mid);
        }
        throw new IllegalArgumentException();       
    }
}