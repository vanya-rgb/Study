/*
*  реализовать вторую версию программы, вместо массива использовать односвязный
список; элементы добавлять таким образом, чтобы сохранялась упорядоченность списка
по названиям пунктов назначения (вставка нового элемента после элемента, который
меньше нового элемента и перед большим элементом)
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <locale.h>
#define MAX 3

struct aeroflot {
	char name[100];
	int number;
	char type[100];
};

struct node
{
	struct aeroflot aero;//поле данных
	struct list* next;//указател на след элемент
	struct node* prev;//указатель на предыдущий
};

struct node* first = NULL;
struct node* last = NULL;

//добавление данных
int max = 0;
struct node* addlem(struct node* last, int number, char* buf, char* ruf)
{
	struct node* temp, * p;
	temp = (struct node*)malloc(sizeof(struct node));
	p = last->next;//сохранение указателя на след эл
	last->next = temp;//предыдущий узел указ на создаваемый

	//сохранение данных
	strcpy(temp->aero.name, buf);
	temp->aero.number = number;
	strcpy(temp->aero.type, ruf);
	temp->next = p;//созданный указывает на следующий

	return(temp);//адрес добавл узла
}

//обмен соседних
struct node* swap(struct node* last1, struct node* last2, struct node* head)
{
	//возвращает новый корень списка
	struct node* prev1, * prev2, * next1, * next2;
	prev1 = head;
	prev2 = head;
	if (prev1 == last1)
		prev1 = NULL;
	else
		while (prev1->next != last1)//поиск предшедств last1
			prev1 = prev1->next;
	if (prev2 == last2)
		prev2 = NULL;
	else
		while (prev2->next != last2)//поиск предшедств last2
			prev2 = prev2->next;
	next1 = last1->next;// узел следующий за last1
	next2 = last2->next;// узел следующий за last2

	if (last2 == next1)
	{
		//Обмениваются соседние узлы
		last2->next = last1;
		last1->next = next2;
		if (last1 != head)
			prev1->next = last2;
	}
	else
		if (last1 == next2)
		{
			//Обмениваются соседние узлы
			last1->next = last2;
			last2->next = next1;
			if (last2 != head)
				prev2->next = last2;
		}
		else
		{
			if (last1 == next2)
			{
				//Обмениваются соседние узлы
				last1->next = last2;
				last2->next = next1;
				if (last2 != head)
					prev2->next = last2;
			}
			else
			{
				//Обмениваются ОТСТОЯЩИЕ узлы
				if (last1 != head)
					prev1->next = last2;
				last2->next = next1;
				if (last2 != head)
					prev2->next = last1;
				last1->next = next2;
			}
			if (last1 == head)
				return(last2);
			if (last2 == head)
				return(last1);
			return(head);
		}
}


main()
{
	setlocale(LC_ALL, "Russian");

	char buf[100];
	char ruf[100];

	for (int i = 0; i < MAX; i++)
	{

		printf_s("%d) name...", i + 1);
		scanf_s("%s", buf, 100);

		int number;
		printf_s("%d) number ...", i + 1);
		scanf_s("%d", &number);


		printf_s("%d) type...", i + 1);
		scanf_s("%s", ruf, 100);

		if (first == NULL)
		{
			first = malloc(sizeof(struct node));
			last = first;
			struct node* head = first;

			first->next = NULL;
			first->prev = NULL;

			strcpy(first->aero.name, buf);
			first->aero.number = number;
			strcpy(first->aero.type, ruf);

			continue;
		}

		addlem(last, number, buf, ruf);


	}

	//вывод элементов списка
	struct node* tmp = first;
	while (tmp != NULL)
	{
		printf_s("%s, %d, %s\n", tmp->aero.name, tmp->aero.number, tmp->aero.type);
		tmp = tmp->next;
	}


	//поиск по типу
	char resp[2];
	do
	{
		printf("\nВведите тип самолёта, данные по которым нужно узнать: ");
		scanf("%s", buf, 100);

		printf("Данные по рейсам, обслуживаемых самолётом типа: %s\n", buf);

		int had = 0;
		struct node *tmp = first;
		for (int i = 0; i < MAX; i++)
		{
			
			if (strcmp(tmp->aero.type, buf) == 0)
			{
				printf("Пункт назначения: %s\n", tmp->aero.name);
				printf("Номер рейса назначения: %d\n", tmp->aero.number);
				had = 1;
			}
			tmp = tmp->next;
		}
		if (!had)
		{
			printf("Не существует рейсов");
		}

		printf("\nПродолжить работу? (y/n): ");
		scanf("%s", resp);

	} while (strcmp(resp, "y") == 0);
	
}
