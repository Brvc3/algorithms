def main():
    raw = list(input().rstrip())
    for i in range(len(raw)-1,-1,-1):
        print(raw[i],end='')

if __name__ == '__main__':
    main()