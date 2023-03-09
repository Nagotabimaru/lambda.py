# 1 без лямбды
# def anti_vowel(text):
#    text = list(text)
#    for i in text[::-1]:
#        if i in 'aeiouAEIOU':
#           text.remove(i)
#    return str(''.join(text))
#
# print(anti_vowel('Hello world'))
# print(anti_vowel('Ah, Hello Mama'))
# print(anti_vowel('Hey look Words!'))
# print(anti_vowel('Hello Mia'))

# string = ['Ah, Hello Mama','Hello Mia','Hey look Words!']
# string_del = lambda lst:[string for string in string if 'aeiouAEIOU' in string]
# print(string_del(string))


# 2
# exit = lambda str:[str.isalpha()]
# print(exit("hjkhjkhu"))
#
# # так понятней )
# str1 = "hello"
# bool = str1.isalpha()
# print(bool)

# 3
# plus = lambda arr:arr[0] + plus(arr[1:]) if arr else 1
# print(plus([1,2,3,4,5,6]))

# 5
# a = lambda x: (x.replace('.', '', 1).replace('-', '', 1)).isnumeric()
#
# print(a(''))  #так false
# print(a('12')) #так true а как по другому сделать мозг не работает)


# 6
# по понятному
# n = int(input())
# factorial = 1
#
# for i in range(2, n + 1):
#     factorial *= i

# print(factorial)

#  по не понятному
# fact = lambda n:1 if n==0 else n*fact(n-1)
# print(fact(5))