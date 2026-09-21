#include <iostream>
#include <vector>

std::vector<std::vector<double>> cartesian_product(const std::vector<std::vector<double>>&);
std::vector<std::vector<double>> recursive_cartesian_product(std::vector<std::vector<double>>&,
                                                             const std::vector<std::vector<double>>&,
                                                             const int);

std::vector<std::vector<double>> cartesian_product(const std::vector<std::vector<double>>& input_sets) {
    std::vector<std::vector<double>> initial;
    initial.clear();
    for (auto const& element: input_sets[0]){
        std::vector<double> temp{element};
        initial.push_back(temp);
    }
    std::vector<std::vector<double>> result = recursive_cartesian_product(initial,input_sets,1);
    return result;
}

std::vector<std::vector<double>> recursive_cartesian_product(std::vector<std::vector<double>>& cumulative,
                                                             const std::vector<std::vector<double>>& input_sets,
                                                             const int level){
    if (level == input_sets.size()){
        return cumulative;
    } else {
        std::vector<std::vector<double>> new_vector;
        new_vector.clear();
        for (auto const& vec: cumulative){
            for (auto const& elem: input_sets[level]){
                std::vector<double> temp;
                temp.insert(temp.end(), vec.begin(), vec.end());
                temp.push_back(elem);
                new_vector.push_back(temp);
            }
        }
        return recursive_cartesian_product(new_vector, input_sets, level+1);
    }
}

int main() {
    std::vector<std::vector<double>> input{{1,2},{30,40,50},{100,200},{1000}};
    std::vector<std::vector<double>> result = cartesian_product(input);
    for (auto const& row: result) {
        for (auto const& elem: row) {
            std::cout << elem << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
