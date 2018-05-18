def menu():
    print()
    print('enter a list')
    print('predict the next element')
    print('quit')
    print()
def predict(L):
    return 42
def main():
    L = [30,10,20]
    while True:
        print('The list is',L)
        def menu():
          uc = input('choose the option')
          if uc == 9:
             break
          elif uc == 1:
              L = input('enter the list:')
          elif uc == 2:
              n = predict(L)
              L = L + [n]
          else:
              print(uc, 'thats not on the menu')
print()
print('see you yesterday')
print menu(L)
