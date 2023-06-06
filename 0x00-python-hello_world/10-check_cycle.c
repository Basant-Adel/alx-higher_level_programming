#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked list has cycle
 *@list: It's refer to arg 1
 *Return: (0)-> if there is no cycle (1)-> if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fa = list, *sl = list;

	if (list == NULL)
		return (0);
	fa = list->next;
	sl = list;
	while (fa != NULL && fa->next != NULL)
	{
		sl = sl->next;
		fa = fa->next->next;
		if (sl == fa)
			return (1);
	}
	return (0);
}
