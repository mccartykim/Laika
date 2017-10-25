# Laika, a tribute to Botnik
## not the_dog_dies.py
### why would you think that

I recently heard about a neat piece of "augmented writing" software called Botnik, which lets authors come up with weird nonsequiters vaguely in the style of the source material using markov chains/ngrams.

Meanwhile, at the Recurse Center, folks have been talking about tries and other prefix trees. I'd like to see if I can use that to make an elegant markov chain, or at least get a better feel for the structure. There may well be limitations to the benefit beyond just sets of words and pointers to other words. :-(

So I'm gonna write a cutesy little tribute.  I'd like a website frontend (maybe serialize my Python-generated tries as JSON or something)