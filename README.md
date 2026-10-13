# Notes :
Program ini mengimplementasikan algoritma A* search untuk menyelesaikan masalah tower of hanoi. 

Dengan initial state:
A = [3,2,1] 
B = [] 
C = [] 
goal state: 
A = [] 
B = [] 
C = [3,2,1].

Rumus dari A* : 
f(n) = g(n) + h(n)
Keterangan: 
g(n) = cost atau jumlah langkah yang telah dilakukan dari state awal.
h(n) = heuristic yang digunakan untuk memperkirakan jarak suatu state terhadap goal state.
f(n) = nilai evaluasi yang digunakan untuk menentukan state yang akan dieksplorasi terlebih dahulu.

Jadi, pada program ini, nilai heuristicnya dihitung berdasarkan jumlah disk yang belum mencapai gagang C. Semakin kecil nilai heuristic, semakin dekat state tersebut dengan goal state.
