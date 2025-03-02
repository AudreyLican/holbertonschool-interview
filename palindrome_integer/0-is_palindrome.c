#include "palindrome.h"

/**
 * is_palindrome - Checks if an unsigned long number is a palindrome.
 * @n: The number to check.
 *
 * Return: 1 if the number is a palindrome, 0 otherwise.
 */

int is_palindrome(unsigned long n) {
    unsigned long div = 1;
    unsigned long first_digit, last_digit;
    unsigned long temp = n;

    // find divisor to extract the fisrt digit
    while (temp >= 10)
    {
        div *= 10;
        temp /= 10;
    }

    // comapre digits from both ends
    while (n > 0)
    {
        first_digit = n / div; // extract 1st digit
        last_digit = n % 10; // extact last digit

        if (first_digit != last_digit)
            return (0); // not palindrome

        n = (n % div) / 10;
        div /= 100; // reduce div by 2 digits
    }

    return (1);
}
