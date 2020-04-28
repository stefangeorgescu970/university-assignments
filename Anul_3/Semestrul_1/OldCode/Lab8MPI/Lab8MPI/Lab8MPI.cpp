// Lab8MPI.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "mpi.h"
#include "stdio.h"
#include "stdlib.h"
#include "iostream"
#include <time.h>

#define intT int
#define intMpi MPI_INT32_T

#define MAX(a, b) (a) >= (b) ? (a) : (b)
#define MIN(a, b) (a) <= (b) ? (a) : (b)

const intT giveWork = 0;
const intT noWorkToGive = 1;

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

void generatePoly(intT poly[], intT size, intT maxValue)
{
	srand(time(NULL));
	for (int i = 0; i < size; i++)
	{
		poly[i] = rand() % maxValue;
	}
}

void mpiSimplePolyMulCompute(intT result[], intT a[], intT sizeA, intT b[], intT sizeB, intT resultBeginPosition, intT resultEndPosition)
{
	for (int position = resultBeginPosition; position < resultEndPosition; position++) {
		int sum = 0;
		int begin = (position < sizeB ? 0 : position - sizeB + 1);
		int end = sizeA <= position + 1 ? sizeA : position + 1;
		for (int i = begin; i < end; i++) {
			sum += a[i] * b[position - i];
		}
		result[position - resultBeginPosition] = sum;
	}
}

