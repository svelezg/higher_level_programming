#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * insert_node- Inserts a number into a sorted singly linked list.
 * @head: Head pointer
 * @number: integer
 * Return: nth node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev, *actual = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t)); /* allocate node */
	if (new_node == NULL)
		return (NULL);

	new_node->n = number; /* put in the data  */
	new_node->next = NULL;

	if (actual == NULL || actual->n > number) /* no head and at beginning */
	{	new_node->next = actual;
		*head = new_node;
		return (new_node);
	}

	while (actual && number > actual->n) /* Traverse till pos or last node */
	{	prev = actual;
		actual = actual->next;
	}

	prev->next = new_node; /* Change the next of prev node */
	new_node->next = actual;  /* point new to after */
	return (new_node);
}
