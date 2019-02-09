#ifndef CLEAN_DATA_H
#define CLEAN_DATA_H

#include <vector>
#include <string>
using namespace std;

// In order to search the video description for any clues, we have to clean the data first
// to clean the data, we need to split up the description into 'terms' which are any words separated by whitespace
// After splitting up the terms into a term vector, we filter out any terms for any stop words
// Stop words are any words in the stopwords.txt file
// After you filter out the vector of terms, return the terms in getTerms()
class CleanData {
    private:
        //
        std::vector<std::string> terms;

    public:
        // Takes in the text of a video description and splits it up via whitespace into terms vector
        CleanData(const std::string &video_description);

        // Filters out the terms for any words in the stopWords file
        // Use this function before passing into the database
        void filter(std::string stopwordsFile);

        // Getter for terms
        const std::vector<std::string> & getTerms();
};

#endif