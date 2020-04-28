#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h>

//There should be a fifo created in the same directory with the name my_fifo, and also the attached vocale.sh, with running permision.

int main(int argc, char** argv){
    if (argc == 1) {
        // We check if the user provided arguments.
        perror("No arguments provided.\n");
        exit(1);
    }
    int index;
    for (index = 1; index < argc; index++) {
        // For each argument in the command line
        int new_proc_A;
        new_proc_A = fork();
        // We create the process A.
        if (new_proc_A < 0) {
            // We check if we can fork.
            perror("Fork failed.\n");
            exit(2);
        }
        if (new_proc_A == 0){
            // This is the code for every process A.
            int new_proc_B, B_to_A[2];
            if(pipe(B_to_A) < 0){
                // First, we create the communication channel between A and B.
                perror("Could not create pipe\n");
                exit(3);
            }
            new_proc_B = fork();
            // For each process A, we create child B.
            if (new_proc_B < 0) {
                // We check if we can fork again.
                perror("Fork failed.\n");
                exit(2);
            }
            if (new_proc_B == 0) {
                // This is the code for process B.
                close(B_to_A[0]);
                // We cannot read from B to A, we must only write.
                char command[50], result[5];
                FILE* popen_result;
                command[0] = 0; //Make sure that this is empty.
                strcat(command, "./vocale.sh ");
                strcat(command, argv[index]);
                // Prepare the command to be executed, file vocale.sh must be in the same directory.
                popen_result = popen(command, "r");
                fgets(result, 5, popen_result);
                // Get the string containing the number.
                write(B_to_A[1], &result, 2);
                pclose(popen_result);
                close(B_to_A[0]);
                // Write towards A the result, then close everything and kill.
                exit(0);
            } else {
                // This is the code for process A, to get the result from B.
                close(B_to_A[1]);
                // We don't write from A to B, we just read.
                wait(0);
                // We wait for the child process.
                char result_got[3], final_result_string[40];
                read(B_to_A[0], &result_got, 2);
                //We read from the pipe the result we get from the other end.
                result_got[2] = 0;
                // We create a null terminated string. We have an empty space at the beginning of this string, at least on my terminal that's how the command executed.
                final_result_string[0] = 0; // Also we make sure that this thing is empty.
                strcat(final_result_string, "The word ");
                strcat(final_result_string, argv[index]);
                strcat(final_result_string, " has");
                strcat(final_result_string, result_got);
                strcat(final_result_string, " vowels.");
                // We build the final response string to be sent to the main program.
                int fifo;
                fifo = open("./my_fifo", O_WRONLY);
                int my_len = strlen(final_result_string);
        
                write(fifo, &my_len, sizeof(int));
                write(fifo, final_result_string, my_len);
                close(B_to_A[0]);
                exit(0);
                // Close the pipe, send the thing through the fifo, close the fifo and kill.
            }
        }
    }
    
    int fifo;
    fifo = open("./my_fifo", O_RDONLY);
    char result_got_final[40];
    int br, to_read;
    for (index = 1; index < argc; index++) {
        wait(0);
        read(fifo, &to_read, sizeof(int));
        br = read(fifo, result_got_final, to_read);
        result_got_final[br] = 0;
        printf("%s\n", result_got_final);
        
    }
    return 0;
}















