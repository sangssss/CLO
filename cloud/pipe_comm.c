#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int parent_to_child[2], child_to_parent[2];
    pid_t pid;
    char parent_msg[100];
    char child_msg[100];
    char buffer[100];

    pipe(parent_to_child);
    pipe(child_to_parent);

    pid = fork();

    if (pid > 0) { // Parent process
        close(parent_to_child[0]);
        close(child_to_parent[1]);

        printf("Parent: Enter a message to send to the child: ");
        fgets(parent_msg, sizeof(parent_msg), stdin);
        parent_msg[strcspn(parent_msg, "\n")] = 0;

        write(parent_to_child[1], parent_msg, strlen(parent_msg) + 1);
        printf("Parent sent: %s\n", parent_msg);

        read(child_to_parent[0], buffer, sizeof(buffer));
        printf("Parent received: %s\n", buffer);

        close(parent_to_child[1]);
        close(child_to_parent[0]);
    } 
    else if (pid == 0) { // Child process
        close(parent_to_child[1]);
        close(child_to_parent[0]);

        read(parent_to_child[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);

        printf("Child: Enter a message to send to the parent: ");
        fgets(child_msg, sizeof(child_msg), stdin);
        child_msg[strcspn(child_msg, "\n")] = 0;  // Remove newline character

        write(child_to_parent[1], child_msg, strlen(child_msg) + 1);

        close(parent_to_child[0]);
        close(child_to_parent[1]);
    }

    return 0;
}