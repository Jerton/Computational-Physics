#include<bits/stdc++.h>
using namespace std;

void mc_sampling(int initial_n_particles, int
max_time,
double decay_probability, int *ncumulative)
{
int time, np, n_unstable, particle_limit;
n_unstable = initial_n_particles;
// accumulate the number of particles per time
step per trial
ncumulative[0] = initial_n_particles;
// loop over each time step
for (time=1; time <= max_time; time++){
particle_limit = n_unstable;
for ( np = 1; np <= particle_limit; np++) {
if( double(rand())/RAND_MAX <=
decay_probability) {
n_unstable=n_unstable-1;
}
} // end of loop over particles
ncumulative[time] = n_unstable;
} // end of loop over time steps
} // end mc_sampling function



int main() {
    int initial_n_particles = 100;  // Adjust as needed
    int max_time = 10;  // Adjust as needed
    double decay_probability = 0.1;  // Adjust as needed

    // Allocate memory for the ncumulative array
    int *ncumulative = (int *)malloc((max_time + 1) * sizeof(int));

    // Check if memory allocation is successful
    if (ncumulative == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;  // Return an error code
    }

    // Run the Monte Carlo simulation
    mc_sampling(initial_n_particles, max_time, decay_probability, ncumulative);

    // Print the results
    for (int time = 0; time <= max_time; time++) {
        printf("Time: %d, Cumulative Particles: %d\n", time, ncumulative[time]);
    }

    // Free allocated memory
    free(ncumulative);

    return 0;  // Return success
}
