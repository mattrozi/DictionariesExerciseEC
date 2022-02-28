
def main(): 

    outfile=open('book of John text.txt ','r')

    specificWords=outfile.read().split()

    john={}

    for i in range(len(specificWords)):
        john[specificWords[i]]=0

    for i in range(len(specificWords)):
        john[specificWords[i]]+=1



    print('Father:',john['Father'])
    print('God:',john['God'])
    print('Christ:',john['Christ'])
    print('Spriit',john['Spirit'])
    print('spriit',john['spirit'])
    print('life',john['life'])
    print('man',john['man'])
    outfile.close()


main()
