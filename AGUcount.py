#!/usr/bin/env python
'''
Per 2014 AGU "page count" metrics
https://liemohnjgrspace.wordpress.com/2014/01/29/agu-has-switched-to-publication-units/

This is not an official count! Check with your AGU editor for an official count estimate.
 '''
from warnings import warn
from texcounts import getcounts

INCLPUB = 25 # more than this, you're changed overlength fees
FIRSTCOST = 1000 # dollars
EXTRACOST = 125 # dollars per extra pub unit

def AGUpagecount(fn):
#%% count items
    counts = getcounts(fn)

    pubunits = (counts[1]/500 +  # one pub unit = 500 words
                counts[2] )             # one pub unit = table or figure

    return pubunits,counts[1:]

if __name__ == "__main__":
    from argparse import ArgumentParser
    p = ArgumentParser(description='Computes statistics of your Latex document')
    p.add_argument('texfn',help='filename of master .tex file to analyze')
    p = p.parse_args()

    pubunits,counts = AGUpagecount(p.texfn)
    dollars = (pubunits-INCLPUB)*EXTRACOST + FIRSTCOST

    if pubunits>INCLPUB:
        warn('You are overlength by {:.1f} pub units'.format(pubunits-INCLPUB))

    print('Pubunits: {:.1f}'.format(pubunits))
    print('tables/figures: {:.0f}'.format(counts[1]))
    print('words (incl. captions) {:.0f}'.format(counts[0]))
    print('equations {:.0f}'.format(counts[2]))