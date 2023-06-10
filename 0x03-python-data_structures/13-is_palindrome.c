#include "lists.h"

/**
 * reverse_listint - reverses a list
 * @head: list head
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - check code
 * @h: list head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **h)
{
	listint_t *slow = *h, *fast = *h, *rev_list;

	if (*h == NULL)
		return (1);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	rev_list = fast ? slow->next : slow;
	reverse_listint(&rev_list);
	slow = *h;
	while (rev_list && slow)
	{
		if (slow->n != rev_list->n)
			return (0);
		rev_list = rev_list->next;
		slow = slow->next;
	}
	return (1);
}
