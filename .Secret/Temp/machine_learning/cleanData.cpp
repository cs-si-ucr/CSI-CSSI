#include "database.h"
#include "cleanData.h"

// Takes in the text of a video description and splits it up via whitespace into terms vector
CleanData::CleanData(const std::string &video_description) {

}

// Filters out the terms for any words in the stopWords file
// Use this function before passing into the database
void CleanData::filter(std::string stopwordsFile) {

}

// Getter for terms
const std::vector<std::string> & CleanData::getTerms() {
    return terms;
}