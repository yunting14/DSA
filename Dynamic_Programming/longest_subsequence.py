def longest_subsequence(string1, string2):
    possible_commons = []
    common = ""
    string2_lastCommonIndex = 0
    for i in range(len(string1)):
        char1 = string1[i]
        found_common = False
        for k in range(string2_lastCommonIndex ,len(string2)):
            char2 = string2[k]
            if char1 == char2:
                string2_lastCommonIndex = k 
                common += char1
                found_common = True
                break
        if found_common == False:
            possible_commons.append(common)
            common = ""
            string2_lastCommonIndex = 0
        if i==len(string1)-1:
            possible_commons.append(common)
    
    if max(possible_commons) != "":
        return max(possible_commons)
    else:
        return ""
    
def longest_common_subsequence(text1,text2):

    # find the length of the strings
    m = len(text1)
    n = len(text2)

    # declaring the list for storing the dynamic programming values
    LCS = [[None]*(n+1) for i in range(m+1)]

    """Following steps build LCS[m+1][n+1] in bottom up fashion using dynamic programming principle
    Note: LCS[i][j] contains length of Longest Common Subsequence of text1[0..i-1] and text2[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                LCS[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j] , LCS[i][j-1])
    #print(LCS[m][n])

    # Following code is used to find out the LCS string using the LCS list created above
    o = LCS[m][n]

    # Create a list to store the characters of LCS string
    lcs_chars = [""] * (o)

    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in text1 and text2 are same, then
        # current character is part of LCS
        if text1[i-1] == text2[j-1]:
            lcs_chars[o-1] = text1[i-1]
            i-=1
            j-=1
            o-=1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif LCS[i-1][j] > LCS[i][j-1]:
            i-=1
        else:
            j-=1

    #Concatenate the characters in the list to form the LCS string
    lcs_str=""
    for char in lcs_chars:
        lcs_str+=char

    return lcs_str

# string1 = "AGGTAB"
# string2 = "GXTXAYB" 

# string1 = "ACA"
# string2 = "ADCE"

string1 = "BCDAACD"
string2 = "ACDBAC"
# print(longest_subsequence(string1, string2))
print(longest_common_subsequence(string1, string2))