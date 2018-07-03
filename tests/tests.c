/*
 * Galois/Counter Mode (GCM) and GMAC with AES
 *
 * Copyright (c) 2012, Jouni Malinen <j@w1.fi>
 *
 * This software may be distributed under the terms of the BSD license.
 * See README for more details.
 */


#include "tests.h"

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_ecdh);
  RUN_TEST(test_ecdsa);
  RUN_TEST(test_compress);
  RUN_TEST(test_compute);
  return UNITY_END();
}