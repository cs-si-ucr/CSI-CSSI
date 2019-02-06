#ifndef CLEAN_DATA_H
#include <vector>
#include <iostream>

class CleanData {
    private:
        vector<string> terms;

    public:
        // Takes in the text of a video description and splits it up via whitespace into terms vector
        CleanData(const string &video_description);
        // Filters out the terms for any words in the stopWords file
        // Use this function before passing into the database
        void filter(string stopwordsFile);
        // Getter for terms
        const vector<int> & getTerms();
}

#endif