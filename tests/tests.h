#ifndef _UECC_TESTS_H_
#define _UECC_TESTS_H_

#include "uECC.h"
#include "unity.h"
#include <stdio.h>
#include <string.h>


void vli_print(char *str, uint8_t *vli, unsigned int size);
void test_ecdsa(void);
void test_ecdh(void);
void test_compress(void);
void test_compute(void);

#endif //_UECC_TESTS_H_
