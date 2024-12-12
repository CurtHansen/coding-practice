#ifndef TESTJSON_TEST_JSON_H
#define TESTJSON_TEST_JSON_H

void test_reading_external_file();
void test_construction();
void test_recursion();
void recursive(json, std::vector<json> &, const json&, const std::vector<std::string>&, int);


#endif //TESTJSON_TEST_JSON_H
