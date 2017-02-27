#!/usr/bin/python

from numpy import array
# construir a funcao que ordena a lista
# se tiver caso de fragmentacao
#   chama a lista restante para ordenar nos elementos dela usando a mesma funcao
#   se tiver sobra nela, chamar novamente



def orderarraydifferentsizes(arraynuminput, arraynumoutput, slice):


    sizelist = len(arraynuminput)
    sizecomparison = sizelist - slice
    sizecomparisonright = sizelist - slice
    i = 0
    j = 0

    for kint in range(0, sizecomparison+sizecomparisonright ,1):
        #            se j esta estourado e i nao
        #                atribui i direto
        if (i < sizecomparison  and j >= sizecomparisonright):
            arraynumoutput[kint+slice] = arraynuminput[slice+i]
            i += 1
            continue
        #            se i esta estourado e j nao
        #                atribui j direto
        if (j < sizecomparisonright  and i>= sizecomparison):
            arraynumoutput[kint+slice] = arraynuminput[slice+sizecomparison+j]
            j += 1
            continue

        if (arraynuminput[slice+i] < arraynuminput[slice+sizecomparison+j]):
            arraynumoutput[kint+slice] = arraynuminput[slice+i]
            i += 1
            continue

        if (arraynuminput[slice+i] > arraynuminput[slice+sizecomparison+j]):
            arraynumoutput[kint+slice] = arraynuminput[slice+(sizecomparison)+j]
            j += 1
            continue




def orderarray(arraynuminput, arraynumoutput, orderstart = 0):
    #    sizelist = len(numberlist)
    sizelist = len(arraynuminput)
    sizecomparison = 2 #sliced n
    numbercomparison = 0

    i = 0
    j = 0
    slice = 0
    kout = 0
    kint = 0

    doitagain = False   #essa variavel vai controlar se o algoritmo tem de ser executado mais uma vez porque
    #sobraram elementos nao analisados




    while sizecomparison <= sizelist or doitagain:
        comparisons = sizelist / sizecomparison

        while kout < comparisons or doitagain:

            if doitagain:
                orderarray(arraynuminput,arraynumoutput,slice)
                orderarraydifferentsizes(arraynuminput,arraynumoutput,slice)

            else:
                for kint in range(0, sizecomparison ,1):
                    #            se j esta estourado e i nao
                    #                atribui i direto
                    if (i < sizecomparison / 2 and j >= sizecomparison / 2 ):
                        arraynumoutput[kint+slice] = arraynuminput[slice+i]
                        i += 1
                        continue
                    #            se i esta estourado e j nao
                    #                atribui j direto
                    if (j <= sizecomparison / 2 and i>= sizecomparison /2):
                        arraynumoutput[kint+slice] = arraynuminput[slice+(sizecomparison/2)+j]
                        j += 1
                        continue

                    if (arraynuminput[slice+i] < arraynuminput[slice+(sizecomparison/2)+j]):
                        arraynumoutput[kint+slice] = arraynuminput[slice+i]
                        i += 1
                        continue

                    if (arraynuminput[slice+i] > arraynuminput[slice+(sizecomparison/2)+j]):
                        arraynumoutput[kint+slice] = arraynuminput[slice+(sizecomparison/2)+j]
                        j += 1
                        continue
                i = 0
                j = 0
                slice += sizecomparison
                kout += 1

        kout = 0

        arraynuminput = array(arraynumoutput,copy=True)
        sizecomparison *= 2 #essa variavel foi criada para saber o tamanho da lista maior que esta sendo comparada
        #tem de fazer as quantidades que nao sao potencias de 2 darem certo com a variavel sendo incrementada por potencia
        #de 2
        #    sizecomparison += 2

        if slice < sizelist: #significa que tem elementos sobrando na lista e que a quantidade dela nao e potencia de 2
            doitagain = True
            sizecomparisonright = sizelist - slice #numero de posicoes que sobraram do lado direito
            sizecomparison /= 2 #sizecomparison tem de voltar a ter o valor anterior
        else:
            doitagain = False
            slice = 0


        print"imprimindo o array de inteiros de saida"
        print arraynumoutput






def orderlist(numberlist):
    arraynuminput = array(numberlist, dtype = 'L')
    arraynumoutput = array(numberlist, dtype = 'L')

    print"imprimindo o array de inteiros de entrada"
    print arraynuminput

    orderarray(arraynuminput, arraynumoutput)

    return arraynumoutput


