#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - prints all elements of a listint_t list
 * @h: pointer to head of list
 * @n: number
 * Return: added node
 */
listint_t *insert_node(listint_t **h, int n)
{
	listint_t *new, *current = *h;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	if (current == NULL || current->n >= n)
	{
		new->next = current;
		*h = new;
	}
	else
	{
		while (current && current->next && current->next->n < n)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
