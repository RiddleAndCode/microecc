/*
 * Galois/Counter Mode (GCM) and GMAC with AES
 *
 * Copyright (c) 2012, Jouni Malinen <j@w1.fi>
 *
 * This software may be distributed under the terms of the BSD license.
 * See README for more details.
 */

#include "uECC.h"
#include "unity.h"
#include <string.h>

void test_keys_shared_secret_secp160r1()
{
  const struct uECC_Curve_t *curve = uECC_secp160r1();

  uint8_t private1[21];
  uint8_t private2[21];

  uint8_t public1[40];
  uint8_t public2[40];

  uint8_t secret1[20];
  uint8_t secret2[20];

  TEST_ASSERT_NOT_EQUAL(uECC_make_key(public1, private1, curve), 0);
  TEST_ASSERT_NOT_EQUAL(uECC_make_key(public2, private2, curve), 0);

  TEST_ASSERT_NOT_EQUAL(uECC_shared_secret(public2, private1, secret1, curve), 0);
  TEST_ASSERT_NOT_EQUAL(uECC_shared_secret(public1, private2, secret2, curve), 0);

  TEST_ASSERT_EQUAL(memcmp(secret1, secret2, 20), 0);
}

int main(void)
{
  UNITY_BEGIN();
  RUN_TEST(test_keys_shared_secret_secp160r1);
  return UNITY_END();
}