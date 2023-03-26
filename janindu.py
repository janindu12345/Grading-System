Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0

data_list = []

while True:
    try:
        passs = int(input('Please enter your credits at pass: '))
        if passs in range (0,121,20):
            defer = int(input('Please enter your credit at defer: '))
            if defer in range (0,121,20):
                fail = int(input('Please enter your credit at fail : '))
                if fail in range (0,121,20):
                    if passs + defer + fail == 120:
                        if passs == 120:
                            print('Progress.')
                            print(' ')
                            Progress = Progress + 1
                            data_list.append(['Progress - ',passs, defer, fail])
                        elif passs == 100:
                            print('Progress (module trailer)')
                            print(' ')
                            Trailer = Trailer + 1
                            data_list.append(['Progress (module trailer) - ',passs, defer, fail])
                        elif (passs == 80 or passs == 60 or passs == 40 or passs == 20 or passs == 0)  and (defer == 0 or defer == 20 or defer == 40 or defer == 60 or defer == 80 or defer == 100 or defer == 120) and (fail == 0 or fail == 20 or fail == 40 or fail == 60):
                            print('Do not Progress – module retriever')
                            print(' ')
                            Retriever = Retriever + 1
                            data_list.append(['module retriever - ',passs, defer, fail])
                        elif (passs == 0 or passs == 20 or passs == 40) and (defer == 0 or defer == 20 or defer == 40) and (fail == 80 or fail == 100 or fail == 120):
                            print('Exclude')
                            print(' ')
                            Excluded = Excluded + 1
                            data_list.append(['Exclude - ',passs, defer, fail])
                    else:
                        print('Total incorrect.')
                else:
                    print('Out of range.')               
            else:
                print('Out of range.')
        else:
            print('Out of range.')
    except:                                                                                                                                                                                
        print('Integer required')
        continue 

    print('Would you like to enter another set of data?')
    another_data = input('Enter \'y\' for yes or \'q\' to quit and view results: ')
    another_data = another_data.lower()
    print('')
    if another_data == 'y':
        continue
    break


print("--------------------------------------------------------------------------")
print('Horizontal Histogram ')
print('Progress', Progress, ' :', Progress * '*')
print('Trailer', Trailer, '  :', Trailer * '*')
print('Retriever', Retriever, ':', Retriever * '*')
print('Excluded', Excluded, ' :', Excluded * '*')
print(' ')
print(int(Progress + Trailer + Retriever + Excluded), 'outcomes in total.')

print("--------------------------------------------------------------------------")

#part2
print('Progress   Trailing   Retriever   Excluded')

for i in range(max(Progress , Trailer , Retriever , Excluded)):

    if (i < Progress):
        print("   *", end=' ')
    else:
        print("  ", end=' ')

    if (i < Trailer):
        print("\t       *", end=' ')
    else:
        print("\t\t", end=' ')

    if (i < Retriever):
        print("\t  *", end=' ')
    else:
        print("\t", end=' ')

    if (i < Excluded):
        print("\t     *", end=' ')
    else:
        print("\t\t", end=' ')

    print()


for count in data_list:
    print(f'{count[0]} {count[1]}, {count[2]}, {count[3]}')    

#part4
file = open('textfile.txt', 'w')
file.write(f'{count[0]} {count[1]}, {count[2]}, {count[3]}')
file.flush()
file.close()

