public class Solution {
    public String reverseWords(String string) {
        int j = 0;
        char [] str = string.toCharArray();

        for (int i = 0 ; i<str.length;i++){
            if (str[i]==' '){
                reverse (str, j, i-1);
                j = i+1;
            }
        }
         reverse (str, j, str.length-1);
        return new String (str);
        
    }
    public void reverse (char []s, int l, int r) {
     while(l < r)
	{
		char temp = s[l];
		s[l] = s[r];
		s[r] = temp;
		l++; r--;
	}
    }
}