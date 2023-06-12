#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: A double pointer to the head of a singly linked list of integers.
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	int check_palindrome = 1;
	listint_t *prev = NULL;
	listint_t *newNode;
	listint_t *slowPtr = *head;
	listint_t *fastPtr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (check_palindrome);

	while (fastPtr != NULL && fastPtr->next != NULL)
	{
		fastPtr = fastPtr->next->next;
		newNode = slowPtr;
		slowPtr = slowPtr->next;
		newNode->next = prev;
		prev = newNode;
	}

	if (fastPtr != NULL)
		slowPtr = slowPtr->next;
	while (slowPtr != NULL)
	{
		if (prev->n != slowPtr->n)
		{
			check_palindrome = 0;
			break;
		}
		prev = prev->next;
		slowPtr = slowPtr->next;
	} newNode = NULL;
	fastPtr = prev;
	while (fastPtr != NULL)
	{
		prev = fastPtr->next;
		fastPtr->next = newNode;
		newNode = fastPtr;
		fastPtr = prev;
	} *head = newNode;
	return (check_palindrome);
}
