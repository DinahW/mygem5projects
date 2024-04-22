import numpy as np

def gemm_with_blocks(matrixA, matrixB, block_size):
    # Dimensions of matrices A and B
    m, k = matrixA.shape
    _, n = matrixB.shape
    
    # Initialize the result matrix C with zeros
    resultMatrix = np.zeros((m, n))
    
    # Iterate over blocks
    for i in range(0, m, block_size):
        for j in range(0, n, block_size):
            for x in range(0, k, block_size):
                # Compute the range for the current block
                i_end = min(i + block_size, m)
                j_end = min(j + block_size, n)
                x_end = min(x + block_size, k)
                
                # Perform GEMM operation for the current block
                resultMatrix[i:i_end, j:j_end] += np.dot(matrixA[i:i_end, x:x_end], matrixB[x:x_end, j:j_end])
    
    return resultMatrix

# Example matrices A and B
matrixA = np.random.rand(1024, 1024)
matrixB = np.random.rand(1024, 1024)

# Block size
block_size = 64

# Perform the GEMM operation with blocks
resultMatrix = gemm_with_blocks(matrixA, matrixB, block_size)

# Print the shape of the result matrix
print("Shape of result matrix:", resultMatrix.shape)


print("Top-left portion of the result matrix:")
print(resultMatrix[:20, :20])
