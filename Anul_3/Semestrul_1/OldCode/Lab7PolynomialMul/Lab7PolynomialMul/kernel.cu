
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <time.h>
#include <stdlib.h>

#define MAX(a, b) (a) >= (b) ? (a) : (b)
#define MIN(a, b) (a) <= (b) ? (a) : (b)


void printPoly(int * polyCoefficients, int size)
{
	for (int i = 0; i < size; i++) {
		std::cout << (polyCoefficients[i] >= 0 ? "+ " : "- ");
		std::cout << std::abs(polyCoefficients[i]);
		std::cout << " * X^";
		std::cout << i;
		std::cout << " ";
	}
}

cudaError_t simpleMulWithCuda(int *result, const int *a, const int *b, unsigned int sizeA, unsigned int sizeB, unsigned int numberOfThreads);
cudaError_t karatsubaMulWithCuda(int *result, const int *a, const int *b, unsigned int sizeA, unsigned int sizeB);

__global__ void simpleMulKernel(int *result, const int *a, const int *b, const int sizeA, const int sizeB, const int numberOfThreads)
{
	int sizeResult = sizeA + sizeB - 1;
	int startPosition = (threadIdx.x * sizeResult) / numberOfThreads;
	int endPosition = ((threadIdx.x + 1) * sizeResult) / numberOfThreads;
	for (int position = startPosition; position < endPosition; position++) {
		int sum = 0;
		int begin = (position < sizeB ? 0 : position - sizeB + 1);
		int end = sizeA <= position + 1 ? sizeA : position + 1;
		for (int i = begin; i < end; i++) {
			sum += a[i] * b[position - i];
		}
		result[position] = sum;
	}
}

__global__ void copyArrayOfRange(int* destination, const int* source, const int begin, const int end)
{
	for (int i = begin; i < end; i++) 
	{
		destination[i - begin] = source[i];
	}
}

__global__ void polyAdd(int* result, const int* a, const int* b, const int sizeA, const int sizeB)
{
	int limit = MAX(sizeA, sizeB);//sizeA >= sizeB ? sizeA : sizeB;
	if (sizeA == limit) 
	{
		while (limit > sizeB) 
		{
			result[limit - 1] = a[limit - 1];
			limit--;
		}
	}
	else 
	{
		while (limit > sizeA) 
		{
			result[limit - 1] = b[limit - 1];
			limit--;
		}
	}
	for (int i = 0; i < limit; i++) 
	{
		result[i] = a[i] + b[i];
	}
}

__global__ void polyShiftKernel(int* result, const int* source, const int size, const int shiftPositions)
{
	int i;
	for (i = 0; i < shiftPositions; i++)
	{
		result[i] = 0;
	}
	for (i = 0; i < size; i++)
	{
		result[i + shiftPositions] = source[i];
	}
}

__global__ void polySubKernel(int* result, const int* a, const int* b, const int sizeA, const int sizeB)
{
	int limit = MAX(sizeA, sizeB);// sizeA >= sizeB ? sizeA : sizeB;
	if (sizeA == sizeB) 
	{
		while (limit > 1 && a[limit - 1] == b[limit - 1]) 
		{
			result[limit - 1] = 0;
			limit--;
		}
	}
	else 
	{
		if (sizeA == limit) 
		{
			while (limit > sizeB) 
			{
				result[limit - 1] = a[limit - 1];
				limit--;
			}
		}
		else 
		{
			while (limit > sizeA) 
			{
				result[limit - 1] = -b[limit - 1];
				limit--;
			}
		}
	}
	for (int i = limit - 1; i >= 0; i--) 
	{
		result[i] = a[i] - b[i];
	}
}

