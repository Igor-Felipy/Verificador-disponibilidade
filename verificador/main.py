from time import sleep
import verify


while True:
    menu = str(input('Unique verification [U] \nContinuous verification [C] \nCheck and save to file [S] \nHelp [H] \nQuit [Q] \n'))

    if menu.upper() == 'U':
        try:
            url = verify.url_clean(input('Which site to check? '))
            print(verify.verify(url))
            print('\n\n')
        except:
            print('Error')


    elif menu.upper() == 'C':
        url = verify.url_clean(input('Which site to check? '))
        time = int(input('How often? (seconds)'))
        while True:
            try:
                print(verify.verify(url))
            except:
                print('Error')
                break
            sleep(time)
            

    elif menu.upper() == 'S':
        url = verify.url_clean(input('Which site to check? '))
        time = int(input('How often? (seconds)'))
        arch = str(input('What do you want to name the file?') + '.txt')
        while True:
            try:
                with open(arch, 'a') as archive:
                    print(str(verify.verify(url) + '\n'))
            except:
                print('Error')
                break
                sleep(time)
                


    elif menu.upper() == 'H':
        print('Consult the documentation in https://github.com/Igor-Felipy/Verificador-disponibilidade')


    elif menu.upper() == 'Q':
        print('Byeee....')
        break

    else:
        print('Invalid Option!!')