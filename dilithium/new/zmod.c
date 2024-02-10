#include <stdint.h>
#include "params.h"
#include "zmod.h"


/*************************************************
* Name:        uniform_zmodq_elements
*
* Description: Sample uniformly random coefficients in [0, Q-1] from a given matrix
*
* Arguments:  - zmodq_matrix* A: pointer to the matrix to be filled
*             - row: number of rows of the matrix
*             - col: number of columns of the matrix
*             
* Returns a matrix A with uniformly random coefficients in [0, Q-1]
**************************************************/
void uniform_zmodq_elements(zmodq_matrix* A, int row, int col) {
  int i, j;
  for(i = 0; i < row; i++) {
    for(j = 0; j < col; j++) {
      A[i].coeffs[j] = randombytes(4);
    }
  }
}

/*************************************************
* Name:        cof_poly
*
* Description: Extract the coefficients of a polynomial and write them in a vector like  [[a0], [a1], [a2], ... , [an-1]] for a polynomial a0 + a1*x + a2*x^2 + ... + an-1*x^(n-1)
*
* Arguments:  - poly a: the polynomial
*             - n: the number of coefficients of the polynomial
*             
* Returns a vector with the coefficients of the polynomial
**************************************************/
int32_t** cof_poly(poly a, int n) {
    int32_t** v = (int32_t**)malloc(n * sizeof(int32_t*));
    for(int i = 0; i < n; i++) {
        v[i] = (int32_t*)malloc(sizeof(int32_t));
        v[i][0] = a.coeffs[i];
    }
    return v;
}


