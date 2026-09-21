#include <iostream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
#include <armadillo>
#include <random>

int main() {

    json j = R"({
                    "param": 1,
                    "MOIInformation": {
                        "3":
                            {"frequency": 0.3,
                             "proportion_profiles": [[0.05, 0.15, 0.20, 0.60],[0.1, 0.2, 0.7], [0.2, 0.3, 0.5]]},
                        "4":
                            {"frequency": 0.7,
                             "proportion_profiles": [[0.1, 0.2, 0.3, 0.4], [0.05, 0.1, 0.25, 0.6]]}
                    }
                })"_json;

    std::default_random_engine generator(42);

    int maxmoi = 0;
    for (auto const& elem: j["MOIInformation"].items()){
        maxmoi = std::max(maxmoi,std::stoi(elem.key()));
    }
    std::vector<float> moi_frequencies(maxmoi);
    for (auto const& elem: j["MOIInformation"].items()){
        moi_frequencies[std::stoi(elem.key())-1] = elem.value()["frequency"];
    }
    std::discrete_distribution<int> moi_distribution(moi_frequencies.begin(),moi_frequencies.end());

    json counts;
    counts["3/0"] = 0;
    counts["3/1"] = 0;
    counts["3/2"] = 0;
    counts["4/0"] = 0;
    counts["4/1"] = 0;

    for (int i=0; i<100000; i++){
        int chosen_moi = moi_distribution(generator)+1;
        int num_options = j["MOIInformation"][std::to_string(chosen_moi)]["proportion_profiles"].size();
        std::uniform_int_distribution<int> uniform(0,num_options-1);
        int chosen_proportions = uniform(generator);
        std::vector<float> temp = j["MOIInformation"][std::to_string(chosen_moi)]["proportion_profiles"][chosen_proportions];
        arma::Col<float> proportions(temp);

        std::string desc = std::to_string(chosen_moi)+"/"+std::to_string(chosen_proportions);
        int current = counts[desc];
        counts[desc] = current + 1;
    }
    std::cout << counts.dump(4) << std::endl;
    return 0;
}
