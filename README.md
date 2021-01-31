# jaccard-similarity-with-k-shingle

Big Data Course Project

There are approximately 1000 articles (from Associated Press, each with 300-500 characters) in dokumanlar.txt.

You can find jaccard similarity between theese articles by using k-shingle.

There are 3 types of shingles in the application.

1-Word shingle (like 2-shingle {The Supreme, Supreme Court, Court in})

2-Character shingle (like 2-shingle {Th, he, e, S, Su})

3-Stop Word shingle (like 2-shingle {The Supreme, in Johannesburg})


with method 1 and 3 shingle
listed jaccard similarity more than 0.5

  dokuman_3 <--> dokuman_7 -----> 0.89
  dokuman_5 <--> dokuman_9 -----> 1.00
  dokuman_11 <--> dokuman_14 -----> 0.88
  dokuman_13 <--> dokuman_15 -----> 0.92
  dokuman_104 <--> dokuman_206 -----> 0.98
  dokuman_123 <--> dokuman_524 -----> 0.98
  dokuman_152 <--> dokuman_481 -----> 0.98
  dokuman_198 <--> dokuman_545 -----> 0.98
  dokuman_199 <--> dokuman_374 -----> 0.98
  dokuman_265 <--> dokuman_881 -----> 0.98
  dokuman_283 <--> dokuman_919 -----> 0.98
  dokuman_290 <--> dokuman_747 -----> 0.98
  dokuman_333 <--> dokuman_803 -----> 0.98
  dokuman_373 <--> dokuman_775 -----> 0.98
