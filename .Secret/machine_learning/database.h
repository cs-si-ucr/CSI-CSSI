#ifndef DATABASE_H
#define DATABASE_H

#include <string>
#include <vector>

class Database {
    public:
        std::string match(const std::vector<std::string> &vs);
};

#endif