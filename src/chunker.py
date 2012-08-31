#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json
import pyparsing
from jpype import *

class PennTreebackChunker(object):
  def __init__(self):
    classpath = "jars/StanfordChunkerWrapper.jar:jars/stanford/stanford-parser.jar:jars/stanford/stanford-parser-2012-03-09-models.jar"
    startJVM(getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)
    Chunker = JClass("com.cognizant.awcoe.nlp.chunker.ChunkerWrapper") 
    self.chunk = Chunker().chunk
    self.penn_treebank_expr = pyparsing.nestedExpr('(', ')')

  def _nestedlist2dict(self, d, l):
    if not l[0] in d:
      d[l[0]] = {}
    for v in l[1:]:
      if type(v) == list:
        self._nestedlist2dict(d[l[0]],v)
      else:
        d[l[0]] = v

  def chunk_string(self, sentence, json_response=False):
    penn = self.chunk(sentence)
    penn = self.penn_treebank_expr.parseString(penn).asList()[0]
    penn_str = {}
    self._nestedlist2dict(penn_str, penn)
    return json.dumps(penn_str) if json_response else penn_str

  def close(self):
    shutdownJVM()
