// DD Period 7 Financial Calculator

#include <stdio.h>

int main(void){
    float income, rent, utilities, groceries, transportation;
    printf("Hello user. Please input the information I require to allow me to help you calculate your finances.\n");
    printf("Please type how much you earn monthly.\n");
    scanf("%f", &income);
    printf("Thank you. Now type in how much you spend on rent each month.\n");
    scanf("%f", &rent);
    printf("Alright, now please type in how much you spend on utilities monthly.\n");
    scanf("%f", &utilities);
    printf("Almost done. Now input how much you pay for groceries each month.\n");
    scanf("%f", &groceries);
    printf("Last one. Now how much do you spend on transportation?\n");
    scanf("%f", &transportation);
    float savings = income/10.0;
    float spending_money = (income/10.0)*9;

    printf("All done.\n");
    printf("Your rent is %f%%");
    return 0;
}