class Solution {
    public void reverseString(char[] s) {
    int st = 0 ;
    int en = s.length-1;
    char temp;
    while(en>st){
    temp = s[st];
    s[st]= s[en];
    s[en]= temp;
    st++;
    en--;
    }

    }
}