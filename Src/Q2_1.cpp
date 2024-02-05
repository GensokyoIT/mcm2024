// Online C++ compiler to run C++ program online
#include <iostream>
#include <random>
#include <vector>

using namespace std;

// restrict the male reproduction times within 5 times
// male reproduction rate
const double mrr[6] = {0, 1.0, 0.4107, 0.1071, 0.0714, 0.0178};

// max population of lamprey we imagine
#define MAX 10000

vector<double> female(MAX + 1), male(MAX + 1);
vector<int> mate_list[MAX + 1];
vector<double> child(MAX + 1);

int main() {

	default_random_engine eng(time(0));
	uniform_real_distribution<double> uni(0.0, 1.0);

	for (int i = 1; i <= MAX; i++) {
		female[i] = uni(eng);
		male[i] = uni(eng);
	}

	mt19937 rnd(time(0));

	for (int i = 1; i <= MAX; i++) {
		int mate_count = 0;
		while (true) {

			mate_count++;
			if (uni(eng) > mrr[mate_count])
				break;

			int female_id = rnd() % MAX + 1;
			mate_list[female_id].push_back(i);
		}
	}

	int child_count = 0;
	double child_average = 0;

	// " clever " female strategy
	// female will only accept the best male
	for (int i = 1; i <= MAX; i++)
		if (!mate_list[i].empty()) {
			child_count++;
			child[i] = 0;
			for (int m : mate_list[i])
				child[i] = max(child[i], (female[i] + male[m]) / 2);
			child_average += child[i];
		}
	child_average /= child_count;

	cout << child_average;

	return 0;
}
