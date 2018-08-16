# Python wrapper around microecc library

## compile **test.c**

```shell
$ cc -fPIC -shared -o libtest.so test.c
```

The compiled version of microECC (_libmicroecc.so_) was given to me by Diogo.

## execute **test.py**

```shell
$ python test.py
```

That's the *C* definition of _uECC_Curve_t_

```c
/* ------------------------------ */
/* uECC_Curve definition (C code) */
/* ------------------------------ */

typedef int8_t wordcount_t;
typedef int16_t bitcount_t;

typedef uint8_t uECC_word_t;

struct uECC_Curve_t {
  wordcount_t num_words;
  wordcount_t num_bytes;
  bitcount_t num_n_bits;
  uECC_word_t p[uECC_MAX_WORDS];
  uECC_word_t n[uECC_MAX_WORDS];
  uECC_word_t G[uECC_MAX_WORDS * 2];
  uECC_word_t b[uECC_MAX_WORDS];
  void (*double_jacobian)(uECC_word_t *X1,
                          uECC_word_t *Y1,
                          uECC_word_t *Z1,
                          uECC_Curve curve);
#if uECC_SUPPORT_COMPRESSED_POINT
  void (*mod_sqrt)(uECC_word_t *a, uECC_Curve curve);
#endif
  void (*x_side)(uECC_word_t *result, const uECC_word_t *x, uECC_Curve curve);
#if (uECC_OPTIMIZATION_LEVEL > 0)
  void (*mmod_fast)(uECC_word_t *result, uECC_word_t *product);
#endif
};
```

That's the definition of the same code in *Python*

```python
# "uECC_Curve" fields definition
uECC_Curve._fields_ = [
    ('num_words', ctypes.c_int8),
    ('num_bytes', ctypes.c_int8),
    ('num_n_bits', ctypes.c_int),
    ('p', ctypes.c_uint * 4),  # 4 = uECC_MAX_WORDS
    ('n', ctypes.c_uint * 4),  # 4 = uECC_MAX_WORDS
    ('G', ctypes.c_uint * 4),  # 4 = uECC_MAX_WORDS
    ('b', ctypes.c_uint * 4),  # 4 = uECC_MAX_WORDS
    ('double_jacobian', _double_jacobian),  # function
    ('mod_sqrt', _mod_sqrt),  # function
    ('x_side', _x_side),  # function
    ('mmod_fast', _mmod_fast),  # function
]
```

If you execute the *Python* code (_test.py_) you can see the error comes up when I'm trying to define the functions (line 127 of _test.py_). Those functions (_double_jacobian_, _mod_sqrt_, _x_side_, _mmod_fast_) all return *void*.
