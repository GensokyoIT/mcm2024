
// another strategy **************************************************************************

// 搞错了，乱码部分是中文，不小心保存成ANSI了
// 大致意思就是下面三篇文章说明了一些基因与体型的关系，这个关系不是简单的显隐性，有的是重复基因多次表达的机制，所以方案1、2中用的平均父母体型是有价值的
// 不过我还是做了个显性的模型

// ע          ģ   û  ע ⵽  Щ     Ƿ        ԵĹ ϵ    Ϊ        ػ   ܶ࣬   ұ ︴
//  ܶ༤ صı ﷽ʽ   ظ   λ   Ȼ   α    Ը       ļ򵥸 ĸȡ  ֵ  ʽ    Ŀ        Ŵ
//             Ȼ       ĳλ    һ         Թ ϵ  Ȼ    һ    ʾ    Ҫ              Եļ

// https://www.sciencedirect.com/science/article/abs/pii/S0380133091713634  关于生长抑素的研究
// https://www.sciencedirect.com/science/article/pii/S0016648016302362?via%3Dihub 性别比、体型的关联
// https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4275091/ 基因与体型、迁徙能力的关联

// the following code assume gene S makes the lamprey bigger, and s has no effect
// and it will show that after reproduction, lampreys grow bigger and S gene frequency grows

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

// lets make gene simple
// let gene be S and s , S is dominant
// the percentage of S in population is d_rate
// we put an interger tag to describe genotype, 0 is ss, 1 is Ss or sS, and 2 is SS

double d_rate = 0.5;
vector<int> fm_gene(MAX + 1), m_gene(MAX + 1), c_gene(MAX + 1);
vector<int> mate_list[MAX + 1];
vector<double> child(MAX + 1);

default_random_engine eng(0);
uniform_real_distribution<double> uni(0.0, 1.0);

mt19937 rnd(time(0));
// x for female's Id, y for male's Id, c_gene for child's gene
void give_birth(int x, int y) {
	switch (fm_gene[x]) {
	case 1:
		if (uni(eng) <= 0.5)
			c_gene[x]++;
		break;
	case 2:
		c_gene[x]++;
	}
	switch (m_gene[y]) {
	case 1:
		if (uni(eng) <= 0.5)
			c_gene[x]++;
		break;
	case 2:
		c_gene[x]++;
	}
    // if child's gene >= 1 then child has S gene, then child's length is 1.0
	child[x] = (c_gene[x] >= 1);
}

int main() {
	// initialize female and male's gene and length
	for (int i = 1; i <= MAX; i++) {
		fm_gene[i] = m_gene[i] = 0;
		for (int j = 1; j <= 2; j++) {
			fm_gene[i] += (uni(eng) <= d_rate ? 1 : 0);
			m_gene[i] += (uni(eng) <= d_rate ? 1 : 0);
		}
		female[i] = (fm_gene[i] >= 1);
		male[i] = (m_gene[i] >= 1);
	}
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
	double new_d_rate = 0;

	// " clever " female strategy
	// female will only accept the best male
	for (int i = 1; i <= MAX; i++)
		if (!mate_list[i].empty()) {
			child_count++;
			child[i] = 0;
			c_gene[i] = 0;
			int best_male_id = mate_list[i][0];
			for (int m : mate_list[i])
				if (male[m] > male[best_male_id])
					best_male_id = m;
			give_birth(i, best_male_id);
			new_d_rate += c_gene[i];
			child_average += child[i];
		}
	child_average /= child_count;
    // new_d_rate is the sum of S gene in child S gene frequency
	new_d_rate /= (child_count * 2);

	cout << child_count << " " << child_average << endl;
	cout << new_d_rate;

	return 0;
}
