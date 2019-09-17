#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome- Checks if a singly linked list is a palindrome.
 * @head: Head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node, *reverse, *rev_head;

	if ((!*head) || (!head))
		return (1);

	/*rev_head = malloc(sizeof(listint_t)); */ /* allocate node */
	/*if (rev_head == NULL)*/
	/*	return (1);*/

	node = *head;
	rev_head = *head;
	node = node->next;

	while (node)
	{
		reverse = malloc(sizeof(listint_t)); /* allocate node */
		if (reverse == NULL)
			return (1);

		reverse->n = node->n; /* put in the data  */
		reverse->next = rev_head;
		node = node->next;
		rev_head = reverse;
	}

	node = *head;

	while (*head)
	{
		if ((*head)->n != rev_head->n)
		{
			/*free_listint(rev_head);*/
			return (0);
		}
		*head = (*head)->next;
		rev_head = rev_head->next;
	}
	/*free_listint(rev_head);*/
	return (1);
}
