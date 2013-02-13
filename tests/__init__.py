#!/usr/bin/python
# -*- coding: utf-8 -*-

import sopex

sentences = [
  'Monkeys are destroying the garden',
  'No man can serve two masters',
  'When students travel to US, they usually go by air',    
  'The Earth revolves around the sun',
  'Honesty is the best policy.',
  'John F. Kennedy was elected as US President in 1960.',
  'The quick brown fox jumps over the lazy dog.',
  'A rare black squirrel has become a regular visitor to a suburban garden',
  'As with every Sony PDA before it, the NR70 series is equipped with Sony\'s own memory stick expansion.'
]

count = 0

for sentence in sentences:
  sop_triplet = sopex.extract(sentence)
  count = count + 1 if sop_triplet.subject and sop_triplet.predicate and sop_triplet.object else count

assert count == len(sentences)
