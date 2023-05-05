#include <stdio.h>

static char daytab[2][13] =
{
    {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
    {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
};
/* day_of_year: set day of year from month and day */
int day_of_year(int year, int month, int day)
{
    int i, leap;
    leap = (year%4 == 0) && (year%100 != 0) || (year%400 == 0);
    for (i = 1; i < month; i++)
    {
        day += daytab[leap][i];
    }
    return day;
}

void month_day(int year, int yearday, int *pmonth, int *pday)
{
        int i, leap;

        leap = (year%4 == 0) && (year%100 != 0) || (year%400 == 0);
        for (i = 1; yearday > daytab[leap][i]; i++)
                yearday -= daytab[leap][i];
        *pmonth = 1;
        *pday = yearday;
}

int main(int year, int month,int day)
{
    int days;
    days = day_of_year(year, month, day);
    if (days)
        printf("%d-%d-%d: day %dth of the year.\n", year, month, day, days);
    else
        printf("%d-%d-%d: invalid!\n", year, month, day);
}
                     