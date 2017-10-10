def main():
    palindrome = str(raw_input("Please enter a string to check to see if its a palindrome: "))
    reversedPalindrome = palindrome [:: -1]

    for i in range(0, len(palindrome)):
        if (palindrome[i] != reversedPalindrome[i]):
            print("Not palindrome")
            break
        if(i == len(palindrome) -1):
            print("Palindrome")
                       

main()
