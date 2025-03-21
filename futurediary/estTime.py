import sys 

def estReadTime(content,wpm=200):
    words=content.split()
    time=len(words)/wpm 
    return time if time > 1 else "less than 1 min"

if __name__=="__main__":
    if len(sys.argv)>1:
        with open(sys.argv[1],"r",encoding="UTF-8") as file:
            content=file.read()

        print(f"Time req: {estReadTime(content)} mins")

    else:
        print("Usage: python estTime.py <filename>")
