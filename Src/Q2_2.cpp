
// Online C++ compiler to run C++ program online
#include <random>
#include <vector>
#include <iostream>
using namespace std;

// restrict the male reproduction times within 5 times
// male reproduction rate
const double mrr[6]={0, 1.0, 0.4107, 0.1071, 0.0714, 0.0178};

// max population of lamprey we imagine
#define MAX 10000

vector<double> female( MAX + 1 ), male( MAX + 1 );
vector<int> mate_list[ MAX + 1 ];
vector<double> child( MAX + 1 );

default_random_engine eng( 0 );
uniform_real_distribution<double> uni( 0.0, 1.0 );

bool check( double fm, double m ){
    if( m <= fm / 2 )
        return false; // reject
    if( m <= fm )
        return uni( eng ) <= 0.7 * ( m - fm / 2) / ( fm / 2 ); // accept
    if( m > fm )
        return 0.7 + 0.3 * ( m - fm ) / ( 1.0 - fm );
} 

int main() {
    
    for( int i = 1; i <= MAX; i ++ ) {
        female[i] = uni( eng );
        male[i] = uni( eng );
    }
    
    mt19937 rnd( time( 0 ) );
    
    for( int i = 1; i <= MAX; i ++ ) {
        int mate_count = 0;
        while( true ) {
            
            mate_count ++;
            if( uni( eng ) > mrr[mate_count] )
                break;
            
            int female_id = rnd() % MAX + 1;
            mate_list[ female_id ].push_back( i );
            
        }
    }
    
    int child_count = 0;
    double child_average = 0;
    
    // " probability " female strategy
    // female will accept male on probability
    // and the probability is influenced by the size of the male
    for( int i = 1; i <= MAX; i ++ )
        if( !mate_list[ i ].empty() ) {
        //    child_count ++;
        //    child[ i ] = 0;
            child[ i ] = -1;
            for( int m : mate_list[ i ] ) {
                if( !check( female[ i ], male[ m ] ) )
                    break;
                child[ i ] = ( female[ i ] + male[ m ] ) / 2;
            }
            if( child[ i ] >= 0.0 ) {
                child_count ++;
                child_average += child[ i ];
            }
        //    child_average += child[ i ];
        }
    child_average /= child_count;
    
    cout << child_count << " " << child_average;
    
    return 0;
}
