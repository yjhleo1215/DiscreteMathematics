def getDet(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(n):
        sub = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * getDet(sub)
    return det

def getCM(matrix):
    n = len(matrix)
    if n == 1:
        return [[1]]
    cm = []
    for i in range(n):
        row_c = []
        for j in range(n):
            sub = [row[:j] + row[j+1:] for idx, row in enumerate(matrix) if idx != i]
            val = ((-1) ** (i + j)) * getDet(sub)
            row_c.append(val)
        cm.append(row_c)
    return cm

def getAdj(matrix):
    cm = getCM(matrix)
    n = len(matrix)
    adj = [[cm[j][i] for j in range(n)] for i in range(n)]
    return adj

def getInverseByDet(matrix):
    det = getDet(matrix)
    if det == 0:
        return print("행렬식이 0이므로 역행렬이 존재하지 않습니다.")
    adj = getAdj(matrix)
    n = len(matrix)
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]
    return inv

def getInverseByGaussJordan(matrix):
    det = getDet(matrix)
    if det == 0:
        print("행렬식이 0이므로 역행렬이 존재하지 않습니다.")
        return None

    n = len(matrix)
    aug = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        pivot = aug[i][i]
        if pivot == 0:
            swap_row = i
            for r in range(i + 1, n):
                if aug[r][i] != 0:
                    swap_row = r
                    break
            aug[i], aug[swap_row] = aug[swap_row], aug[i]
            pivot = aug[i][i]

        for j in range(2 * n):
            aug[i][j] /= pivot

        for r in range(n):
            if r != i:
                factor = aug[r][i]
                for j in range(2 * n):
                    aug[r][j] -= factor * aug[i][j]

    inv = [row[n:] for row in aug]
    return inv

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:8.2f}" for val in row))

def compareMatrixs(m1, m2):
    n = len(m1)
    for i in range(n):
        for j in range(n):
            if round(m1[i][j], 2) != round(m2[i][j], 2): # 조건 수정
                return False
    return True

def main():
    n = int(input("정방행렬의 차수를 입력하세요: "))
    a = []
    for i in range(1, n+1):
        row_input = list(map(float, input(f"{i}행: ").split()))
        a.append(row_input)   
    print()
    
    # 행렬식을 이용한 역행렬 계산     
    print("행렬식 으로 구한 역행렬:")
    inv_det = getInverseByDet(a)
    printMatrix(inv_det)
    
    print()
    
    # 가우스-조던 소거법으로 구한 역행렬 계산
    print("가우스-조던 소거법으로 구한 역행렬:")
    inv_gj = getInverseByGaussJordan(a)
    printMatrix(inv_gj)
    
    print()
    
    # 3. 결과 비교
    if compareMatrixs(inv_det, inv_gj):
        print("두 방법의 결과가 동일합니다.")
    else:
        print("두 방법의 결과가 다릅니다.")

if __name__ == "__main__":
    main()