#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newNode->next = node->next;
	node->next = newNode;
	return (new);
}
