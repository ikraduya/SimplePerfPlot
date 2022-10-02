// Phi approximation
#include <stdio.h>
#include <math.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int N = 1680000000;    // arbitrary number

    int rank = 0, cluster_size = 0;
    MPI_Comm comm = MPI_COMM_WORLD;
    int root = 0;
    
    MPI_Init(&argc, &argv);
    MPI_Comm_size(comm, &cluster_size);
    MPI_Comm_rank(comm, &rank);

#ifdef DEBUG
    if (rank == root) {
        printf("Cluster size %d\n", cluster_size);
    }
#endif

    double phi;
    double starttime = 0.0, endtime = 0.0;
    MPI_Barrier(comm);
    starttime = MPI_Wtime();

    double local_sum = 0.0;
    int startI = 1 + rank;
    for (int i = startI; i <= N; i += cluster_size) {
        local_sum += 1.0 / (1.0 + pow(((double)i - 0.5) / N, 2.0));
    }

    double global_sum;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_DOUBLE, MPI_SUM, root, comm);

    if (rank == root) {
        phi = (global_sum / N) * 4;
    }

    MPI_Barrier(comm);
    endtime = MPI_Wtime();

    if (rank == root) {
        printf("Phi value: %.10lf\n", phi);
        printf("Calc time: %.5lf\n", (endtime - starttime));
    }

    MPI_Finalize();

    return 0;
}
