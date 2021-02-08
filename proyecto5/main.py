from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    for a in range(0,n):
        print(a*a)