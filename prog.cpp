#include <iostream>
#include <cstdlib>
#include <vector>
#include <numeric>

using namespace std;

double random_double()
{
    return ((double)rand())/RAND_MAX;
}

class DataArray
{
private:
    const vector<size_t> dims;
    const size_t count;
    double * const data;
    vector<size_t> base;

public:
    /**
     * Constructor
     * 
     * Play fast and loose with the input, assuming len(_dims) > 0 and
     * _dims[i] > 0 for all elements.
     */
    DataArray(vector<size_t> const & _dims)
        : dims(_dims)
        , count(accumulate(dims.begin(), dims.end(), 1, multiplies<size_t>()))
        , data(new double[count])
    {
        assert(dims.size() > 0);
        assert(count > 0);
        generate(data, data+count, random_double);

        size_t value = count;
        for (size_t i = 0 ; i < dims.size() ; ++i) {
            value /= dims[i];
            base.push_back(value);
        }
    }

    ~DataArray()
    {
        delete[] data;
    }

    double corr() const
    {
        double val = data[count/2];
        cout << val << endl;
        return val;
    }
};

int
main()
{
    srand(time(0));
    vector<size_t> bounds = {8,8,8,8}; 
    DataArray data(bounds);
    data.corr();

    return 0;
}