__global__ void karatsubaMulKernel(int *result, const int *a, const int *b, const int sizeA, const int sizeB)
{
	//karatsubaMulKernel<<<1, 1>>>(result, a, b, sizeA, sizeB, numberOfThreads - 1);
	cudaError_t cudaStatus;// = cudaDeviceSynchronize();
	//if (cudaStatus != cudaSuccess) {
		//fprintf(stderr, "cudaDeviceSynchronize returned error code %d after launching addKernel!\n", cudaStatus);
	//}
	//printf("ENTRY sizes: %d %d\n", sizeA, sizeB);

	//printf("%d %d pos 1\n", a[0], b[0]);

	/*if (a[0] == 2 && a[1] == 3) {
		printf("A: ");
		for (int i = 0; i < sizeA; i++)
		{
			printf("%d ", a[i]);
		}
		printf("\n");
		printf("B: ");
		for (int i = 0; i < sizeB; i++)
		{
			printf("%d ", b[i]);
		}
		printf("\n");
		printf("\n");
	}*/


	//printf("%d %d pos 2\n", a[0], b[0]);
	if (sizeA < 2 || sizeB < 2) {
		simpleMulKernel <<<1, 1 >>>(result, a, b, sizeA, sizeB, 1);
		cudaDeviceSynchronize();
		/*printf("RESULT: ");
		for (int i = 0; i < (sizeA + sizeB - 1); i++)
		{
			printf("%d ", result[i]);
		}
		printf("\n");
		printf("\n");*/
		return;
	}
	int m = sizeA > sizeB ? sizeA : sizeB;
	const int halfPoint = m / 2;
	const int sizeH = sizeA;

	int* highA;
	cudaMalloc((void**)&highA, (sizeA - halfPoint) * sizeof(int));
	int* lowA;
	cudaMalloc((void**)&lowA, halfPoint * sizeof(int));
	int* highB;
	cudaMalloc((void**)&highB, (sizeB - halfPoint) * sizeof(int));
	int* lowB;
	cudaMalloc((void**)&lowB, halfPoint * sizeof(int));

	//printf("%d %d sizes hA %d lA %d hB %d lb %d\n", a[0], b[0], (sizeA - halfPoint), halfPoint, (sizeB - halfPoint), halfPoint);

	copyArrayOfRange <<<1, 1 >>>(highA, a, halfPoint, sizeA);
	copyArrayOfRange <<<1, 1 >>>(lowA, a, 0, halfPoint);
	copyArrayOfRange <<<1, 1 >>>(highB, b, halfPoint, sizeB);
	copyArrayOfRange <<<1, 1 >>>(lowB, b, 0, halfPoint);
	cudaDeviceSynchronize();


	//printf("%d %d pos 3\n", a[0], b[0]);

	int* lowParts;
	int sizeLowParts = (halfPoint * 2);
	cudaMalloc((void**)&lowParts, sizeLowParts * sizeof(int));
	int* highParts;
	int sizeHighParts = (sizeA + sizeB - halfPoint * 2);
	cudaMalloc((void**)&highParts, sizeHighParts * sizeof(int));
	int* sumA;
	int sizeSumA = ((halfPoint >= (sizeA - halfPoint)) ? halfPoint : (sizeA - halfPoint));
	cudaMalloc((void**)&sumA, sizeSumA * sizeof(int));
	int* sumB;
	int sizeSumB = ((halfPoint >= (sizeB - halfPoint)) ? halfPoint : (sizeB - halfPoint));
	cudaMalloc((void**)&sumB, sizeSumB * sizeof(int));

	polyAdd <<< 1, 1 >>> (sumA, lowA, highA, halfPoint, (sizeA - halfPoint));
	polyAdd <<< 1, 1 >>> (sumB, lowB, highB, halfPoint, (sizeB - halfPoint));



	int* sumParts;
	int sizeSumParts = sizeSumA + sizeSumB - 1;
	cudaMalloc((void**)&sumParts, sizeSumParts * sizeof(int));

	cudaDeviceSynchronize();
	//printf("%d %d pos 4\n", a[0], b[0]);

	

	karatsubaMulKernel <<< 1, 1 >>> (lowParts, lowA, lowB, halfPoint, halfPoint);
	karatsubaMulKernel <<< 1, 1 >>> (sumParts, sumA, sumB, sizeSumA, sizeSumB);
	karatsubaMulKernel <<< 1, 1 >>> (highParts, highA, highB, (sizeA - halfPoint), (sizeB - halfPoint));

	//printf("%d %d pos 5\n", a[0], b[0]);

	/*printf("highB: ");
	for (int i = 0; i < (sizeB - halfPoint); i++)
	{
		printf("%d ", highB[i]);
	}
	printf("\n");*/

	/*printf("highParts: ");
	for (int i = 0; i < (sizeA + sizeB - 2 *halfPoint); i++)
	{
		printf("%d ", highParts[i]);
	}
	printf("\n");
	printf("SUM : %d |", sizeSumA);
	for (int i = 0; i < sizeSumParts; i++)
	{
		printf("%d ", sumParts[i]);
	}
	printf("\n");*/
	cudaDeviceSynchronize();

	cudaFree(lowA);
	cudaFree(lowB);
	cudaFree(highA);
	cudaFree(highB);
	cudaFree(sumA);
	cudaFree(sumB);

	int* shiftHighParts;
	int sizeShiftHighParts = (sizeA + sizeB);
	cudaMalloc((void**)&shiftHighParts, sizeShiftHighParts * sizeof(int));

	int* sumMinusHigh;
	int sizeHighMinusSum = MAX(sizeHighParts, sizeSumParts);
	cudaMalloc((void**)&sumMinusHigh,  sizeHighMinusSum * sizeof(int));

	polyShiftKernel <<< 1, 1 >>> (shiftHighParts, highParts, (sizeA + sizeB - halfPoint * 2), 2 * halfPoint);
	polySubKernel <<< 1, 1 >>> (sumMinusHigh, sumParts, highParts, sizeSumParts, sizeHighParts);

	cudaDeviceSynchronize();
	//printf("%d %d pos 6\n", a[0], b[0]);
	/*printf("SUM MINUS HIGH: ");
	for (int i = 0; i < sizeHighMinusSum; i++)
	{
		printf("%d ", sumMinusHigh[i]);
	}
	printf("\n");*/

	int* shiftPlusLow;
	int sizeShiftPlusLow = MAX(sizeShiftHighParts, sizeLowParts);
	cudaMalloc((void**)&shiftPlusLow, sizeShiftPlusLow * sizeof(int));

	int* minusMinus;
	int sizeMinusMinus = MAX(sizeHighMinusSum, sizeLowParts);
	cudaMalloc((void**)&minusMinus, sizeMinusMinus * sizeof(int));

	polyAdd <<< 1, 1 >>> (shiftPlusLow, shiftHighParts, lowParts, sizeShiftHighParts, sizeLowParts);
	polySubKernel <<< 1, 1 >>> (minusMinus, sumMinusHigh, lowParts, sizeHighMinusSum, sizeLowParts);

	cudaDeviceSynchronize();
	//printf("%d %d pos 7\n", a[0], b[0]);

	int* finalShift;
	int sizeFinalShift = sizeMinusMinus + halfPoint;
	cudaMalloc((void**)&finalShift, sizeFinalShift * sizeof(int));

	polyShiftKernel <<< 1, 1 >>> (finalShift, minusMinus, sizeMinusMinus, halfPoint);

	cudaDeviceSynchronize();
	//printf("%d %d pos 8\n", a[0], b[0]);

	/*printf("FINAL SHIFT: ");
	for (int i = 0; i < sizeFinalShift; i++)
	{
		printf("%d ", finalShift[i]);
	}
	printf("\n");*/

	polyAdd <<< 1, 1 >>> (result, shiftPlusLow, finalShift, sizeShiftPlusLow, sizeFinalShift);

	cudaFree(lowParts);
	cudaFree(highParts);
	cudaFree(sumParts);
	cudaFree(shiftHighParts);
	cudaFree(sumMinusHigh);
	cudaFree(minusMinus);
	cudaFree(shiftPlusLow);
	cudaFree(finalShift);

	cudaDeviceSynchronize();
	//printf("%d %d pos 9\n", a[0], b[0]);

	/*printf("RESULT: ");
	for (int i = 0; i < (sizeA + sizeB - 1); i++)
	{
		printf("%d ", result[i]);
	}
	printf("\n");
	printf("\n");*/

	//printf("EXIT sizes: %d %d\n", sizeA, sizeB);
	//return polyAdd(polyAdd(polyShift(r, 2 * halfPoint), polyShift(polySub(polySub(q, r), p), halfPoint)), p);
}