void mpiSimplePolyMulSplitWork(intT result[], intT a[], const intT &sizeA, intT b[], const intT &sizeB, intT workersBeginInterval, intT workersEndInterval, intT resultBeginPos, intT resultEndPos)
{
	if ((workersEndInterval - workersBeginInterval) > 1)
	{
		if ((resultEndPos - resultBeginPos) <= 1) 
		{
			for (int i = workersBeginInterval + 1; i < workersEndInterval; i++) 
				MPI_Send(&noWorkToGive, 1, intMpi, i, 0, MPI_COMM_WORLD);
			mpiSimplePolyMulCompute(result, a, sizeA, b, sizeB, resultBeginPos, resultEndPos);
		} 
		else 
		{
			intT midWorkers = (workersBeginInterval + workersEndInterval + 1) / 2;
			intT midResultPos = (resultBeginPos + resultEndPos) / 2;
			MPI_Send(&giveWork, 1, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(&sizeA, 1, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(a, sizeA, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(&sizeB, 1, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(b, sizeB, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(&workersEndInterval, 1, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(&midResultPos, 1, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			MPI_Send(&resultEndPos, 1, intMpi, midWorkers, 0, MPI_COMM_WORLD);
			mpiSimplePolyMulSplitWork(result, a, sizeA, b, sizeB, workersBeginInterval, midWorkers, resultBeginPos, midResultPos);
			MPI_Recv(result + midResultPos - resultBeginPos, resultEndPos - midResultPos, intMpi, midWorkers, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		}
	}
	else
	{
		mpiSimplePolyMulCompute(result, a, sizeA, b, sizeB, resultBeginPos, resultEndPos);
	}
}

void mpiSimplePolyMul(int &argc, char* argv[])
{
	MPI_Init(&argc, &argv);

	intT rank;

	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	if (rank == 0)
	{
		clock_t begin;
		clock_t end;
		const intT degree = 3;
		const intT sizeA = degree;
		const intT sizeB = degree;
		intT a[sizeA] = { 1, 2, 3 };
		intT b[sizeB] = { 4, 5, 6 };
		const intT sizeResult = sizeA + sizeB - 1;
		intT result[sizeResult];
		intT numberOfWorkers;
		//generatePoly(a, degree, 10);
		//generatePoly(b, degree, 10);
		MPI_Comm_size(MPI_COMM_WORLD, &numberOfWorkers);
		begin = clock();
		mpiSimplePolyMulSplitWork(result, a, sizeA, b, sizeB, 0, numberOfWorkers, 0, sizeResult);
		end = clock();
		printPoly(result, sizeA + sizeB - 1);
		std::cout << "\ntime: ";
		printf("%d ", (int)(double(end - begin) / CLOCKS_PER_SEC * 1000));
	}
	else if (rank >= 1)
	{
		intT* a;
		intT* b;
		intT sizeA;
		intT sizeB;
		intT workersEndInterval;
		intT resultBeginPos;
		intT resultEndPos;
		intT* result;
		intT givenWork;
		MPI_Status status;
		MPI_Recv(&givenWork, 1, intMpi, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
		if (givenWork == giveWork)
		{
			MPI_Recv(&sizeA, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			a = (int*)malloc(sizeA * sizeof(intT));
			MPI_Recv(a, sizeA, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Recv(&sizeB, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			b = (int*)malloc(sizeB * sizeof(intT));
			MPI_Recv(b, sizeB, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Recv(&workersEndInterval, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Recv(&resultBeginPos, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Recv(&resultEndPos, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			result = (int*)malloc(sizeof(intT) * (resultEndPos - resultBeginPos));
			mpiSimplePolyMulSplitWork(result, a, sizeA, b, sizeB, rank, workersEndInterval, resultBeginPos, resultEndPos);
			MPI_Send(result, resultEndPos - resultBeginPos, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD);
			//std::cout << "Rank " << rank << "(" << resultBeginPos << ", " << resultEndPos << "): ";
			//printPoly(result, resultEndPos - resultBeginPos);
			//std::cout << std::endl;
			//MPI_Recv(&givenWork, 1, intMpi, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
		}
	}

	MPI_Finalize();
}

void copyArrayOfRange(intT* destination, const intT* source, const intT begin, const intT end)
{
	for (int i = begin; i < end; i++)
	{
		destination[i - begin] = source[i];
	}
}

void polyAdd(intT* result, const intT* a, const intT sizeA, const intT* b, const intT sizeB)
{
	intT limit = MAX(sizeA, sizeB);//sizeA >= sizeB ? sizeA : sizeB;
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

void polyShift(intT* result, const intT* source, const intT size, const intT shiftPositions)
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

void polySub(intT* result, const intT* a, const intT sizeA, const intT* b, const intT sizeB)
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

void mpiKaratsubaPolyMulCompute(intT *result, intT *a, const intT sizeA, intT *b, const intT sizeB, intT workersBeginInterval, intT workersEndInterval)
{
	//std::cout << workersBeginInterval << " " << workersEndInterval<< " started" << std::endl;
	if (sizeA < 2 || sizeB < 2) {
		mpiSimplePolyMulCompute(result, a, sizeA, b, sizeB, 0, sizeA + sizeB - 1);
		if ((workersEndInterval - workersBeginInterval) > 1)
		{
			//std::cout << workersBeginInterval << " " << workersEndInterval << " will notify" << std::endl;
			for (int i = workersBeginInterval + 1; i < workersEndInterval; i++)
				MPI_Send(&noWorkToGive, 1, intMpi, i, 0, MPI_COMM_WORLD);
		}
		//std::cout << workersBeginInterval << " " << workersEndInterval << " finished" << std::endl;
		return;
	}
	intT m = MAX(sizeA, sizeB);
	const intT halfPoint = m / 2;
	const intT sizeH = sizeA;

	intT* highA = (intT*)malloc((sizeA - halfPoint) * sizeof(intT));
	intT* lowA = (intT*)malloc(halfPoint * sizeof(intT));
	intT* highB = (intT*)malloc((sizeB - halfPoint) * sizeof(intT));
	intT* lowB = (intT*)malloc(halfPoint * sizeof(intT));

	copyArrayOfRange(highA, a, halfPoint, sizeA);
	copyArrayOfRange(lowA, a, 0, halfPoint);
	copyArrayOfRange(highB, b, halfPoint, sizeB);
	copyArrayOfRange(lowB, b, 0, halfPoint);

	intT* lowParts;
	intT sizeLowParts = (halfPoint * 2 - 1);
	lowParts = (intT*)malloc(sizeLowParts * sizeof(intT));
	intT* highParts;
	intT sizeHighParts = (sizeA + sizeB - halfPoint * 2 - 1);
	highParts = (intT*)malloc(sizeHighParts * sizeof(intT));
	intT* sumA;
	intT sizeSumA = MAX(halfPoint, (sizeA - halfPoint));
	sumA = (intT*)malloc(sizeSumA * sizeof(intT));
	intT* sumB;
	intT sizeSumB = MAX(halfPoint, (sizeB - halfPoint));
	sumB = (intT*)malloc(sizeSumB * sizeof(intT));

	polyAdd(sumA, lowA, halfPoint, highA, (sizeA - halfPoint));
	polyAdd(sumB, lowB, halfPoint, highB, (sizeB - halfPoint));

	intT* sumParts;
	intT sizeSumParts = sizeSumA + sizeSumB - 1;
	sumParts = (intT*)malloc(sizeSumParts * sizeof(intT));

	if ((workersEndInterval - workersBeginInterval) > 2)
	{
		intT mid1 = workersBeginInterval + (workersEndInterval - workersBeginInterval) / 3;//(workersBeginInterval + workersEndInterval + 1) / 3;
		intT mid2 = workersBeginInterval + (workersEndInterval - workersBeginInterval) * 2 / 3;//(workersBeginInterval + workersEndInterval) / 3 + (wo);
		//std::cout << workersBeginInterval << " " << mid1 << " " << mid2 << " " << workersEndInterval << std::endl;
		//mpiKaratsubaPolyMulCompute(lowParts, lowA, halfPoint, lowB, halfPoint, workersBeginInterval, workersEndInterval);
		MPI_Send(&giveWork, 1, intMpi, mid1, 0, MPI_COMM_WORLD);
		MPI_Send(&halfPoint, 1, intMpi, mid1, 0, MPI_COMM_WORLD);
		MPI_Send(lowA, halfPoint, intMpi, mid1, 0, MPI_COMM_WORLD);
		MPI_Send(&halfPoint, 1, intMpi, mid1, 0, MPI_COMM_WORLD);
		MPI_Send(lowB, halfPoint, intMpi, mid1, 0, MPI_COMM_WORLD);
		MPI_Send(&mid2, 1, intMpi, mid1, 0, MPI_COMM_WORLD);

		//mpiKaratsubaPolyMulCompute(sumParts, sumA, sizeSumA, sumB, sizeSumB, workersBeginInterval, workersEndInterval);
		MPI_Send(&giveWork, 1, intMpi, mid2, 0, MPI_COMM_WORLD);
		MPI_Send(&sizeSumA, 1, intMpi, mid2, 0, MPI_COMM_WORLD);
		MPI_Send(sumA, sizeSumA, intMpi, mid2, 0, MPI_COMM_WORLD);
		MPI_Send(&sizeSumB, 1, intMpi, mid2, 0, MPI_COMM_WORLD);
		MPI_Send(sumB, sizeSumB, intMpi, mid2, 0, MPI_COMM_WORLD);
		MPI_Send(&workersEndInterval, 1, intMpi, mid2, 0, MPI_COMM_WORLD);

		mpiKaratsubaPolyMulCompute(highParts, highA, (sizeA - halfPoint), highB, (sizeB - halfPoint), workersBeginInterval, mid1);
		MPI_Recv(lowParts, sizeLowParts, intMpi, mid1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		MPI_Recv(sumParts, sizeSumParts, intMpi, mid2, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	}
	else
	{
		if ((workersEndInterval - workersBeginInterval) > 1)
		{
			//std::cout << workersBeginInterval << " " << workersEndInterval << " will notify" << std::endl;
			for (int i = workersBeginInterval + 1; i < workersEndInterval; i++)
				MPI_Send(&noWorkToGive, 1, intMpi, i, 0, MPI_COMM_WORLD);
		}
		mpiKaratsubaPolyMulCompute(lowParts, lowA, halfPoint, lowB, halfPoint, workersBeginInterval, workersBeginInterval + 1);
		mpiKaratsubaPolyMulCompute(sumParts, sumA, sizeSumA, sumB, sizeSumB, workersBeginInterval, workersBeginInterval + 1);
		mpiKaratsubaPolyMulCompute(highParts, highA, (sizeA - halfPoint), highB, (sizeB - halfPoint), workersBeginInterval, workersBeginInterval + 1);
	}

	free(lowA);
	free(lowB);
	free(highA);
	free(highB);
	free(sumA);
	free(sumB);

	intT* shiftHighParts;
	intT sizeShiftHighParts = sizeHighParts + halfPoint * 2;
	shiftHighParts = (intT*)malloc(sizeShiftHighParts * sizeof(intT));

	intT* sumMinusHigh;
	intT sizeHighMinusSum = MAX(sizeHighParts, sizeSumParts);
	sumMinusHigh = (intT*)malloc(sizeHighMinusSum * sizeof(intT));

	polyShift(shiftHighParts, highParts, sizeHighParts, 2 * halfPoint);
	polySub(sumMinusHigh, sumParts, sizeSumParts, highParts, sizeHighParts);

	intT* shiftPlusLow;
	intT sizeShiftPlusLow = MAX(sizeShiftHighParts, sizeLowParts);
	shiftPlusLow = (intT*)malloc(sizeShiftPlusLow * sizeof(intT));

	intT* minusMinus;
	intT sizeMinusMinus = MAX(sizeHighMinusSum, sizeLowParts);
	minusMinus = (intT*)malloc(sizeMinusMinus * sizeof(intT));

	polyAdd(shiftPlusLow, shiftHighParts, sizeShiftHighParts, lowParts, sizeLowParts);
	polySub(minusMinus, sumMinusHigh, sizeHighMinusSum, lowParts, sizeLowParts);

	intT* finalShift;
	intT sizeFinalShift = sizeMinusMinus + halfPoint;
	finalShift = (intT*)malloc(sizeFinalShift * sizeof(int));

	polyShift(finalShift, minusMinus, sizeMinusMinus, halfPoint);

	polyAdd(result, shiftPlusLow, sizeShiftPlusLow, finalShift, sizeFinalShift);

	free(lowParts);
	free(highParts);
	free(sumParts);
	free(shiftHighParts);
	free(sumMinusHigh);
	free(minusMinus);
	free(shiftPlusLow);
	free(finalShift);
	//std::cout << workersBeginInterval << " " << workersEndInterval << " finished" << std::endl;
}

void mpiKaratsubaPolyMul(int &argc, char* argv[])
{
	MPI_Init(&argc, &argv);

	intT rank;

	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	if (rank == 0)
	{
		clock_t begin;
		clock_t end;
		const intT degree = 1000;
		const intT sizeA = degree;
		const intT sizeB = degree;
		intT a[sizeA];// = { 1, 2, 3 };//, 4, 5, 6, 7, 8, 9 };
		intT b[sizeB];// = { 4, 5, 6 };//, 12, 23, 45, 67, 7, 0 };
		const intT sizeResult = sizeA + sizeB - 1;
		intT result[sizeResult];
		intT numberOfWorkers;
		generatePoly(a, degree, 10);
		generatePoly(b, degree, 10);
		MPI_Comm_size(MPI_COMM_WORLD, &numberOfWorkers);
		begin = clock();
		mpiKaratsubaPolyMulCompute(result, a, sizeA, b, sizeB, 0, numberOfWorkers);
		end = clock();
		//printPoly(result, sizeA + sizeB - 1);
		std::cout << "\ntime: ";
		printf("%d ", (int)(double(end - begin) / CLOCKS_PER_SEC * 1000));
	}
	else if (rank >= 1)
	{
		intT* a;
		intT* b;
		intT sizeA;
		intT sizeB;
		intT workersEndInterval;
		intT resultSize;
		intT* result;
		intT givenWork;
		MPI_Status status;
		//std::cout << "Rank " << rank << " waiting data" << std::endl;
		MPI_Recv(&givenWork, 1, intMpi, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
		//std::cout << "Rank " << rank << " got data" << std::endl;
		if (givenWork == giveWork)
		{
			MPI_Recv(&sizeA, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			a = (int*)malloc(sizeA * sizeof(intT));
			MPI_Recv(a, sizeA, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Recv(&sizeB, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			b = (int*)malloc(sizeB * sizeof(intT));
			MPI_Recv(b, sizeB, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Recv(&workersEndInterval, 1, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			resultSize = sizeA + sizeB - 1;
			result = (int*)malloc(sizeof(intT) * resultSize);
			mpiKaratsubaPolyMulCompute(result, a, sizeA, b, sizeB, rank, workersEndInterval);
			MPI_Send(result, resultSize, intMpi, status.MPI_SOURCE, 0, MPI_COMM_WORLD);
			//std::cout << "Rank " << rank << "(" << resultBeginPos << ", " << resultEndPos << "): ";
			//printPoly(result, resultEndPos - resultBeginPos);
			//std::cout << std::endl;
			//MPI_Recv(&givenWork, 1, intMpi, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);

		}
	}

	MPI_Finalize();
}

int main(int argc, char* argv[])
{
	//mpiSimplePolyMul(argc, argv);
	mpiKaratsubaPolyMul(argc, argv);
    return 0;
}

