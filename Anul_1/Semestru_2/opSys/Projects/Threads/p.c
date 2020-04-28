#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

pthread_t threads[100]; //the threads
int matrix[100][100]; // the matrix
int row_sum[100]; //where to store all the sums that the threads compute
int n; //the size of the matrix

void* row_sum_calc (void* arg){
    // function used to compute the sum on a certain row received as a parameter
    int row = *(int*)arg, i; //getting the info out of the parameter
    free(arg);
    for (i = 0; i < n; i++)
        row_sum[row] += matrix[row][i];
    return NULL;
}

int main(){
    printf("Give the size of the matrix, smaller than 100: ");
    scanf("%d", &n);
    printf("Enter the elements of the matrix\n");
    int i, j;
    for (i=0; i<n; i++) {
        for (j=0; j<n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    //here we finish reading from the keyboard
    for(i=0;i<n;i++){
        int* arg = (int*)malloc(sizeof(int));
        *arg = i;
        if (pthread_create(&threads[i], NULL, row_sum_calc, arg) <0 ){
            //we create and check if we could create a thread for each row of the matrix
            perror("Error creating thread.\n");
            exit(1);
        }
    }
    
    for(i=0;i<n;i++)
        pthread_join(threads[i], NULL);
        //we wait on all the threads
    int sum=0;
    
    for(i=0;i<n;i++)
        sum+=row_sum[i]; //we compute the final sum in the main thread
    
    printf("The total sum of the matrix is %d.\n", sum); //and print it out
    return 0;
}
