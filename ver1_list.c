/*Описать структуру с именем aeroflot, содержащую следующие поля:
 название пункта назначения рейса;
 номер рейса (число);
 тип самолета.
Написать программу, выполняющую следующие действия:
 ввод с клавиатуры данных в массив, состоящий из максимум 7 элементов типа aeroflot,
причем сделать возможность прервать ввод, чтобы можно было не вводить все 7
элементов; после окончания ввода отсортировать элементы массива в алфавитном
порядке по названиям пунктов назначения;
 вывод в консоль номеров рейсов и пунктов назначения, обслуживаемых самолетом, тип
которого введен с клавиатуры;
 если таких рейсов нет, вывести соответствующее сообщение;
 реализовать вторую версию программы, вместо массива использовать односвязный
список; элементы добавлять таким образом, чтобы сохранялась упорядоченность списка
по названиям пунктов назначения (вставка нового элемента после элемента, который
меньше нового элемента и перед большим элементом)
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>


#define MAX_LENGTH_NAME     100
#define NDISCIPLINES         5
#define PROGRESS_TRESHOLD   4.0

typedef struct aeroflot {
    char name[MAX_LENGTH_NAME];
    int number;
    char type[MAX_LENGTH_NAME];
} flyght;

#define FLYGHTS 3

int comp(void const* a, void const* b)
{
    struct aeroflot* fly_a = (struct aeroflot*)a;
    struct aeroflot* fly_b = (struct aeroflot*)b;
    return strcmp(fly_a->name, fly_b->name);
}

int main()
{
    setlocale(LC_ALL, "Russian");

    flyght flyghts[FLYGHTS];

    memset(flyghts, 0, sizeof(flyght) * FLYGHTS);

    // ввод данных

    char buf[100];

    for (int i = 0; i < FLYGHTS; ++i) 
    {

        printf("Введите название пункта назначения: ");
        
        if (scanf("%s", buf, 100) == 1)
        {
            strcpy(flyghts[i].name, buf);

            if (strcmp(flyghts[i].name, "stop") == 0)
            {
                break;
            }
        }
            
        printf("Введите номер рейса: ");
        if (scanf("%d", &(flyghts[i].number)) < 1) 
        {
            break;
        }

        printf("Введите тип самолета: ");
        if (scanf("%s", buf, 100) == 0)
            break;
        strcpy(flyghts[i].type, buf);
    }

    //сортировка

    qsort(flyghts, FLYGHTS, sizeof(struct aeroflot), comp);

    for (int i = 0; i < FLYGHTS; i++)
        printf("%i) пункт = %s, рейс = %d, тип = %s\n", i + 1, flyghts[i].name, flyghts[i].number, flyghts[i].type);

    //вывод в консоль номеров рейсов и пунктов назначения, обслуживаемых самолетом, тип
    //которого введен с клавиатуры;

    char resp[2];

    do
    {
        printf("\nВведите тип самолёта, данные по которым нужно узнать: ");
        scanf("%s", buf, 100);

        printf("Данные по рейсам, обслуживаемых самолётом типа: %s\n", buf);

        int had = 0;
        for (int i = 0; i < FLYGHTS; i++)
        {
            
            if (strcmp( flyghts[i].type, buf) == 0)
            {
                printf("Пункт назначения: %s\n", flyghts[i].name);
                printf("Номер рейса назначения: %d\n", flyghts[i].number);
                had= 1;
            }
        }
        if (!had)
        {
            printf("Не существует рейсов");
        }

        printf("\nПродолжить работу? (y/n): ");
        scanf("%s", resp);

    } while (strcmp(resp, "y") == 0);
}



