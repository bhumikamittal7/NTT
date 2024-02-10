#ifndef ZMOD_H
#define ZMOD_H

#include <stdint.h>
#include "params.h"
#include "poly.h"

typedef struct {
  int32_t coeffs[LDASH];
} zmodq_matrix;


void uniform_zmodq_elements(zmodq_matrix* A, int row, int col);



#endif
