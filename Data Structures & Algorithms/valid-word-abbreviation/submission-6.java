class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {       int i = 0;
        int j = 0;
        int m = word.length();
        int n = abbr.length();
        
        while (i < m && j < n) {
            char ch = abbr.charAt(j);
            
            if (Character.isDigit(ch)) {
                if (ch == '0') {
                    return false;
                }
                
                int num = 0;
                while (j < n && Character.isDigit(abbr.charAt(j))) {
                    num = num * 10 + (abbr.charAt(j) - '0');
                    j++;
                }
                
                i += num;
            } else {
                if (word.charAt(i) != ch) {
                    return false;
                }
                i++;
                j++;
            }
        }
        return i == m && j == n;
        
    }
}