digits = "23"

phoneDict = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], 
             "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'],
             "8": ['t', 'u', 'v'], "9": ["w", "x", "y", "z"]}

res = []

def dfs(cur, path):
    if len(path) == len(digits):
        res.append([path])

    for i in cur:
        dict = phoneDict[i]
        for x in dict:
            dfs(cur[i+1:], path + str(x))


dfs(digits, "")