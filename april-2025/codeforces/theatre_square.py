def theatre_square(n: int,m: int,a: int) -> int:
    # second = -(m//-a)
    return -(n//-a) * -(m //-a)
  

if __name__ == '__main__':
    n, m, a = map(int, input().split())
    print(theatre_square(n,m,a))


# print(theatre_square(6,6,4))
# print(theatre_square(5,5,3))