void generatePoly(int* poly, int size, int maxValue)
{
	srand(time(NULL));
	for (int i = 0; i <= size; i++) 
	{
		poly[i] = rand() % maxValue;
	}
}

int main()
{
	int* a;
	int* b;
	int* resultSimple;
	int* resultKaratsuba;
	const int degreeSize = 9;
	const int degrees[degreeSize] = { 1, 2, 3, 8, 16, 32, 64, 128, 256 };//, 512, 1024};
	clock_t begin;
	clock_t end;
	
	int x[] = { 1, 2, 3, 4 };
	int y[] = { 5, 6, 7, 8 };

	/*resultSimple = (int*)malloc((2 * 4 - 1) * sizeof(int));
	resultKaratsuba = (int*)malloc((2 * 4 - 1) * sizeof(int));

	cudaError_t cudaStatus = simpleMulWithCuda(resultSimple, x, y, 4, 4, MIN(100, ((2 * 3 - 1) / 5 + 1)));
	cudaStatus = karatsubaMulWithCuda(resultKaratsuba, x, y, 4, 4);

	printPoly(resultSimple, 2 * 4 - 1);
	printf("\n");
	printPoly(resultKaratsuba, 2 * 4 - 1);
	printf("\n");

	free(resultSimple);
	free(resultKaratsuba);*/

	for (int i = 0; i < degreeSize; i++)
	{
		a = (int*)malloc((degrees[i] + 1) * sizeof(int));
		b = (int*)malloc((degrees[i] + 1) * sizeof(int));
		resultSimple = (int*)malloc((2 * degrees[i] - 1) * sizeof(int));
		resultKaratsuba = (int*)malloc((2 * degrees[i] - 1) * sizeof(int));
		generatePoly(a, degrees[i], 10);
		generatePoly(b, degrees[i], 10);

		printf("degree: %d: ", degrees[i]);
		begin = clock();
		cudaError_t cudaStatus = simpleMulWithCuda(resultSimple, a, b, degrees[i], degrees[i], MIN(100, ((2 * degrees[i] - 1) / 5 + 1)));
		end = clock();
		printf("%d ", (int)(double(end - begin) / CLOCKS_PER_SEC * 1000));
		begin = clock();
		cudaStatus = karatsubaMulWithCuda(resultKaratsuba, a, b, degrees[i], degrees[i]); 
		end = clock();
		printf("%d\n", (int)(double(end - begin) / CLOCKS_PER_SEC * 1000));
		/*if (cudaStatus != cudaSuccess) {
			fprintf(stderr, "addWithCuda failed!");
			return 1;
		}*/

		/*printPoly(resultSimple, 2 * degrees[i] - 1);
		printf("\n");
		printPoly(resultKaratsuba, 2 * degrees[i] - 1);
		printf("\n");*/


		// cudaDeviceReset must be called before exiting in order for profiling and
		// tracing tools such as Nsight and Visual Profiler to show complete traces.
		cudaStatus = cudaDeviceReset();
		if (cudaStatus != cudaSuccess) {
			fprintf(stderr, "cudaDeviceReset failed!");
			return 1;
		}
		free(a);
		free(b);
		free(resultSimple);
		free(resultKaratsuba);
	}
	getchar();

    return 0;
}


