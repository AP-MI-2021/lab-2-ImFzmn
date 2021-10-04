def is_palindrome(n):
    x=n
    a=0
    print(x)
    while x!=0:
        a=a*10+x%10
        x=x//10

    if a==n:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(5) is True
    assert is_palindrome(4564) is False
    assert is_palindrome (123321) is True
    assert is_palindrome(5323533) is False

def prim(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def is_superprime(n):
    while n!=0:
        if prim(n)==False:
            return False
        n=n//10
    return True

def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(222) is False
    assert is_superprime(293) is True

def main():
    print("Alegeti optiunea:\n"
          "1.Testati daca un nr este palindrom\n"
          "2.Testati daca un nr este superprim\n")
    n=int(input())
    if n==1:
        x=int(input("Ce numar vreti sa testati?\n"))
        print(is_palindrome(x))
    elif n==2:
        x = int(input("Ce numar vreti sa testati?\n"))
        print(is_superprime(x))
    else:
        print("Ati ales un numar incorect , tastati din nou\n")
        main()

main()





