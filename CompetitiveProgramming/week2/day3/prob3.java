import java.util.Arrays;
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
public class Solution {
	public static char[] reverse(char[] arrayOfChars) {
  		for(int i = 0, j = arrayOfChars.length- 1; i < arrayOfChars.length/2; i++, j--) {
    	char c = arrayOfChars[i];
    	arrayOfChars[i] = arrayOfChars[j];
    	arrayOfChars[j] = c;
  	}
  	return arrayOfChars;
}