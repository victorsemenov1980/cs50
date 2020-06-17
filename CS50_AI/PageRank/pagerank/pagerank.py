import os
import random
import re
import sys
import numpy as np
import bisect
import collections

DAMPING = 0.85
SAMPLES = 10


def main():
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl('corpus0')
    # corpus = crawl('corpus1')
    # corpus = crawl('corpus2')
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    # print (pages)
    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    quantity=len(corpus.keys())
    transition={}
    if len(corpus[page])==0:
        damping_factor=0
    universal=round((1-damping_factor)/quantity,3)
    for i in corpus.keys():
        transition[i]=universal
    specific=round(damping_factor/len(corpus[page]),3)   
    for i in corpus[page]:
        transition[i]+=specific
    return transition
    
    

# corpus={"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
# page="1.html"
# damping_factor=DAMPING

    
# print('Transition model   ',transition_model(corpus, page, damping_factor))
# print()


def weighted_choice_sub(population,weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return population[i]

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    sample={}
    for i in corpus.keys():
        sample[i]=0
     
    page=random.choice(list(corpus.keys()))
    k=0
    while k<n:
        t=transition_model(corpus, page, damping_factor)
        
        page = weighted_choice_sub(list(t.keys()), list(t.values()))
        for i in corpus.keys():
            sample[i]+=t[i]
        k+=1
        
    for k,v in sample.items():
        sample[k]=round(v/n,3)
        
    return sample        

# corpus={"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
# n=SAMPLES
# damping_factor=DAMPING

    
# print('Sample pagerank   ',sample_pagerank(corpus, damping_factor, n))


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    quantity=len(corpus.keys())
    iterate={}
    universal=(1-damping_factor)/quantity
    for i in corpus.keys():
        iterate[i]=1/quantity
    converge=0.001
    for i in corpus.keys():
        new_rank=0
        while iterate[i]-new_rank<=converge:
            x=damping_factor*(iterate[i]/len(corpus[i]))
            new_rank=universal+x
            if iterate[i]-new_rank>converge:
                iterate[i]=new_rank
                x=0
            
            
    return iterate

# corpus={"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
# n=SAMPLES
# damping_factor=DAMPING
# print('iterate pagerank   ',iterate_pagerank(corpus, damping_factor))
if __name__ == "__main__":
    main()
