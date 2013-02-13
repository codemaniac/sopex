## Synopsis

Library and CLI to extract the subject, predicate and object for a given english sentence

## Status

Development

## Installation

### Source

    $ git clone https://github.com/codemaniac/sopex.git
    $ cd sopex
    $ python setup.py install

### PyPI

    $ easy_install sopex

## Usage

### Help

	$ sopex -h

### CLI

	$ sopex "A rare black squirrel has become a regular visitor to a suburban garden"

### Library

    >>> import sopex
    >>> sentence = 'A rare black squirrel has become a regular visitor to a suburban garden'
    >>> triplet = sopex.extract(sentence)
    >>> print triplet.subject, triplet.predicate, triplet.object

## Contributors

ashish.ap.rao@gmail.com

## License

Copyright (c) 2013, Ashish Prasad
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 
