#include "lists.h"
#include <stdlib.h>

/**
 * add_node - check the code
 * @h: list header
 * @n: value to add
 * Return: new node
 */
listint_t *add_node(listint_t **h, int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	new_node->next = *h;
	*h = new_node;
	return (new_node);
}
/**
 * is_palindrome - check code
 * @h: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **h)
{
	listint_t *node = *h, *tmp;
	listint_t *stk = NULL;
	int c = 1;

	if (h == NULL || *h == NULL)
		return (c);
	while (node)
	{
		add_node(&stk, node->n);
		node = node->next;
	}
	node = *h;
	tmp = stk;
	while (node)
	{
		if (node->n != tmp->n)
		{
			c = 0;
			break;
		}
		tmp = tmp->next;
		node = node->next;
	}
	free_listint(stk);
	return (c);
}
