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
	listint_t *new_node, *before, *after;

	if (head == NULL)
		return (NULL);
/* pointers */
	before = *head;
	after = *head;
	after = after->next;
	new_node = malloc(sizeof(listint_t)); /* allocate node */
	if (new_node == NULL)
		return (NULL);
	new_node->n = number; /* put in the data  */
/* If the Linked List is empty, then make the new node as head */
	if (*head == NULL)
	{	*head = new_node;
		return (new_node);
	}
	if (before->n >= number)
	{	new_node->next = before;
		*head = new_node;
		return (new_node);
	}
/* Else traverse till position or the last node */
	while (after->next != NULL)
	{
		if (before->n < number && after->n > number)
		{	before->next = new_node; /* Change the next of before node */
			new_node->next = after;  /* point new to after */
			return (new_node);
		}
		before = before->next;
		after = after->next;
	}
	after->next = new_node; /* Change the next of after node */
	new_node->next = NULL; /* point new to NULL */
	return (new_node);
}
