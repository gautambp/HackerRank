// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-bigdecimal/problem


        //Write your code here
        ArrayList<String> ts = new ArrayList<String>();
        for (int i=0; i<n; i++) ts.add(s[i]);
        ts.sort(new Comparator<String>() {

            @Override
            public int compare(String o1, String o2) {
                return new BigDecimal(o2).compareTo(new BigDecimal(o1));
            }
            
        });
        s = ts.toArray(s);