cudaError_t simpleMulWithCuda(int *result, const int *a, const int *b, unsigned int sizeA, unsigned int sizeB, unsigned int numberOfThreads)
{
    int *dev_a = 0;
    int *dev_b = 0;
    int *dev_result = 0;

	//int numberOfThreads = sizeA;
	//int sizeB = sizeA;

	int sizeResult = sizeA + sizeB - 1;
    cudaError_t cudaStatus;


    // Choose which GPU to run on, change this on a multi-GPU system.
    cudaStatus = cudaSetDevice(0);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaSetDevice failed!  Do you have a CUDA-capable GPU installed?");
        goto Error;
    }

    // Allocate GPU buffers for three vectors (two input, one output)    .
    cudaStatus = cudaMalloc((void**)&dev_result, sizeResult * sizeof(int));
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed!");
        goto Error;
    }

    cudaStatus = cudaMalloc((void**)&dev_a, sizeA * sizeof(int));
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed!");
        goto Error;
    }

    cudaStatus = cudaMalloc((void**)&dev_b, sizeB * sizeof(int));
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed!");
        goto Error;
    }

    // Copy input vectors from host memory to GPU buffers.
    cudaStatus = cudaMemcpy(dev_a, a, sizeA * sizeof(int), cudaMemcpyHostToDevice);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

    cudaStatus = cudaMemcpy(dev_b, b, sizeB * sizeof(int), cudaMemcpyHostToDevice);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

    // Launch a kernel on the GPU with one thread for each element.
    simpleMulKernel<<<1, numberOfThreads>>>(dev_result, dev_a, dev_b, sizeA, sizeB, numberOfThreads);
	//karatsubaMulKernel <<<1, 1 >>>(dev_result, dev_a, dev_b, sizeA, sizeB);

    // Check for any errors launching the kernel
    cudaStatus = cudaGetLastError();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "addKernel launch failed: %s\n", cudaGetErrorString(cudaStatus));
        goto Error;
    }
    
    // cudaDeviceSynchronize waits for the kernel to finish, and returns
    // any errors encountered during the launch.
    cudaStatus = cudaDeviceSynchronize();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDeviceSynchronize returned error code %d after launching addKernel!\n", cudaStatus);
        goto Error;
    }

    // Copy output vector from GPU buffer to host memory.
    cudaStatus = cudaMemcpy(result, dev_result, sizeResult * sizeof(int), cudaMemcpyDeviceToHost);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

