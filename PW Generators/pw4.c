#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void generate_password(char* password, int password_length, char* choices, int* choices_length)
{
    char side;
    printf("Which side of the keyboard do you want the keys to be from? (left/right) ");
    scanf(" %c", &side);

    char lower[26] = "abcdefghijklmnopqrstuvwxyz";
    char upper[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char numeric[10] = "0123456789";
    char symbols[33] = "!@#$%^&*()-_=+[]{}\\|;:\'\",.<>/?";

    char include;
    printf("Include lowercase letters in the password? (y/n) ");
    scanf(" %c", &include);
    if (include == 'y') 
    {
        strncat(choices, lower, sizeof(lower));
        *choices_length += sizeof(lower);
    }

    printf("Include uppercase letters in the password? (y/n) ");
    scanf(" %c", &include);
    if (include == 'y') 
    {
        strncat(choices, upper, sizeof(upper));
        *choices_length += sizeof(upper);
    }

    printf("Include numbers in the password? (y/n) ");
    scanf(" %c", &include);
    if (include == 'y') 
    {
        strncat(choices, numeric, sizeof(numeric));
        *choices_length += sizeof(numeric);
    }

    printf("Include symbols in the password? (y/n) ");
    scanf(" %c", &include);
    if (include == 'y') 
    {
        strncat(choices, symbols, sizeof(symbols));
        *choices_length += sizeof(symbols);
    }

    char left_keys[] = "qwertasdfgzxcvb12345!@#$%QWERASDFGZXCVB";
    char right_keys[] = "yuiophjklnmYUIOPHJKLNM67890^&*()-_=+[]{};:\'\",.<>/?";

    if (side == 'left') 
    {
        for (int i = 0; i < *choices_length; i++) 
        {
            if (strpbrk(left_keys, &choices[i]) == NULL) 
            {
                choices[i] = '\0';
            }
        }
    } else if (side == 'right') 
    {
        for (int i = 0; i < *choices_length; i++) 
        {
            if (strpbrk(right_keys, &choices[i]) == NULL) 
            {
                choices[i] = '\0';
            }
        }
    }

    int new_length = 0;
    for (int i = 0; i < *choices_length; i++) {
        if (choices[i] != '\0') {
            choices[new_length++] = choices[i];
        }
    }
    *choices_length = new_length;

    if (password_length > *choices_length) {
        printf("Error: password length is greater than the number of available characters.\n");
        return;
    }

    for (int i = 0; i < password_length; i++) {
        int random_index = rand() % *choices_length;
        password[i] = choices[random_index];
    }
}

int main() {
    srand(time(0));
    char password[100];
    char choices[100] = "";
    int choices_length = 0;

    while (1) {
        generate_password(password, 8, choices, &choices_length);
        printf("Your password is: %s\n", password);

        char again;
        printf("Generate another password? (y/n) ");
        scanf(" %c", &again);

        if (again != 'y') {
            break;
        }
    }
    printf("Goodbye!");
    return 0;
}
