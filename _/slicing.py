def slice(txt, n):
    return [txt[i:i+n] for i in range(0, len(txt), n)]
    
if __name__ == "__main__":
    for i in slice(input("text: "), int(input("number: "))):
        print(i)