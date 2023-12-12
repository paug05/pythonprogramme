# Übungszettel 6 Laufzeiten
#Paul Gnädig, Tim Duske


# #1a asymptotische Laufzeit von Insertionsort

# def insert(xs, i):    # Hilfsfunktion
#     key = xs[i]         # 1
#     j = i               #n 
#     while(j > 0 and xs[j-1] > key):
#         xs[j] = xs[j-1]
#         j -= 1
#     xs[j] = key 


# def insertion_sort(xs):
#     n = len(xs)             # 1
#     for i in range (1, n):
#         insert(xs,i)        # n
#     print(xs)

# # 1 + n - 2 + n * n 


# #1b.

def bauernmultiplikation(a,b):
    erg = 0
    i = 1
    while ( a> 0):
        if a % 2 == 1:
            print("hallo")
            erg = erg + b
        print(erg)
        a = a //2
        print("a ist jetzt:",a)
        b = b*2
        print("b ist jetzt:",b)
        i += 1
        print("Durchlauf:",i)

    return erg

print(bauernmultiplikation(17,121))


# #1c. 

# # list_sum =  1 + n +1 => Tn(n+2) => O (n)

# #sorted_zip =  1 + nlog n + n logn + n = 1 + 2* nlog(n) + n

# # bauernmulti = 1 + 


# #2b. Matrixsumme als Funktion

# # Spezifiaktion: matrix_summe(List[List[int]]): int
# #Voraussetzung: Jede zeile der Matrix beinhaltet die gleiche Anzahl an Elementen
# #Ergebnis: /
# #Effekt: Die Summe aller Elemente innerhalb der Matrix ist auf dem Bildschirm ausgegeben.
# '''Tests:
# 1. matrix_summe([[1,2,3],[0,0,1]]) == 7
# 2. matrix_summe([]) == 0
# 3. matrix_summe([[-2,3,4]],[0,0,-2]) == 3
# '''


# def matrix_summe(xs):
#     n = len(xs)             #1
#     if n < 1:
#         return 0
#     erg = 0                 #1
#     for i in range(n):          #n
#         for j in range(len(xs[i])):     #n
#             erg = erg + (xs[i][j])
            
#     print(erg)      #1


# # u = [[1,2,3],[3,4,5],[0,2,1]]

# # matrix_summe(u)

# print(matrix_summe([[1,2,3],[0,0,1]]) == 7)
# print(matrix_summe([]) == 0)
# print(matrix_summe([[-2,3,4],[0,0,-2]]) == 3)

# # tn(n) = 1 + 1 + n*n + 1 = n°2 +3


# #2c.) 

# # matrix_spec(List[List[int]]) : int
# # Voraussetzung: die einzelnen Listen sind aufsteigend sortiert und die Matrix besitzt maximal 2 verschiedene Elemente.
# # Ergebnis: /
# # Effekt: die Summe aller Listen innerhalb der Matrix ist auf dem Bildschirm ausgegeben. Falls die Matrix leer ist wird 0 augegeben
# '''Tests:
# 1. matrix_spec([[9,9],[8,8]]) == 34
# 2. matrix_spec([]) == 0
# 3. matrix_spec([[-2,-2]],[11,11]] == 18
# '''



# def matrix_spec(xs):
#     n = len(xs)