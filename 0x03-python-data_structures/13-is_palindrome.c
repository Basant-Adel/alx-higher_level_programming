int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *prev = NULL;
    listint_t *next = NULL;

    while (slow != NULL) {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    slow = prev;

    while (slow != NULL) {
        if (slow->data != slow->next->data) {
            return 0;
        }
        slow = slow->next;
    }

    return 1;
}
