#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
#include <random>
#include "test_json.h"


int main() {
    test_reading_external_file();
    test_construction();
    test_recursion();
    return 0;
}

void test_reading_external_file() {
    std::cout << "\n\ntest_reading_external_file()\n" << std::endl;

    json all_info = R"(
                        {
                            "AddtnlMOI": 1,

                            "MOIInformation": {
                                "1": {
                                    "frequency": 0.1,
                                    "proportion_profiles": [[1.0]]
                                },
                                "2": {
                                    "frequency": 0.3,
                                    "proportion_profiles": [[0.01,0.99],[0.02,0.98],[0.05,0.95],[0.1,0.9],[0.4,0.6],[0.5,0.5]]
                                }
                            },
                            "Scenarios": [  {"C":1000000,"FPMode":0,"FPConcentration":100,"AllelePropCutoff":0.0},
                                            {"C":1000000,"FPMode":0.05,"FPConcentration":100,"AllelePropCutoff":0.0},
                                            {"C":1000000,"FPMode":0.0,"FPConcentration":100,"AllelePropCutoff":0.05},
                                            {"C":1000,"FPMode":0.00,"FPConcentration":100,"AllelePropCutoff":0.0}]
                        }
                    )"_json;

    std::cout << "There are " << all_info.size() << " entries at the top level." << std::endl;
    for (auto& elem: all_info.items()){
        std::cout << elem.key() << std::endl;
    }

    auto value = all_info["AddtnlMOI"];
    std::cout << "\nFor 'AddtnlMOI'," << std::endl;
    std::cout << "  value: " << value <<  std::endl;
    std::cout << "  value.size(): " << value.size() << std::endl;
    std::cout << "  value.is_number(): " << value.is_number() << std::endl;
    std::cout << "  value.is_array(): " << value.is_array() << std::endl;
    std::cout << "  value.is_object(): " << value.is_object() << std::endl;

    value = all_info["MOIInformation"];
    std::cout << "\nFor 'MOIInformation'," << std::endl;
    std::cout << "  value: " << value <<  std::endl;
    std::cout << "  value.size(): " << value.size() << std::endl;
    std::cout << "  value.is_number(): " << value.is_number() << std::endl;
    std::cout << "  value.is_array(): " << value.is_array() << std::endl;
    std::cout << "  value.is_object(): " << value.is_object() << std::endl;

    value = all_info["MOIInformation"]["1"];
    std::cout << "\nFor 'MOIInformation[1]'," << std::endl;
    std::cout << "  value: " << value <<  std::endl;
    std::cout << "  value.size(): " << value.size() << std::endl;
    std::cout << "  value.is_number(): " << value.is_number() << std::endl;
    std::cout << "  value.is_array(): " << value.is_array() << std::endl;
    std::cout << "  value.is_object(): " << value.is_object() << std::endl;

    value = all_info["MOIInformation"]["1"]["proportion_profiles"];
    std::cout << "\nFor 'MOIInformation[1][[proportion_profiles]'," << std::endl;
    std::cout << "  value: " << value <<  std::endl;
    std::cout << "  value.size(): " << value.size() << std::endl;
    std::cout << "  value.is_number(): " << value.is_number() << std::endl;
    std::cout << "  value.is_array(): " << value.is_array() << std::endl;
    std::cout << "  value.is_object(): " << value.is_object() << std::endl;
    std::vector<std::vector<float> > temp = value.get<std::vector<std::vector<float>>>();
    std::cout << temp[0][0] << std::endl;

    value = all_info["Scenarios"];
    std::cout << "\nFor 'Scenarios'," << std::endl;
    std::cout << "  value: " << value <<  std::endl;
    std::cout << "  value.size(): " << value.size() << std::endl;
    std::cout << "  value.is_number(): " << value.is_number() << std::endl;
    std::cout << "  value.is_array(): " << value.is_array() << std::endl;
    std::cout << "  value.is_object(): " << value.is_object() << std::endl;

    value = all_info["Scenarios"][0];
    std::cout << "\nFor 'Scenarios[0]'," << std::endl;
    std::cout << "  value: " << value <<  std::endl;
    std::cout << "  value.size(): " << value.size() << std::endl;
    std::cout << "  value.is_number(): " << value.is_number() << std::endl;
    std::cout << "  value.is_array(): " << value.is_array() << std::endl;
    std::cout << "  value.is_object(): " << value.is_object() << std::endl;
}

void test_construction(){
    std::cout << "\n\ntest_construction()\n" << std::endl;

    std::map<std::string, float> mymap;
    mymap["value1"] = 1.0;
    mymap["value2"] = 2.0;
    mymap["value3"] = 3.0;

    json myjson(mymap);
    for (auto& elem: myjson.items()) {
        std::cout << elem << std::endl;
    }
}

void test_recursion(){
    std::cout << "\n\ntest_recursion()\n" << std::endl;

    std::vector<json> list_of_jsons;
    json master_json = R"(
                        {
                            "Value1": 1,
                            "Value2": [1,2,3],
                            "Value3": [10,20,30],
                            "Value4": 100,
                            "Scenarios": [  {"C":1000000,"FPMode":0,"FPConcentration":100,"AllelePropCutoff":0.0},
                                            {"C":1000000,"FPMode":0.05,"FPConcentration":100,"AllelePropCutoff":0.0},
                                            {"C":1000000,"FPMode":0.0,"FPConcentration":100,"AllelePropCutoff":0.05},
                                            {"C":1000,"FPMode":0.00,"FPConcentration":100,"AllelePropCutoff":0.0}]
                        }
                    )"_json;

    std::vector<std::string> all_keys = {"Value1","Value2","Value3","Value4","Scenarios"};
    json temp;

    recursive(temp,list_of_jsons,master_json,all_keys,0);

    std::cout << "There are " << list_of_jsons.size() << " entries in the constructed list!" << std::endl;
    for (auto& elem: list_of_jsons) {
        std::cout << elem << std::endl;
    }
}

void recursive(json current, std::vector<json> &list, const json& master_json, const std::vector<std::string>& key_names, int level) {
    if (level==key_names.size()){
        list.push_back(current);
    } else {
        if (master_json[key_names[level]].is_array()) {
            for (auto const &value: master_json[key_names[level]]) {
                if (value.is_object()) {
                    current.update(value);
                } else {
                    current[key_names[level]] = value;
                }
                recursive(current, list, master_json, key_names, level + 1);
            }
        } else {
            current[key_names[level]]=master_json[key_names[level]];
            recursive(current,list,master_json,key_names,level+1);
        }
    }
}