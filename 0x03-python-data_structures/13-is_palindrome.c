#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: A double pointer to the head of a singly linked list of integers.
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	if (!head || !*head || !(*head)->next)
		return (1);

	listint_t *prev = NULL;
	listint_t *next;
	listint_t *slowPtr = *head;
	listint_t *fastPtr = *head;

	while (fastPtr != NULL && fastPtr->next != NULL)
	{
		fastPtr = fastPtr->next->next;
		next = slowPtr->next;
		slowPtr->next = prev;
		prev = slowPtr;
		slowPtr = next;
	}

	if (fastPtr != NULL)
	{
		slowPtr = slowPtr->next;
	}

	while (prev != NULL && slowPtr != NULL)
	{
		if (prev->n != slowPtr->n)
			return (0);

		prev = prev->next;
		slowPtr = slowPtr->next;
	}

	return (1);
}
