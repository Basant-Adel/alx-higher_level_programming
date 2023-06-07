#include "lists.h"

/**
 * insert_node -> A function to inserts number into sorted singly linked list
 *@head: It's pointer (Head)
 *@number: It's the Insert Number
 *Return: The address of the new node or (NULL)-> if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nnode, *currentnode;

	if (head == NULL)
	{
		return (NULL);
	}
	nnode = malloc(sizeof(listint_t));

	if (nnode == NULL)
	{
		return (NULL);
	}
	nnode->n = number;
	nnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		nnode->next = *head;
		*head = nnode;
		return (nnode);
	}
	currentnode = *head;

	while (currentnode->next != NULL && currentnode->next->n < number)
	{
		currentnode = currentnode->next;
	}
	nnode->next = currentnode->next;
	currentnode->next = nnode;
	return (nnode);
}
