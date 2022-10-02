// Phi approximation
#include <math.h>
#include <stdio.h>
#include <omp.h>

int main() {
    int N = 1680000000;    // arbitrary number

    double start = omp_get_wtime();

    double sum = 0.0;
    #pragma omp parallel for default(none) shared(N) reduction(+:sum)
    for (int i = 1; i <= N; ++i) {
#ifdef DEBUG
        if (i == 1) {
            printf("Cores used %d\n", omp_get_num_threads());
        }
#endif
        sum += 1.0 / (1.0 + pow(((double)i - 0.5) / N, 2.0));
    }
    double phi = (sum / N) * 4;

    double finish = omp_get_wtime();
    printf("Phi value: %.10lf\n", phi);
    printf("Calc time: %.5lf\n", (finish - start));

    return 0;
}