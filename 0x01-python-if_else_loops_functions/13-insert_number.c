#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new -> n = number;
	new -> next = NULL;

	if (!node || new -> n < node -> n)
	{
		new -> next = node;
		return (*head = new);
	}
	while (node)
	{
		if (!node -> next || new -> n < node -> next -> n)
		{
			new -> next = node -> next;
			node -> next = new;
			return (node);
		}
		node = node -> next;
	}
	return (NULL);
}