Error:
    cudaFree(dev_result);
    cudaFree(dev_a);
    cudaFree(dev_b);

    return cudaStatus;
}

cudaError_t karatsubaMulWithCuda(int *result, const int *a, const int *b, unsigned int sizeA, unsigned int sizeB)
{
	int *dev_a = 0;
	int *dev_b = 0;
	int *dev_result = 0;

	//int numberOfThreads = sizeA;
	//int sizeB = sizeA;

	int sizeResult = sizeA + sizeB - 1;
	cudaError_t cudaStatus;


	// Choose which GPU to run on, change this on a multi-GPU system.
	cudaStatus = cudaSetDevice(0);
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaSetDevice failed!  Do you have a CUDA-capable GPU installed?");
		goto Error;
	}

	// Allocate GPU buffers for three vectors (two input, one output)    .
	cudaStatus = cudaMalloc((void**)&dev_result, sizeResult * sizeof(int));
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaMalloc failed!");
		goto Error;
	}

	cudaStatus = cudaMalloc((void**)&dev_a, sizeA * sizeof(int));
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaMalloc failed!");
		goto Error;
	}

	cudaStatus = cudaMalloc((void**)&dev_b, sizeB * sizeof(int));
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaMalloc failed!");
		goto Error;
	}

	// Copy input vectors from host memory to GPU buffers.
	cudaStatus = cudaMemcpy(dev_a, a, sizeA * sizeof(int), cudaMemcpyHostToDevice);
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaMemcpy failed!");
		goto Error;
	}

	cudaStatus = cudaMemcpy(dev_b, b, sizeB * sizeof(int), cudaMemcpyHostToDevice);
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaMemcpy failed!");
		goto Error;
	}


	// Launch a kernel on the GPU with one thread for each element.
	//simpleMulKernel<<<1, numberOfThreads>>>(dev_result, dev_a, dev_b, sizeA, sizeB, numberOfThreads);
	karatsubaMulKernel <<<1, 1 >>>(dev_result, dev_a, dev_b, sizeA, sizeB);

	// Check for any errors launching the kernel
	cudaStatus = cudaGetLastError();
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "addKernel launch failed: %s\n", cudaGetErrorString(cudaStatus));
		goto Error;
	}

	// cudaDeviceSynchronize waits for the kernel to finish, and returns
	// any errors encountered during the launch.
	cudaStatus = cudaDeviceSynchronize();
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaDeviceSynchronize returned error code %d after launching addKernel!\n", cudaStatus);
		goto Error;
	}


	// Copy output vector from GPU buffer to host memory.
	cudaStatus = cudaMemcpy(result, dev_result, sizeResult * sizeof(int), cudaMemcpyDeviceToHost);
	if (cudaStatus != cudaSuccess) {
		fprintf(stderr, "cudaMemcpy failed!");
		goto Error;
	}

Error:
	cudaFree(dev_result);
	cudaFree(dev_a);
	cudaFree(dev_b);

	return cudaStatus;
}
