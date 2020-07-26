def main():
	matriz = generar_matriz()
	generar_sudoku(matriz)
	for i in range (9):
		print(matriz[i])

def generar_matriz():
	archivo = input("Ingrese el archivo con los datos iniciales: ")
	matriz = []
	with open(archivo,'r') as f:
		for i in range (9):
			fila = f.readline()
			fila = fila.split()
			for j in range(9):
				fila[j] = int (fila[j])
			matriz.append(fila)
	return matriz

def generar_sudoku(matriz):
	if matriz_llena(matriz):
		return True
	pos = buscar_pos_libre(matriz)
	for x in range (1,10):
		if solucion_parcial(matriz,pos[0],pos[1],x):
			matriz[pos[0]][pos[1]] = x
			if generar_sudoku(matriz) == True:
				return True
	matriz[pos[0]][pos[1]] = 0
	return False

def matriz_llena(matriz):
	for i in range (9):
		for j in range (9):
			if matriz[i][j] == 0:
				return False
	return True

def buscar_pos_libre(matriz):
	for i in range (9):
		for j in range (9):
			if matriz[i][j] == 0:
				return (i,j)
	return False

def solucion_parcial(matriz,fila,columna,valor):
	for i in range (9):
		if i == fila:
			continue
		if matriz[i][columna] == valor:
			return False
	for j in range (9):
		if j == columna:
			continue
		if matriz[fila][j] == valor:
			return False
	fila_inicial = fila - fila%3
	columna_inicial = columna - columna%3
	for i in range (fila_inicial,fila_inicial+3):
		for j in range (columna_inicial,columna_inicial+3):
			if (i,j) == (fila,columna):
				continue
			if matriz[i][j] == valor:
				return False
	return True
    
main()