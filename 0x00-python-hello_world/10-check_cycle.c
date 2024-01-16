#include "lists.h"

/**
 * check_cycle - a function tha checks if a singly linked list has cycle in it
 * @list: the linked list we wanna check
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
