# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/nested-lists/problem
if __name__ == '__main__':
    st_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st_dict[name] = score
    st = set()
    low_score = 100
    sec_low_score = 100
    for n in st_dict:
        if st_dict[n] < low_score:
            sec_low_score = low_score
            low_score = st_dict[n]
        elif st_dict[n] != low_score and st_dict[n] < sec_low_score:
            sec_low_score = st_dict[n]
    for n in st_dict:
        if st_dict[n] == sec_low_score:
            st.add(n)    
    for s in st:
        print(s)

